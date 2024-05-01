
import pandas as pd
import os

def text_to_df(filename,Name ,chat_startdate,chat_enddate):
    '''
    args: filename (str): path to the uploaded file
          Name (str): Name of the person whose chat is to be analyzed
          chat_startdate (str): start date of the chat
          chat_enddate (str): end date of the chat
    returns: df (pandas DataFrame): dataframe of the text file
    '''
    #Converting the date to datetime format
    chat_startdate = pd.to_datetime(chat_startdate)
    chat_enddate = pd.to_datetime(chat_enddate)

    #Loading the text file into a pandas DataFrame
    df=pd.read_csv(filename,header=None,on_bad_lines='warn',encoding='utf-8')

    #Removing the rows containing the encryption pattern
    encryption_pattern = r"Messages and calls are end-to-end"
    df = df.drop(df[df[1].str.contains(encryption_pattern)].index)

    #Setting the column names
    df.columns=['Date','Time','Name','Text']

    #Fixing every data in proper columns
    Message= df["Time"].str.split("-", n = 1, expand = True) 
    df['Date']=df['Date'].str.replace(",","") 
    df['Time']=Message[0]
    df['Text']=Message[1]
    Message1= df["Text"].str.split(":", n = 1, expand = True) 
    df['Text']=Message1[1]
    df['Name']=Message1[0]
    df['Text']=df['Text'].str.lower()

    #Removing the extra whitespaces from the 'Name' column
    df['Name']=df['Name'].str.strip()

    #Replacing the chat words with the actual words
    df['Text'] = df['Text'].str.replace('<media omitted>','MediaShared')
    df['Text'] = df['Text'].str.replace('this message was deleted','DeletedMsg') 

    #Dropping the rows with missing values   
    df =df.dropna()

    #Converting the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    #Filtering the data based on the 'Name' column
    df =df[df['Name'] == Name]
    #Filtering the data range based on the 'Date' column 
    df = df[ (df['Date'] >= chat_startdate) & (df['Date'] <= chat_enddate)]

    #No files are saed internally so we delete the file after reading it
    os.remove(filename)
    return df

