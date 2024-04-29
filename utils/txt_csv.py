
import pandas as pd
filename="data/ipdata/chat.txt"
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
print(df)
df['Text'] = df['Text'].str.replace('<media omitted>','MediaShared')
df['Text'] = df['Text'].str.replace('this message was deleted','DeletedMsg')    
df =df.dropna()
print(df)
df.to_csv("data/opdata/chat.csv",index=True)
