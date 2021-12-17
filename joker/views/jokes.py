from pyramid.view import view_config
from joker.logic import jokes as jokes_logic


@view_config(route_name="random", request_method="GET", renderer="json")
def random(request):
    (joke, answer) = jokes_logic.get_random_joke()

    return {
        "joke": joke,
        "answer": answer,
    }


@view_config(route_name="jokes", request_method="GET", renderer="json")
def jokes(request):
    jokes = jokes_logic.get_all_jokes()

    return {"jokes": jokes}
