# ShieldPass

ShieldPass is a Python tool that checks password strength and alerts users if their passwords are weak or have appeared in known data breaches. It helps improve security and encourages better password hygiene, all while respecting user privacy.

## Features

- Checks password complexity (length, uppercase, lowercase, digits, special characters)  
- Detects if the password has been compromised in known data breaches  
- Uses privacy-preserving methods to ensure user passwords are never fully exposed  
- Simple command-line interface, easy to use  

## Why ShieldPass?

Passwords are often the weakest link in security. ShieldPass empowers users to understand the strength of their passwords and avoid reusing compromised ones, helping reduce the risk of account breaches.

---

## Requirements

- Python 3.x installed on your computer  
- `requests` Python package

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/shieldpass.git
cd shieldpass
pip3 install requests

python3 shieldpass.py
