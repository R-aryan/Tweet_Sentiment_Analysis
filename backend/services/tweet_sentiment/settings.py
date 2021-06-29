import os
import sys


class Settings:
    PROJ_NAME = 'Tweet_Sentiment_Analysis'
    root_path = os.getcwd().split(PROJ_NAME)[0] + "\\" + PROJ_NAME + "\\"
    # print(root_path)
    service_path = root_path + "backend\\services\\tweet_sentiment\\application\\"
    # model configuration
    MAX_LEN = 150
    MODEL_PATH = service_path + "ai\\weights\\albert_weight\\weights_v1\\pytorch_model.bin"
    # print(MODEL_PATH)
    BATCH_SIZE = 16
    EPOCHS = 4
    SEED_VAL = 42
    LABEL_DICT = {'neutral': 0, 'negative': 1, 'positive': 2}
    REVERSE_LABEL_DICT = {0: 'neutral', 1: 'negative', 2: 'positive'}
    NUM_LABELS = 3
