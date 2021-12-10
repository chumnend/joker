from pyramid.view import view_config
from joker.logic.jokes import get_random_joke, get_all_jokes


@view_config(route_name="random_joke", renderer="json")
def random_joke(request):
    (joke, answer) = get_random_joke()

    return {
        "joke": joke,
        "answer": answer,
    }


@view_config(route_name="get_jokes", renderer="json")
def get_jokes(request):
    jokes = get_all_jokes()

    return {"jokes": jokes}
