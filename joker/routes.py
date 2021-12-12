def includeme(config):
    config.add_route("random_joke", "/v1/random", request_method="GET")
    config.add_route("get_jokes", "/v1/jokes", request_method="GET")
