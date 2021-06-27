from services.tweet_sentiment.api.server import server

app = server.app

if __name__ == "__main__":
    server.run()