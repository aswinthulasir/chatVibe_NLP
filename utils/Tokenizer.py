import pandas as pd
import tensorflow as tf
from keras.layers import TextVectorization
import numpy as np

def CleanText_csv(csv_file):
    """
    This function reads a csv file and cleans the text in the file.
    args:   
    csv_file: path to the csv file
    """
    df = pd.read_csv(csv_file)
    #print(df)
    try:
        df = df.dropna()  # Drop rows with missing values
        vectorizer = TextVectorization(max_tokens=500,standardize="lower_and_strip_punctuation",split="whitespace",output_mode='int',\
                                    output_sequence_length=20)
        vectorizer.adapt(df['Text_preprocess'])  # Fit the vectorizer on the texts
        #df['text_tokenize'] = vectorizer('Text_preprocess')  # Convert texts to sequences of indices
        df['text_tokenize'] = df['Text_preprocess'].apply(lambda text: vectorizer([text]))

        return df
    except Exception as e:
        return e

   # df.to_csv('csv_file', index=False)





# def Tokenize(texts):
#     """
#     This function tokenizes the text.
#     args:   
#     texts: text to be tokenized
#     """
#     vectorizer = TextVectorization(max_tokens=500,standardize="lower_and_strip_punctuation",split="whitespace",output_mode='int',\
#                                    output_sequence_length=20)
#     vectorizer.adapt(texts)  # Fit the vectorizer on the texts
#     #sequences = vectorizer(texts)  # Convert texts to sequences of indices
#     #print(vectorizer(texts).numpy().tolist())
#     return vectorizer(texts).numpy().tolist()

#texts = ["hello i am nandhana","are you ok","Im not well"]
#print(Tokenize(texts))

csvfile = 'data/dataset/preprocessed_text.csv'
#print(CleanText_csv(csvfile))
result =  CleanText_csv(csvfile)
print(result)



