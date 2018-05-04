from flask import Flask


def create_app(service_factory_builder, name=__name__):
    app = Flask(name)
    _service_factory = service_factory_builder(app)

    class ContextGlobals(Flask.app_ctx_globals_class):
        service_factory = _service_factory

    app.app_ctx_globals_class = ContextGlobals
    return app
