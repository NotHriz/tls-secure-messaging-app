import sys
from app import create_app
import ssl

app = create_app()

def run_http():
    print("Starting in HTTP mode (no encryption).")
    app.run(host='0.0.0.0', port=5000, debug=True)

def run_https():
    print("Starting in HTTPS mode (TLS encrypted).")
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain('ssl/server.crt', 'ssl/server.key')
    app.run(host='0.0.0.0', port=5000, ssl_context=ssl_context, debug=True)

def run_both():
    """
    Run both HTTP (port 5001) and HTTPS (port 5000).
    """
    from threading import Thread

    def http_thread():
        app.run(host='0.0.0.0', port=5001, debug=False, use_reloader=False)

    def https_thread():
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain('ssl/server.crt', 'ssl/server.key')
        app.run(host='0.0.0.0', port=5000, ssl_context=ssl_context, debug=False, use_reloader=False)

    t1 = Thread(target=http_thread, daemon=True)
    t2 = Thread(target=https_thread, daemon=True)
    t1.start()
    t2.start()
    print("Both HTTP (port 5001) and HTTPS (port 5000) are running.")
    # Keep main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Shutting down.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
    else:
        # Interactive prompt (optional)
        mode = input("Select mode: http / https / both: ").strip().lower()
    
    if mode == 'http':
        run_http()
    elif mode == 'https':
        run_https()
    elif mode == 'both':
        run_both()
    else:
        print("Unknown mode. Use: python server.py [http|https|both]")
