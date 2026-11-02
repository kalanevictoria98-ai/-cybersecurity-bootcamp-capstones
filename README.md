# 🛡️ Cybersecurity Bootcamp Capstone Portfolio

Welcome to my capstone project portfolio! This repository contains the major milestone projects completed during my HyperionDev Cybersecurity Bootcamp. It showcases practical applications of multi-layered identity verification, cryptographic string manipulations, and automated vulnerability exploitation inside an isolated laboratory environment.

---

## 📂 Featured Capstone Projects

### 🔐 1. Custom Multi-Factor Authentication (MFA) Engine
**File:** `Python for Cybersecurity (mfa_automation)`

* **The Problem It Solves:** Single-factor authentication (passwords alone) leaves infrastructure exposed to compromise. This application creates a secure, three-layer (3FA) validation workflow checking distinct identity tokens sequentially.
* **Key Technical Implementations:**
  * **Zero-Plaintext Signatures:** Encodes sensitive text arrays into unique hexadecimal strings using deterministic `SHA-256` hash functions.
  * **RFC 6238 Compliant TOTP Engine:** Uses `HMAC-SHA1` calculations, Base32 secret decoding, and big-endian `struct` packaging to dynamically evaluate 6-digit tokens across 30-second intervals.
  * **Biometric Inherence Simulation:** Enforces process execution logic by verifying cryptographically hashed mock physical inputs before system entry is allowed.
* **Technologies Used:** `Python 3.x` | `hashlib` | `hmac` | `struct` | `base64` | `time`

---

### 🔑 2. Automated Caesar Cipher Encoder Utility
**File:** `Ciphers.py` (or `cipher.py`)

* **The Problem It Solves:** Storing or transferring plain text data without encryption leaves confidential messages vulnerable to unauthorized disclosure. This utility securely encodes a text string by shifting alphabetical characters cleanly across a structural boundary.
* **Key Technical Implementations:**
  * **Cyclical Boundary Shifts:** Programmatically processes each character, executing a precise `+15` positional shift inside the standard 26-character alphabet using mathematical modulo (`% 26`) tracking.
  * **Strict Input Sanitization:** Processes lowercase (`a-z`) and uppercase (`A-Z`) boundary conditions independently through character byte values (`ord()`), keeping original spaces and punctuation untouched.
* **Technologies Used:** `Python 3.x` | `String Indexing` | `Mathematical Modulo Logic`

---

### 🖥️ 3. Basic Pentesting: Target Machine Vulnerability & Exploitation Report
**File:** `Case Study for Local VM.pdf`

* **The Problem It Solves:** Misconfigured open services on public or private networks act as direct entry channels for unauthorized attackers. This report walks through the stages of discovery, target identification, and automated service exploitation.
* **Key Technical Implementations:**
  * **Reconnaissance & Footprinting:** Uses `Nmap` service version scanning to profile running ports (`21`, `22`, `80`) and evaluate target services (`ProFTPD 1.3.5c`, `OpenSSH 7.2p2`, `Apache 2.4.18`).
  * **Backdoor Exploitation:** Leverages the Metasploit Framework to select, configure, and execute the `exploit/unix/ftp/proftpd_133c_backdoor` mechanism, adjusting payload options from basic reverse connections to a successful functional bind shell (`cmd/unix/bind_perl`).
  * **Credential Auditing & Cracking:** Extracts target shadow files (`/etc/passwd` and `/etc/shadow`) and implements dictionary attacks using `John the Ripper` to isolate and crack target user credentials.
* **Skills Demonstrated:** `Vulnerability Analysis` | `Metasploit Framework` | `Network Mapping (Nmap)` | `Password Crack Utilities`

---

## 🚀 Setting Up & Running the Python Scripts

### Prerequisites
Make sure you have a standard installation of Python 3. This portfolio utilizes standard library tools with zero external dependencies to maintain system audit stability:
```bash
python3 --version
```

### Execution Steps
1. Clone this capstone portfolio to your local engineering workspace:
   ```bash
   git clone https://github.com
   ```
2. Change into the root project container:
   ```bash
   cd -cybersecurity-bootcamp-capstones
   ```
3. Launch the Cipher text encoder script:
   ```bash
   python3 Ciphers.py
   ```

---

## 👥 Professional Contacts
* **LinkedIn:** [Your Professional Profile Link]
* **Email:** kalanevictoria98@gmail.com
