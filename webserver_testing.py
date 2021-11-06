import requests
from webserver import WebServer
from http.server import HTTPServer

host_name = "localhost"
server_port = 8080


class TestWebserver:
    def test_webserver_running(self):
        web_server = HTTPServer((host_name, server_port), WebServer)
        web_server.serve_forever()
        response = requests.get('http://127.0.0.1:8080')
        web_server.server_close()
        assert response.status_code == 200

    def test_notfound(self):
        web_server = HTTPServer((host_name, server_port), WebServer)
        web_server.serve_forever()
        response = requests.get('http://127.0.0.1:8080/random')
        assert response.status_code == 404
