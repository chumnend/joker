def includeme(config):
    config.add_route("random_joke", "/v1/surprise")
    config.add_route("get_jokes", "/v1/jokes")
