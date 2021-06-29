from backend.services.tweet_sentiment.api.controllers.controller import Controller


class ParamsController(Controller):
    def __init__(self):
        pass

    def post(self):
        print("Post request Successfully..!!")
