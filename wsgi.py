from wsgiref.simple_server import make_server

class WSGI_Middleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        for string in self.app(environ, start_response):
            if string.find('<body') > 0 and string.find("<div class='top'>Middleware TOP</div>") < 0:
                yield string.encode()
                yield "<div class='top'>Middleware TOP</div> \n".encode()
            elif string.find('</body>') > 0 and string.find("<div class='botton'>Middleware BOTTOM</div>") < 0:
                yield "<div class='botton'>Middleware BOTTOM</div> \n".encode()
                yield string.encode()
            else:
                yield string.encode()

def app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/HTML')])
    return open(environ['PATH_INFO'], 'r')

make_server('127.0.0.1', 8000, WSGI_Middleware(app)).serve_forever()