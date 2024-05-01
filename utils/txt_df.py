
import pandas as pd
import os
# filename="data/ipdata/chat.txt"
# Name = "Indrajith S"
# chat_startdate = "2023-11-19"
# #chat_starttime = "3:45 pm"
# chat_enddate =  "2024-01-01"
# #chat_endtime =  "12:09 am"

def text_to_df(filename,Name ,chat_startdate,chat_enddate):
    '''
    args: filename (str): path to the text file
    returns: df (pandas DataFrame): dataframe of the text file
    '''
    chat_startdate = pd.to_datetime(chat_startdate)
    chat_enddate = pd.to_datetime(chat_enddate)
    df=pd.read_csv(filename,header=None,on_bad_lines='warn',encoding='utf-8')
    encryption_pattern = r"Messages and calls are end-to-end"
    df = df.drop(df[df[1].str.contains(encryption_pattern)].index)
    df.columns=['Date','Time','Name','Text']
    Message= df["Time"].str.split("-", n = 1, expand = True) 
    df['Date']=df['Date'].str.replace(",","") 
    df['Time']=Message[0]
    df['Text']=Message[1]
    Message1= df["Text"].str.split(":", n = 1, expand = True) 
    df['Text']=Message1[1]
    df['Name']=Message1[0]
    df['Text']=df['Text'].str.lower()
    df['Name']=df['Name'].str.strip()
    df['Text'] = df['Text'].str.replace('<media omitted>','MediaShared')
    df['Text'] = df['Text'].str.replace('this message was deleted','DeletedMsg')    
    df =df.dropna()
    df['Date'] = pd.to_datetime(df['Date'])
    df =df[df['Name'] == Name]
    df = df[ (df['Date'] >= chat_startdate) & (df['Date'] <= chat_enddate)]
    os.remove(filename)
    return df
    #print(df)
    #df.to_csv("data/opdata/chat.csv",index=True)
#print(text_to_df(filename,Name,chat_startdate,chat_enddate))
