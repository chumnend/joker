from pyramid.view import view_config
from joker.logic.jokes import get_random_joke

@view_config(route_name='random_joke', renderer='json')
def random_joke(request):
  (joke, answer) = get_random_joke()

  return {
    'joke': joke,
    'answer': answer,
  }
