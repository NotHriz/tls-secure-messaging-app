# TLS-Secured Messaging App

A **TLS-secured messaging application** built for a cryptography class.  
The system demonstrates how TLS (Transport Layer Security) encrypts messages in transit, making them unreadable even when intercepted by an adversary.

## Purpose

- **Educational**: Show that intercepted network traffic appears as ciphertext when TLS is properly implemented.
- **Local Network Deployment**: Run the app on your local LAN to simulate real‑world communication and interception (e.g., using Wireshark or a man‑in‑the‑middle proxy).

## Tech Stack

- **Backend**: Python (Flask or custom socket server with TLS)
- **Frontend**: HTML + JavaScript (plain, no framework)
- **Security**: Python’s `ssl` module (wrapping sockets with TLS certificates)

## Getting Started

1. **Clone the repository**  
   ```bash
   git clone <repo-url>
   cd tls-secure-messaging-app
   ```

2. **Install dependencies** (Python 3.8+ recommended)  
   ```bash
   pip install -r requirements.txt   # if provided later
   ```

3. **Generate a self‑signed TLS certificate** (for local testing)  
   ```bash
   openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes
   ```

4. **Run the backend server**  
   ```bash
   python server.py
   ```

5. **Open the frontend**  
   - Serve the HTML file (e.g., `python -m http.server 8000`) and open `http://localhost:8000` in a browser.  
   - Or configure the backend to also serve static files.

## Interception Demo

1. Start the app and send a message between two clients.
2. Use **Wireshark** (or a MITM proxy like mitmproxy) to capture traffic on the local network.
3. Observe that the payload in the captured packets is **encrypted** (TLS ciphertext), not plaintext.
4. This proves that the message was protected by TLS before being sent.

## Project Status

This is a **skeleton** for the project. The actual implementation of the server, client, and TLS wrappers will be added next.

---

*For educational purposes only. Do not use in production without proper certificate authorities and security hardening.*
```

---

