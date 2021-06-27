from flask import request
from injector import inject

from common.logging.logger import Logger


@inject
def log_request(logger: Logger):
    logger.info(request.method + ' request received:' + request.url)
