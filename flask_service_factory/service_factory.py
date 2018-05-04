from flask import g
from werkzeug.local import LocalProxy


class InvalidServiceError(Exception):
    pass


class ServiceFactory(object):
    @staticmethod
    def get_service_factory():
        return g.service_factory

    @classmethod
    def create_proxy_service(cls, service_name):
        def load_service():
            service_factory = cls.get_service_factory()
            return service_factory.get_service(service_name)
        return LocalProxy(load_service)

    def __init__(self):
        self.registry = {}

    def register_service(self, service_name, service_builder):
        self.registry[service_name] = service_builder

    def get_service(self, service_name):
        if service_name not in self.registry:
            raise InvalidServiceError(service_name)
        if not hasattr(g, service_name):
            setattr(g, service_name, self.registry[service_name](self))
        return getattr(g, service_name)
