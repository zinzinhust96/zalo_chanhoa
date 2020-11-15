import pandas as pd
import numpy as np
from tqdm import tqdm, trange
import torch
from torch.optim import Adam
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from torch.nn.utils.rnn import pad_sequence
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
# from pytorch_pretrained_bert import BertTokenizer, BertConfig
# from pytorch_pretrained_bert import BertForTokenClassification, BertAdam
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('vinai/phobert-base', do_lower_case=True)
print('tokenizer: ', tokenizer)

sentences = ['Tuy vậy, 1 phút sau, Chelsea đã cụ thể hóa sức ép liên tục bằng bàn thắng']

tokenized_texts = [tokenizer.tokenize(sent) for sent in sentences]

print(tokenized_texts)