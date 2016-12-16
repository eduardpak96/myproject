from pyramid.response import Response
from pyramid.config import Configurator
from wsgiref.simple_server import make_server

def index(request):
    return Response("""<p><a href="about/aboutme.html">прямая ссылка</a></p><p><a href="http://127.0.0.1:8000/about/aboutme.html">абсолютная ссылка</a></p>""")
def aboutme(request):
    return Response("""<p><a href="../">прямая ссылка</a></p><p><a href="http://127.0.0.1:8000/">абсолютная ссылка</a></p>""")
if __name__ == '__main__':
    config = Configurator()
    config.add_view(index, route_name='index')
    config.add_route("index",'/')
    config.add_view(aboutme, route_name='aboutme')
    config.add_route('aboutme', 'about/aboutme.html')
    serv = make_server('127.0.0.1', 8000, config.make_wsgi_app())
    serv.serve_forever()