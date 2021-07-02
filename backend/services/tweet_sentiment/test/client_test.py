from services.tweet_sentiment.application.ai.operations.prediction import Prediction
from services.tweet_sentiment.application.ai.operations.preprocess import Preprocess
from services.tweet_sentiment.settings import Settings

t1 = "I am feeling very bad  today , it was a bad day ."

p = Prediction(preprocess=Preprocess(Settings))
print(p.run_prediction(t1))
