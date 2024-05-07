# Load chat
from whatstk import WhatsAppChat
import pandas as pd
filepath = 'data/dataset/gobi.txt'
chat = WhatsAppChat.from_source(filepath=filepath)
df = chat.df
df =df.dropna()
#Converting the 'Date' column to datetime format
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df = df.dropna(subset=['date'])
#Removing the extra whitespaces from the 'Name' column
df['username']=df['username'].str.strip()
#Filtering the data based on the 'Name' column
df =df[df['username'] == 'Gobind Team❤️']
print(df)
df.to_csv('data/ipdata/gobi.csv', index=False)
# Chat as Dataframe available in chat.df