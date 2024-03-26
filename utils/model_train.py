# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import re
import string
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
import emoji
nltk.download('punkt')
from keras.layers import TextVectorization
from keras.preprocessing.sequence import pad_sequences
nltk.download('wordnet')
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import *
from keras.layers import GRU, Dense, Embedding, Flatten, Dropout
from keras.activations import softmax
from sklearn.model_selection import train_test_split
# ignore warnings   
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('./Data/text.csv')
df.head()
