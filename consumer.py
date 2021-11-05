from kafka import KafkaConsumer
from json import loads
import json 
import pandas as pd
from datetime import datetime


data = []

consumer = KafkaConsumer(
    #'Payam2Topic',
     'ChallengeTopic',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     consumer_timeout_ms=1000,
     enable_auto_commit=True,
     value_deserializer=lambda x: loads(x.decode('utf-8')))


dfs = pd.DataFrame()
try:
    for message in consumer:
        # if message.offset >= 1:
        #     break
        print('********')
        single_data = pd.json_normalize(message.value)
        single_data['DateTime'] = datetime.fromtimestamp(single_data['ts'])
        single_data['Date'] = single_data['DateTime'].dt.strftime('%y%m%d')
        
        # single_data['Year'] = single_data['DateTime'].dt.strftime('%y')
        # single_data['Month'] = single_data['DateTime'].dt.strftime('%m')
        # single_data['Day'] = single_data['DateTime'].dt.strftime('%d')
        # single_data['Hour'] = single_data['DateTime'].dt.strftime('%H')
        # single_data['Minute'] = single_data['DateTime'].dt.strftime('%M')
        # single_data['Second'] = single_data['DateTime'].dt.strftime('%S')
        
        dfs = pd.concat([single_data, dfs], sort=True)     
        print(dfs.groupby('Date')['uid'].nunique())
        #print(dfs.get('uid') )
except:
    print('Error occurred')        
    


    
    