from backend.common.logging.console_loger import ConsoleLogger
from injector import Module, singleton

from backend.common.logging.logger import Logger
from backend.services.tweet_sentiment.settings import Settings
from backend.services.tweet_sentiment.application.ai.operations.preprocess import Preprocess
from backend.services.tweet_sentiment.application.ai.operations.prediction import Prediction


class Configuration(Module):
    def configure(self, binder):
        binder.bind(Preprocess, to=Preprocess, scope=singleton)
        binder.bind(Prediction, to=Prediction, scope=singleton)
        logger = ConsoleLogger()
        binder.bind(Logger, to=logger, scope=singleton)
