from flask import request

from backend.services.tweet_sentiment.api.controllers.controller import Controller
from backend.services.tweet_sentiment.application.ai.operations.prediction import Prediction


class ParamsController(Controller):
    def __init__(self, prediction: Prediction):
        self.prediction = prediction

    def post(self):
        try:
            req_json = request.get_json()
            response = self.prediction.run_prediction(req_json['data'])
            result = {
                'sentence': req_json['data'],
                'sentiment': response
            }
            print("Request Processed Successfully..!!")
            return self.response_ok(result)

        except BaseException as ex:
            print("Following error Occurred----", str(ex))
            return self.response_error(str(ex))
