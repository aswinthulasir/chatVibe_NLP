import pandas as pd
import re

def preprocess(filename,personname ,chat_startdate,chat_enddate):
    #Converting the date to datetime format
    #chat_startdate = pd.to_datetime(chat_startdate)
    #chat_enddate = pd.to_datetime(chat_enddate)
    print(chat_startdate , chat_enddate)
    personname = personname.replace(" ", "")
    personname = personname.lower()

    #Loading the text file into a pandas DataFrame
    df=pd.read_csv(filename,header=None,on_bad_lines='warn',encoding='utf-8',delimiter='\t')
    df.columns = ['input']

    #lists
    Text = []
    Dates = []
    Name = []
    encryption_pattern = r"Messages and calls are end-to-end"
    df = df.drop(df[df['input'].str.contains(encryption_pattern)].index)
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:am|pm)\s-\s'
    impuretext = []
    impuredate = []
    for data in df['input']:
        messages=re.split(pattern, data)[1:]
        dates = re.findall(pattern, data)
        impuredate.append(dates)
        impuretext.append(messages)

    df['Date'] = pd.DataFrame(impuredate)
    df['Text'] = pd.DataFrame(impuretext)
    df =df.dropna()
   # df['Name'] = pd.DataFrame(Name)
    for data in df['Text']:
       nametext = re.split('([\w\W]+?):\s', data) 
       Name.append(nametext[1:2])
       Text.append(nametext[2:])
    df['Name'] = pd.DataFrame(Name)  
    df['Text'] = pd.DataFrame(Text)
    for data in df['Date']:
        date = re.findall('\d{1,2}/\d{1,2}/\d{2,4}', data)
        Dates.append(date)
    df['Date'] = pd.DataFrame(Dates)
    df.dropna()
    #df['Date'] = pd.to_datetime(df['Date'])
    
    #Replacing the chat words with the actual words
    df['Text'] = df['Text'].str.replace('<Media omitted>','MediaShared')
    df['Text'] = df['Text'].str.replace('this message was deleted','DeletedMsg') 

    df['Name'] = df['Name'].str.replace(" ","")
    df['Name'] = df['Name'].str.lower()
    #Dropping the rows with missing values
    df =df.dropna()
    df.drop('input',axis=1,inplace=True)

    #Filtering the data range based on the 'Date' column 
    if chat_startdate != None and chat_enddate != None:
      df = df[ (df['Date'] >= chat_startdate) & (df['Date'] <= chat_enddate)]
    #Filtering the data based on the 'Name' column
    df =df[df['Name'] == personname]
    #print(df)
    #df.to_csv('data/textdata/Abhi_Niyamasabha.csv')
    return df
#file = 'data/textdata/Abhi_Niyamasabha.txt'
#Name = 'Abhi Niyamasabha'
#preprocess(file,Name,'07/02/24','20/03/24') 
#print(df.head())