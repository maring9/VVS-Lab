import requests
from webserver2 import WebServer
from pytest_httpserver import HTTPServer

host_name = "localhost"
server_port = 8080


class TestWebserver2:
    def test_page2(self):
        web_server = HTTPServer((host_name, server_port), WebServer)
        web_server.expect_request('/page')
        expectation = {'Page 2 ': 'Such Wow, Much Amaze',
                       'Status': 200}
        assert requests.get(web_server.url_for('/page')).json() == expectation

    def test_response(self):
        web_server = HTTPServer((host_name, server_port), WebServer)
        web_server.expect_request('/')
        assert requests.get(web_server.url_for('/')).status_code == 200
