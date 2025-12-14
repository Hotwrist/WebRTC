from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Access-Control-Allow-Headers', '*')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 9000), CORSHandler)
    print("🚀 Internal .local server (port 9000) is running...")
    server.serve_forever()
