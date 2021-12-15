def includeme(config):
    config.add_route("random", "/v1/random", request_method="GET")
    config.add_route("jokes", "/v1/jokes", request_method="GET")
