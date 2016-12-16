from jinja2 import Environment, FileSystemLoader
from wsgiref.simple_server import make_server

def app(environ, start_response):
    env = Environment(loader=FileSystemLoader('templates'))
    start_response('200 OK', [('Content-Type', 'text/html')])
    pathTofile = environ['PATH_INFO']
    def templ(w):
        w = pathTofile
        return env.get_template(pathTofile).render(link=w)
    return [templ(pathTofile).encode('utf-8')]

serv = make_server('127.0.0.1', 8000, app)
serv.serve_forever()
