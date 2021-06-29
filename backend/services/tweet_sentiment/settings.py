import os
import sys


class Settings:
    root_path = os.getcwd()
    service_path = root_path + "\\backend\\services\\tweet_sentiment\\application\\"
    # model configuration
    MAX_LEN = 150
    MODEL_PATH = service_path + '\\ai\\weights\\albert_weight\\weights_v1\\pytorch_model.bin'
    BATCH_SIZE = 16
    EPOCHS = 4
    SEED_VAL = 42
    SENTIMENT_DICT = {'neutral': 0, 'negative': 1, 'positive': 2}
    NUM_LABELS = 3

