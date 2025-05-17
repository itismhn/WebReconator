# 🌐 WebReconator

**WebReconator** is a modular web reconnaissance toolkit designed for security analysts, penetration testers, and bug bounty hunters. It automates a suite of essential web security checks to assist in the reconnaissance phase of offensive security assessments.

---

## 🧰 Features

- 🔐 **HeaderSafe** – Analyze and report missing or misconfigured HTTP security headers (e.g., `Content-Security-Policy`, `Strict-Transport-Security`).
- 🚪 **Verb Tampering** – Enumerate and test HTTP methods like `PUT`, `DELETE`, `OPTIONS` to discover potential misconfigurations.
- 📂 **Sensitive Directory Check** – Detect exposed files and directories such as `.git`, `.env`, `backup.zip`, and more.
- 🌍 **WHOIS Lookup** – Retrieve WHOIS information of the target domain to gather registration and ownership data.
- 🔎 **SSL Inspector** – Scan and evaluate the target's SSL/TLS setup and supported cipher suites to identify weak or deprecated configurations.

## Getting Started 🚀

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/webreconator.git
   cd webreconator

### Install dependencies
```bash
pip install -r requirements.txt
```

## Usage
### Interactive Mode
Launch the tool and choose modules interactively:
```bash
python webreconator.py
```
You’ll be prompted to enter the target URL and then choose from the menu.

### Command-Line Mode
#### Run All Modules
Run all modules against a target URL:
```bash
python webreconator.py -u https://example.com
```

## File Structure

```bash
webreconator/
├── webreconator.py          # Main CLI entrypoint
├── modules/
│   ├── headersafe.py
│   ├── verbtampering.py
│   ├── sencheck.py
│   ├── who_is.py
│   └── ssl_inspector.py
└── requirements.txt
```

