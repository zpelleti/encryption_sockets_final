
# socket = endpoints that receive the data
## Server side: 
# 

#server.py file
import socket
import pymongo
import random
import json
from pymongo import MongoClient
from cryptography.fernet import Fernet


dbconnection = pymongo.MongoClient("mongodb+srv://project3560:weekend@cluster0.zqsmp.mongodb.net/ecryptdecrypt?retryWrites=true&w=majority")
db = dbconnection["encryptdecrypt"]
dbcollection = db["keycontainer"]

def main():
    
    key = Fernet.generate_key()

# open file to encrypt:
    with open('CARS.json', 'rb') as f:
        data = f.read()
# create Fernet object and encrypt the file with the generated key
    fernet = Fernet(key)
    encryptedFile = fernet.encrypt(data)
    print(encryptedFile)
    print(' \n')
#create a random number
    ranNum = random.random()
    decodedkey = key.decode()    # send decoded to mongo
    print(type(key))
    print(' \n')
# parse ranNum from float to string:
    ranNum = str(ranNum)
    
# send the key + randnum to mongo
    post = {"key":decodedkey,"ranNum":ranNum}
    dbcollection.insert_one(post)
    
    

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '172.31.32.126' # private ip4 cloud9
    port = 55555
    s.bind((host, port))  
    s.listen(5) 
# convert f key to str: 
  #  ranNumString = str(ranNum)
    print(ranNum)

    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established")
#=========================================================
        clientsocket.send(bytes(encryptedFile))
        clientsocket.send(bytes(ranNum.encode())) ## .encode()))# file to be sent  
        clientsocket.close()


# sendDoc(encryptedFile)
if __name__ == '__main__':
    main()
    



