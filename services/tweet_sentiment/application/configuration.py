import logging
from common.logging.console_loger import ConsoleLogger
from injector import Module, singleton

from common.logging.logger import Logger


class Configuration(Module):
    def configure(self, binder):
        logger = ConsoleLogger()
        binder.bind(Logger, to=logger, scope=singleton)
