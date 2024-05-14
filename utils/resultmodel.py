
import pickle
#import pandas as pd
import collections
#df = pd.read_csv('data/dataset/text2.csv')
#df =df.dropna()

def emotionlabel(df):
    #Load the model from the file
    with open('data/trainedmodels/accuratemodel.pickle', 'rb') as f:
        loaded_model = pickle.load(f)
    emotions = loaded_model.predict(df['Text_preprocess'])
    count = collections.Counter(emotions)
    #print(count)
    return count

#emotionlabel(df)
