from flask_injector import FlaskInjector

from services.tweet_sentiment.api.server import server
from services.tweet_sentiment.api.controllers.params_controller import ParamsController
from services.tweet_sentiment.application.configuration import Configuration

api_name = "/tweet_sentiment/api/v1/"

server.api.add_resource(ParamsController, api_name + 'inference', methods=["POST"])

flask_inject = FlaskInjector(app=server.app, modules=[Configuration])

# print('done..!!')