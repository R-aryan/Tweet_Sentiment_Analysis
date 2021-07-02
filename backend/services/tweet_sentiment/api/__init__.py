from flask_injector import FlaskInjector
from backend.services.tweet_sentiment.api.server import server
from backend.services.tweet_sentiment.application.configuration import Configuration
from backend.services.tweet_sentiment.api.controllers.params_controller import ParamsController

api_name = '/tweet_sentiment/api/v1/'

server.api.add_resource(ParamsController, api_name + 'predict', methods=["POST"])

flask_injector = FlaskInjector(app=server.app, modules=[Configuration])
