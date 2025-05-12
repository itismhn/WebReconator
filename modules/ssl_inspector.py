import ssl
import socket
import contextlib
import warnings
from typing import Any, Dict, List
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.utils import CryptographyDeprecationWarning

warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

def _get_certificate_extensions(cert: x509.Certificate) -> Dict[str, Any]:
    ext_dict = {}
    for ext in cert.extensions:
        ext_name = getattr(ext.oid, "_name", None) or ext.oid.dotted_string
        ext_dict[ext_name] = {"critical": ext.critical, "value": str(ext.value)}
    return ext_dict

def _get_supported_ciphers(host: str, port: int) -> List[str]:
    available_ciphers = ssl.create_default_context().get_ciphers()
    supported_ciphers = []

    for cipher in available_ciphers:
        cipher_name = cipher["name"]
        with contextlib.suppress(Exception):
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.set_ciphers(cipher_name)
            context.options |= ssl.OP_NO_COMPRESSION
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE

            with socket.create_connection((host, port), timeout=2) as sock:
                with context.wrap_socket(sock, server_hostname=host):
                    supported_ciphers.append(cipher_name)

    return supported_ciphers

def _get_certificate_info(host: str, port: int) -> Dict[str, Any]:
    try:
        pem_data = ssl.get_server_certificate((host, port))
        cert = x509.load_pem_x509_certificate(pem_data.encode(), default_backend())
    except Exception as e:
        raise RuntimeError(f"Failed to retrieve or parse certificate: {e}")

    cert_info = {
        "version": cert.version.name,
        "serial": cert.serial_number,
        "validity": {
            "not_valid_before": str(cert.not_valid_before),
            "not_valid_after": str(cert.not_valid_after),
        },
        "issuer": {getattr(attr.oid, "_name", None) or attr.oid.dotted_string: attr.value for attr in cert.issuer},
        "fingerprints": {
            "SHA256": cert.fingerprint(hashes.SHA256()).hex(),
            "SHA1": cert.fingerprint(hashes.SHA1()).hex(),
        },
        "extensions": _get_certificate_extensions(cert),
    }
    return cert_info

def ssl_inspect(host: str, port: int = 443) -> Dict[str, Any]:
    print(f"[*] Inspecting {host}:{port} ...")

    cert_info = _get_certificate_info(host, port)
    ciphers = _get_supported_ciphers(host, port)

    print(f"\n[+] Supported Cipher Suites for {host}:{port}:")
    for cipher in ciphers:
        print(f"  - {cipher}")

    result = {
        "certificate": cert_info,
        "supported_ciphers": ciphers,
    }
    return result

# Prevent automatic execution on import
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python ssl_inspector.py <host> <port>")
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        ssl_inspect(host, port)