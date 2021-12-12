from pyramid.config import Configurator


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    # settings["pyramid_swagger.schema_file"] = "swagger.yaml"
    with Configurator(settings=settings) as config:
        config.include(".routes")
        # config.include("pyramid_swagger")
        config.scan()
    return config.make_wsgi_app()
