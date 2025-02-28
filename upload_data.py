from pymongo.mongo_client import MongoClient
import pandas as pd
import json

url="mongodb+srv://sagar:aR5XzQU7KkA4TYmJ@cluster0.ujykm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#Create new client and connect to server
client=MongoClient(url)

DATABASE_NAME="faultdetection"
COLLECTION_NAME='Waferfault'

df=pd.read_csv("D:\\Desktop\SensorProject\notebook\wafer_23012020_041211 (1).csv")

df.head()

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

type(json_record)

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)