from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'localhost'
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    """Класс для обработки запросов"""

    def do_GET(self):
        """Обработка входящих get-запросов"""
        page_content = self.get_html_code('index.html')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(page_content, 'utf-8'))

    @staticmethod
    def get_html_code(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            page_content = file.read()
        return page_content


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Server started http://%s:%s' % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Server stopped')