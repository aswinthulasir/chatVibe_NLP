import pandas as pd
import tensorflow as tf
from keras.layers import TextVectorization
#from keras.preprocessing.sequence import pad_sequences

def CleanText_csv(csv_file):
    # """
    # This function reads a csv file and cleans the text in the file.
    # args:   
    # csv_file: path to the csv file
    # """
    df = pd.read_csv(csv_file)
    df['text_tokenized'] = df['text'].apply(Tokenize)
    return df

   # df.to_csv('csv_file', index=False)





def Tokenize(texts):
    """
    This function tokenizes the text.
    args:   
    texts: text to be tokenized
    """
    vectorizer = TextVectorization(max_tokens=100, output_mode='int')
    vectorizer.adapt(texts)  # Fit the vectorizer on the texts
    sequences = vectorizer(texts)  # Convert texts to sequences of indices
    #print(sequences)
    return sequences

#texts = ["hello i am nandhana","are you ok","Im not well"]
#Tokenize(texts)
#csvfile = r'C:\Users\NANDHANA ESBEE\Desktop\CHATViBE\chatvibe\data\dataset\new.csv'
csvfile = r"C:\Users\NANDHANA ESBEE\Desktop\CHATViBE\chatvibe\data\dataset\text.csv"
result =  CleanText_csv(csvfile)
print(result)



