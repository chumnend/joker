from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='hello')
def hello_world(request):
    return Response('Hello World')