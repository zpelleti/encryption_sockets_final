import socket
import pymongo
from pymongo import MongoClient
import json
from cryptography.fernet import Fernet
import random
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('23.20.224.56', 55555))    # CHANGE public ip4 cloud9(server) 

msg = s.recv(100000)
print(msg.decode("utf-8"))
ranNumString = s.recv(5000)
print(" ")
print(ranNumString.decode("utf-8"))
s.close()

ranNum = ranNumString.decode("utf-8")
print(type(ranNum))

dbconnection = pymongo.MongoClient("mongodb+srv://project3560:williammario@cluster0.zqsmp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = dbconnection["myFirstDatabase"]
dbcollection = db["keycontainer"]

result = dbcollection.find_one({"ranNum":ranNum})
keyfromMongo = result["key"].encode()
print(type(result["key"]))

fernet2 = Fernet(keyfromMongo)
decryptedFile = fernet2.decrypt(msg)
print(decryptedFile)


## to connect with Linux env. and receive from server_socket:

# In AWS, open EC2 / got to Instance
# Select Cloud9 instance, go to security
# In security: 'security groups' 
# in 'security groups', 'edit inbound rules'
# Add rule: custom TCP
# Port 55555, Source 'anywhere IPV4'
# 'Apply'
# [only do this setting once]

# Start session: 
# Run main instance (AWS Cloud9, linux)
# Run second instance (EC2, windows client)
# In AWS Cloud9 instance, copy the 'Public IPV4 address'
# in client.py: paste 'Public IPV4 address' in s.connect
# run server socket in Linux, run client socket in windows remote 

