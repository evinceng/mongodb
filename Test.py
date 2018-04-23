# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 13:58:46 2018

@author: evin

To start a local server open cmd 

cd C:\Program Files\MongoDB\Server\3.6\bin
mongod.exe cd --dbpath "C:\Users\evin\Documents\MongoDB"

then it will start waiting connections
"""
import sys
import time
import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def insertTimeCollection():
    try:
        client = MongoClient(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
        
    dbh = client["local"]
    collection = dbh.time
    
    for i in range (0,100):
        rawTime = time.time()
        timeStamp = datetime.datetime.fromtimestamp(rawTime).strftime('%Y-%m-%d_%H%M%S')
        collection.insert_one({"timeStamp" : rawTime, "hrTimeStamp": timeStamp})
        time.sleep(0.5)
        
    print "Successfully inserted documents"

def main():
    insertTimeCollection()

if __name__ == "__main__":
    main()
    
#from pymongo import MongoClient
#import time
#import datetime
#
#def createTimeCollection():
#    client = MongoClient('localhost', 27017)
#    db = client.local
#    collection = db.time
#    
#    for i in range (0,100):
#        rawTime = time.time()
#        timeStamp = datetime.datetime.fromtimestamp(rawTime).strftime('%Y-%m-%d_%H%M%S')
#        collection.insert_one({"timeStamp" : rawTime, "hrTimeStamp": timeStamp})
#        time.sleep(1)
#        
#createTimeCollection()
      
#def insertDoc():
#    while True:
#    time.sleep(1)
#    data = {
#        'time': datetime.datetime.utcnow(),
#        'oxygen': random.random()
#    }
#
#    # Try for five minutes to recover from a failed primary
#    for i in range(60):
#        try:
#            mabel_db.breaths.insert(data, safe=True)
#            print 'wrote'
#            break # Exit the retry loop
#        except pymongo.errors.AutoReconnect, e:
#            print 'Warning', e
#            time.sleep(5)

