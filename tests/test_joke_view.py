from joker.views.jokes import random_joke

def test_joke_view(app_request):
  res = random_joke(app_request)
  assert app_request.response.status_int == 200
  assert 'joke' in res
  assert 'answer' in res