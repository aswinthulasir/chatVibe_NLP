# import pickle
# def emotionlabel(df):
    
#     # Load the model from the file
#     with open('chatvibe/pipe.pickle', 'rb') as f:
#         loaded_model = pickle.load(f)
#     # Use the loaded model for prediction
#     # for item in df['Text_preprocess']:
#     #     df['prediction'] = loaded_model.predict([item])
    
#     # emotions = df['prediction'].unique()
#     # # Count emotion occurrences
#     # emotion_counts = {}
#     # for emotion in emotions:
#     #   emotion_counts[emotion] = 0
#     #   for row in df['prediction']:
#     #     if emotion in row:
#     #       emotion_counts[emotion] += 1
#     text = "I am happy"
#     prediction = loaded_model.predict([text])
#     print(prediction)

#     #return emotion_counts
import pickle
import pandas as pd
df = pd.read_csv('data/dataset/new.csv')
def emotionlabel(df):
    #Load the model from the file
    emotions = []
    with open('data/trainedmodels/pipe.pickle', 'rb') as f:
        loaded_model = pickle.load(f)
    for row in df['text']:
        emotions.append(loaded_model.predict([row]))
    uni = list(emotions)
    print(uni)
    # df['prediction'] = emotions
    # unique = df['prediction'].
    # # Count emotion occurrences
    # emotion_counts = {}
    # for emotion in unique:
    #   emotion_counts[emotion] = 0
    #   for row in df['prediction']:
    #     if emotion in row:
    #       emotion_counts[emotion] += 1

    # print(emotion_counts)
    # Use the loaded model for prediction
    # new_review = "feeling sick."
    # prediction = loaded_model.predict([new_review])
    #return prediction

emotionlabel(df)
