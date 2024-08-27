q=[]
max_retries = 10
import http.client
import json
import time
import schedule
import random
import pandas as pd
def get_data():
    conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

    headers = {
    'x-rapidapi-key': "1b22eeed5dmsh1352cbfdfab7d85p1e9f9djsn5f7f70c83980",
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }

    conn.request("GET", "/query?datatype=json&output_size=compact&interval=1min&function=TIME_SERIES_INTRADAY&symbol=TSLA", headers=headers)
 


    res = conn.getresponse()
    
    
    
        
    
    data = res.read()
    
  
    
    d=json.loads(bytearray(data))
    di=d["Time Series (1min)"]
    formatted_data={}
    a=[]
    b=[]
    for timestamp, details in di.items():
        
        price = details['1. open']
        a.append(timestamp)
        b.append(price)
        
    random_integer = random.randint(1000,9000)
    
    formatted_data["ID"]=random_integer
    formatted_data["timestamp"]=a
    formatted_data["price"]=b
    
    df = pd.DataFrame(formatted_data)
    df_sorted = df.sort_values(by="timestamp", ascending=False)
    data=df_sorted.head(5) 
    data=data.to_dict(orient='records')[0]
     
     
    
    return data
import boto3
 
def send_sqs_message(queue_url,message_body):
     

    sqs = boto3.client('sqs',aws_access_key_id= ,
    aws_secret_access_key= )
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )
    return response

def job():
    global q
    
     
    for attempt in range(max_retries):
        
        try:
            d=get_data()
            q.append(str(d))
            print(q)
             
            break   
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(3)   
            else:
                print("Max retries reached. Code failed.")
    if(len(q)==5):
        for i in q:
            
            send_sqs_message("https://sqs.eu-north-1.amazonaws.com/730335407622/stock_data",i)
        q=[]
schedule.every(1).seconds.do(job)
