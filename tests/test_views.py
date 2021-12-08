from joker.views.hello import hello_world


def test_hello_world_view(app_request):
    info = hello_world(app_request)
    assert app_request.response.status_int == 200
