def includeme(config):
    config.add_route("random_joke", "/api/v1/surprise", request_method='GET')
    config.add_route("get_jokes", "/api/v1/jokes", request_method='GET')
