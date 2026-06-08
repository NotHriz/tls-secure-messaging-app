# TLS‑Secured Messaging App

A lightweight Flask app that demonstrates TLS encryption by sending messages over HTTP (plaintext) or HTTPS (encrypted).  
Run it on your local network, capture traffic with Wireshark, and compare the intercepted payloads.

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate a self‑signed TLS certificate (only needed for HTTPS)
```bash
openssl req -x509 -newkey rsa:2048 -keyout ssl/server.key -out ssl/server.crt -days 365 -nodes -subj "/CN=192.168.0.1"
```
*Replace `192.168.0.1` with your server’s actual IP.*

### 3. Run the server
Choose one of the following commands:

| Mode | Command | Port |
|------|---------|------|
| HTTP (no encryption) | `python server.py http` | 5000 |
| HTTPS (TLS encryption) | `python server.py https` | 5000 |
| Both (side‑by‑side) | `python server.py both` | HTTP 5001, HTTPS 5000 |

- Without any argument, the script will prompt you for the mode.

### 4. Access from a client
- **HTTP:** `http://<server-ip>:5000`
- **HTTPS:** `https://<server-ip>:5000` (accept the self‑signed warning)

### 5. Interception demo (Wireshark)
- Filter by `ip.addr == <server-ip> && tcp.port == 5000` (or 5001).
- Send a message from the browser.
- **HTTP** – the message appears as plaintext in the packet.
- **HTTPS** – the payload is encrypted (ciphertext).

---

## Project Structure
```
.
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── index.html
├── ssl/                  (create this folder for .crt and .key)
├── server.py
├── requirements.txt
├── README.md
└── .gitignore
```