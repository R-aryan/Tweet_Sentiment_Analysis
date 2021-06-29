import torch
from injector import inject
from transformers import AlbertTokenizer

from backend.services.tweet_sentiment.settings import Settings


class Preprocess:
    @inject
    def __init__(self, settings: Settings):
        self.settings = settings
        self.max_len = self.settings.MAX_LEN
        self.tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2', do_lower_case=True)

    def preprocess_data(self, data):
        inputs = self.tokenizer.encode_plus(
            data,
            add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
            max_length=self.max_len,  # Pad & truncate all sentences. Just in case there are some longer tes
            pad_to_max_length=True,
            return_attention_mask=True,  # Construct attn. masks
            return_tensors='pt',  # Return pytorch tensors.
            truncation=True
        )

        input_ids = inputs["input_ids"]
        attention_mask = inputs["attention_mask"]

        # Convert the lists into tensors.
        input_ids = torch.cat(input_ids, dim=0)
        attention_mask = torch.cat(attention_mask, dim=0)

        return input_ids, attention_mask
