import torch
import torch.nn.functional as F
from pytorch_pretrained_bert import BertTokenizer
from bertModel import BertClassification

labels = {0: 'neutral', 1: 'positive', 2: 'negative'}
num_labels = len(labels)
vocab = "finance-uncased"
vocab_path = 'analyst_tone/vocab'
pretrained_weights_path = "analyst_tone/pretrained_weights"  # this is pre-trained FinBERT weights
fine_tuned_weight_path = "analyst_tone/fine_tuned.pth"  # this is fine-tuned FinBERT weights
max_seq_length = 512
device = 'cuda:1'

model = BertClassification(weight_path=pretrained_weights_path, num_labels=num_labels, vocab=vocab)
