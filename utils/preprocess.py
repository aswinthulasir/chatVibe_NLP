import pandas as pd
from bs4 import BeautifulSoup
import re
import string
from nltk.corpus import stopwords
import emoji
from nltk.stem import PorterStemmer
import nltk
from nltk.stem import WordNetLemmatizer
# Download necessary resources (one-time setup)
nltk.download('wordnet')
#import asyncio

csv_file = 'data/dataset/text.csv'

# Define a dictionary of chat word mappings
chat_words = {
    "AFAIK": "As Far As I Know",
    "AFK": "Away From Keyboard",
    "ASAP": "As Soon As Possible",
    "ATK": "At The Keyboard",
    "ATM": "At The Moment",
    "A3": "Anytime, Anywhere, Anyplace",
    "BAK": "Back At Keyboard",
    "BBL": "Be Back Later",
    "BBS": "Be Back Soon",
    "BFN": "Bye For Now",
    "B4N": "Bye For Now",
    "BRB": "Be Right Back",
    "BRT": "Be Right There",
    "BTW": "By The Way",
    "B4": "Before",
    "B4N": "Bye For Now",
    "CU": "See You",
    "CUL8R": "See You Later",
    "CYA": "See You",
    "FAQ": "Frequently Asked Questions",
    "FC": "Fingers Crossed",
    "FWIW": "For What It's Worth",
    "FYI": "For Your Information",
    "GAL": "Get A Life",
    "GG": "Good Game",
    "GN": "Good Night",
    "GMTA": "Great Minds Think Alike",
    "GR8": "Great!",
    "G9": "Genius",
    "IC": "I See",
    "ICQ": "I Seek you (also a chat program)",
    "ILU": "ILU: I Love You",
    "IMHO": "In My Honest/Humble Opinion",
    "IMO": "In My Opinion",
    "IOW": "In Other Words",
    "IRL": "In Real Life",
    "KISS": "Keep It Simple, Stupid",
    "LDR": "Long Distance Relationship",
    "LMAO": "Laugh My A.. Off",
    "LOL": "Laughing Out Loud",
    "LTNS": "Long Time No See",
    "L8R": "Later",
    "MTE": "My Thoughts Exactly",
    "M8": "Mate",
    "NRN": "No Reply Necessary",
    "OIC": "Oh I See",
    "PITA": "Pain In The A..",
    "PRT": "Party",
    "PRW": "Parents Are Watching",
    "QPSA?": "Que Pasa?",
    "ROFL": "Rolling On The Floor Laughing",
    "ROFLOL": "Rolling On The Floor Laughing Out Loud",
    "ROTFLMAO": "Rolling On The Floor Laughing My A.. Off",
    "SK8": "Skate",
    "STATS": "Your sex and age",
    "ASL": "Age, Sex, Location",
    "THX": "Thank You",
    "TTFN": "Ta-Ta For Now!",
    "TTYL": "Talk To You Later",
    "U": "You",
    "U2": "You Too",
    "U4E": "Yours For Ever",
    "WB": "Welcome Back",
    "WTF": "What The F...",
    "WTG": "Way To Go!",
    "WUF": "Where Are You From?",
    "W8": "Wait...",
    "7K": "Sick:-D Laugher",
    "TFW": "That feeling when",
    "MFW": "My face when",
    "MRW": "My reaction when",
    "IFYP": "I feel your pain",
    "TNTL": "Trying not to laugh",
    "JK": "Just kidding",
    "IDC": "I don't care",
    "ILY": "I love you",
    "IMU": "I miss you",
    "ADIH": "Another day in hell",
    "ZZZ": "Sleeping, bored, tired",
    "WYWH": "Wish you were here",
    "TIME": "Tears in my eyes",
    "BAE": "Before anyone else",
    "FIMH": "Forever in my heart",
    "BSAAW": "Big smile and a wink",
    "BWL": "Bursting with laughter",
    "BFF": "Best friends forever",
    "CSL": "Can't stop laughing"
}

def pre(csv_file , chat_words):
    #Opening the csv file
    df = pd.read_csv(csv_file)
    #Converting the text to lowercase
    df['text'] = df['text'].str.lower()
    #Removing the extra whitespaces
    df['text'] = df['text'].str.strip()


    #html tags removal function
    def remove_html_tags(text):
            soup =  BeautifulSoup(text, 'html.parser')
            return soup.get_text()

    # Remove HTML tags from 'Text' column
    df['text'] = df['text'].apply(remove_html_tags)


    # Define a function to remove URLs using regular expressions
    def remove_urls(text):
            return re.sub(r'http\S+|www\S+', '', text)

    # Apply the function to the 'Text' column
    df['text'] = df['text'].apply(remove_urls)



    string.punctuation
    # Define the punctuation characters to remove
    punctuation = string.punctuation
    # Function to remove punctuation from text
    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', punctuation))

    # Apply remove_punctuation function to 'Text' column
    df['text'] = df['text'].apply(remove_punctuation)


    # Function to replace chat words with their full forms
    def replace_chat_words(text):
        words = text.split()
        for i, word in enumerate(words):
            if word.lower() in chat_words:
                words[i] = chat_words[word.lower()]
        return ' '.join(words)


    # Apply replace_chat_words function to 'Text' column
    df['text'] = df['text'].apply(replace_chat_words)




    # Get English stopwords from NLTK
    stop_words = set(stopwords.words('english'))
    # Function to remove stop words from text
    def remove_stopwords(text):
        words = text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return ' '.join(filtered_words)

    # Apply remove_stopwords function to 'Text' column
    df['text'] = df['text'].apply(remove_stopwords)

    # Function to remove emojis from text
    def remove_emojis(text):
        return emoji.demojize(text)
    # Apply remove_emojis function to 'Text' column
    df['text'] = df['text'].apply(remove_emojis)

    # Initialize the Porter Stemmer
    porter_stemmer = PorterStemmer()
    # Apply stemming
    df['Text_preprocess'] = df['text'].apply(lambda x: ' '.join([porter_stemmer.stem(word) for word in x.split()]))
    # Initialize the WordNet Lemmatizer
    lemmatizer = WordNetLemmatizer()
    #Apply lemmatisation
    df['Text_preprocess'] = df['Text_preprocess'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in x.split()]))

    return df

data = pre(csv_file, chat_words)
print(data.head())