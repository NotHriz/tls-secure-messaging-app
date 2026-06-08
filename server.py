from app import create_app
import ssl

app = create_app()

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('ssl/server.crt', 'ssl/server.key')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=ssl_context, debug=True)