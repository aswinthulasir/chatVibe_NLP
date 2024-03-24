import pandas as pd
import tensorflow as tf
from keras.layers import TextVectorization
from keras.preprocessing.sequence import pad_sequences

def CleanText_csv(csv_file):
    # """
    # This function reads a csv file and cleans the text in the file.
    # args:   
    # csv_file: path to the csv file
    # """
    df = pd.read_csv(csv_file)
    for index, value in df['text']:
        df['text'][index] = Tokenize(value)

    df.to_csv('csv_file', index=False)





def Tokenize(texts):
    """
    This function tokenizes the text.
    args:   
    texts: text to be tokenized
    """
    vectorizer = TextVectorization(max_tokens=100, output_mode='int')
    vectorizer.adapt(texts)  # Fit the vectorizer on the texts
    sequences = vectorizer(texts)  # Convert texts to sequences of indices
    print(sequences)
    return sequences




