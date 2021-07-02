from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from backend.services.tweet_sentiment.api.decorators.request_logger import log_request


class Server:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if not Server.__instance:
            Server()
        return Server.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Server.__instance:
            raise Exception("This class is a singleton!")
        else:
            Server.__instance = self

        self.app = Flask(__name__)
        self.api = Api(self.app)

        @self.app.route("/", methods=["GET"])
        def render(path=None):
            return "Tweet Sentiment Analysis Root Page"

        # TODO: Allow restricted origins
        cors = CORS(self.app, resources={r"/*": {"origins": "*"}})
        # self.app.before_request(connect_db)
        self.app.before_request(log_request)
        # self.app.after_request(disconnect_db)

    def verify_access_key_validation(self, access_key):
        is_exist = False
        is_expired = True
        role = None
        access_keys = self.app.config['ACCESS_KEYS']
        if access_key in access_keys:
            is_exist = True
            is_expired = access_keys[access_key].is_expired()
            role = access_keys[access_key].get_role()

        return is_exist, is_expired, role

    def run(self):
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        # self.app.register_error_handler(Exception, global_handle_error)
        # self.app.register_error_handler(DoesNotExist, does_not_exist_handle_error)
        # self.app.run(port=8080, use_reloader=False)
        self.app.run(host='localhost', port=8080, use_reloader=False)


server = Server.getInstance()
# print(server)
