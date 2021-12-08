from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='hello')
def hello_world(request):
    name = request.params.get('name', '')

    if name == '':
        body = 'Hello World'
    else:
        body = f'Hello, {name}!'

    return Response(
        content_type="text/plain",
        body=body
    )