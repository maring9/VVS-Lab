from http.server import HTTPServer, BaseHTTPRequestHandler
import json
host_name = "localhost"
server_port = 8080


class WebServer(BaseHTTPRequestHandler):
    def _set_headers(self, code):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        response = {}
        if self.path == '/':
            self._set_headers(200)
            response = {'Software Verification and Validation': 'Welcome',
                        'Status': 200}
        elif self.path == '/page':
            self._set_headers(200)
            response = {'Page 2 ': 'Such Wow, Much Amaze',
                        'Status': 200}
        else:
            self._set_headers(503)
            response = {'Service is unavailable': 503}
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), WebServer)
    print(f'Started server http://{host_name}:{server_port}')
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
    web_server.server_close()
    print('Server stopped')
