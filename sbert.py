# This file computes firm embedding vectors using Sentence-BERT (sentence-transformers-2.2.0.tar.gz)
# Author: Hye Jin Lee
# Last Updated: 03-08-2023

# Load packages
import os, torch
import numpy as np
from sentence_transformers import SentenceTransformer, models
import pandas as pd

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f'Running on: {device}')


embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

df = pd.read_csv(os.path.join('/home/hyejin/data/','sp500_all.csv'))

#
contents = df.


long_enough = [len(t) > 200 for t in dataset["data"]]
targets = np.array(dataset.target)[long_enough]
news_data = [t.lower() for t in dataset["data"] if len(t) > 200]
