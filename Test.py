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
import json

def insertTimeCollection(client):
    dbh = client["local"]
    collection = dbh["time"]
    
    for i in range (0,100):
        rawTime = time.time()
        timeStamp = datetime.datetime.fromtimestamp(rawTime).strftime('%Y-%m-%d_%H%M%S')
        collection.insert_one({"timeStamp" : rawTime, "hrTimeStamp": timeStamp})
        time.sleep(0.01)
        
    print "Successfully inserted documents"
    
def insertUser(client):
    dbh = client["test"]
    collection = dbh["user"]
    ret = collection.find_one({'userName': 'evina'})
    if ret == None:
        collection.insert({'userName': 'evina',
                           'password': '',
                           'sessions': [1]})
    
def main(client):
    #insertTimeCollection()
    #insertUser(client)
    pass

def shapeData(data):
    pass
    
if __name__ == "__main__":
    try:
        client = MongoClient(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    #main(client)
    data = '{"tobiiEyeTracker":{"timeStamp":"30.12.2015 14:06:20.2412","leftPos":{"x":"-0,228793755914194","y":"11,5027813555582","z":"60,912982163767"},"rightPos":{"x":"5,89524352818696","y":"11,2245013358383","z":"61,0730322352786"},"leftGaze":{"x":"3,15812377150551","y":"17,3247499470179","z":"4,61986983600664"},"rightGaze":{"x":"-2,49937069615642","y":"17,3932511520527","z":"4,64480229580618"},"leftPupilDiameter":"2,645874","rightPupilDiameter":"2,622345"}}'
    sensorMessage=[]
    sensorMessage.append(json.loads(data))
    #print sensorMessage
    dbh = client["local"]
    collection = dbh["sensor"]
    dataDict = {}
    dataDict["timeStamp"] = "30.12.2015 14:06:20.2412"
    dataDict["leftPos"] = {"x":"-0,228793755914194","y":"11,5027813555582","z":"60,912982163767"}
    
    data = data.replace('{"tobiiEyeTracker":', '')
    data = data[:-1]
    print data
    collection.insert_one(json.loads(data))
    #print double("-0,228793755914194")
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

