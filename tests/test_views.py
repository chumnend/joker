from joker.views.jokes import random_joke, get_jokes

def test_random_joke_view(app_request):
  res = random_joke(app_request)
  assert app_request.response.status_int == 200
  assert 'joke' in res
  assert 'answer' in res

def test_list_jokes_view(app_request):
  res = get_jokes(app_request)
  assert app_request.response.status_int == 200
  assert 'jokes' in res