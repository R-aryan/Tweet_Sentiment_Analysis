# Transformers
import torch

from transformers import AlbertTokenizer
from transformers import AlbertForSequenceClassification, AdamW, AlbertConfig
from transformers import get_linear_schedule_with_warmup

from injector import inject

from backend.services.tweet_sentiment.settings import Settings
from backend.services.tweet_sentiment.application.ai.operations.preprocess import Preprocess


class Prediction:
    @inject
    def __init__(self, settings: Settings, preprocess: Preprocess):
        self.settings = settings
        self.preprocess = preprocess
        self.device = self.__check_device()
        # Load the ALBERT tokenizer.
        print('Loading ALBERT tokenizer...')
        self.tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2', do_lower_case=True)
        self.__model = None
        self.__load_model()

    def run(self, data):
        input_ids, attention_mask = self.preprocess.preprocess_data(data)
        self.__predict(input_ids, attention_mask)

    def __check_device(self):
        if torch.cuda.is_available():

            # Tell PyTorch to use the GPU.
            device = torch.device("cuda")

            print('There are %d GPU(s) available.' % torch.cuda.device_count())

            print('We will use the GPU:', torch.cuda.get_device_name(0))

        # If not...
        else:
            print('No GPU available, using the CPU instead.')
            device = torch.device("cpu")

        return device

    def __load_model(self):

        try:
            self.__model = AlbertForSequenceClassification.from_pretrained(
                "albert-large-v2",  # Use the 12-layer BERT model, with an uncased vocab.
                num_labels=self.settings.NUM_LABELS,
                # The number of output labels--2 for binary classification.# You can increase this for multi-class tasks
                output_attentions=False,  # Whether the model returns attentions weights.
                output_hidden_states=False,  # Whether the model returns all hidden-states.
                return_dict=False,
            )

            if self.__model:
                self.__model.load_state_dict(torch.load(self.settings.MODEL_PATH,
                                                        map_location=torch.device(self.device)))

        except BaseException as ex:
            print("Following error occurred while loading the model------", str(ex))

    def __predict(self, input_ids, attention_mask, token_type_ids=None):
        result = self.__model(
            input_ids=input_ids,
            token_type_ids=token_type_ids,
            attention_mask=attention_mask
        )