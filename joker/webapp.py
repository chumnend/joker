from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def list_jokes(request):
  return Response('List of jokes\n')

def random_joke(request):
    return Response('Knock Knock\n')

if __name__ == '__main__':
  config = Configurator()

  config.add_route('jokes', '/jokes')
  config.add_route('joke', '/joke')

  config.add_view(list_jokes, route_name='jokes')
  config.add_view(random_joke, route_name='joke')

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 8000, app)
  server.serve_forever()
