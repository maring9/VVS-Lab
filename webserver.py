from http.server import HTTPServer, BaseHTTPRequestHandler

host_name = "localhost"
server_port = 8080


class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file = open(self.path[1:]).read()
            self.send_response(200)
        except Exception:
            file = open('notfound.html').read()
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(file, 'utf-8'))


if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), WebServer)
    print(f'Started server http://{host_name}:{server_port}')
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
    web_server.server_close()
    print('Server stopped')
