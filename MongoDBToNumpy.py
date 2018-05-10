# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 10:26:38 2018

@author: evin
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import sys
import pprint
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import re

def insertDocs():
    docs = [
            {"timeStamp":"25.09.2017 18:06:36.7452","leftPos":{"x":"-16,7315728269386","y":"3,89062108428363","z":"56,2198678361344"},"rightPos":{"x":"-10,0026425550767","y":"3,29426110476243","z":"56,0879127434864"},"leftGaze":{"x":"-3,49850843959982","y":"22,1567167927533","z":"6,37821179543316"},"rightGaze":{"x":"-7,89889571217705","y":"21,4349212191887","z":"6,11551553472114"},"leftPupilDiameter":"3,069977","rightPupilDiameter":"2,963455"},
            {"timeStamp":"25.09.2017 18:06:36.7943","leftPos":{"x":"-16,7098222900898","y":"3,90436146663274","z":"56,2242540276036"},"rightPos":{"x":"-9,98631284785558","y":"3,30704196490619","z":"56,0891633566908"},"leftGaze":{"x":"-1,72234459305309","y":"22,4207459567531","z":"6,47430475671185"},"rightGaze":{"x":"-5,62868343709524","y":"22,422401237002","z":"6,47490719311872"},"leftPupilDiameter":"3,102768","rightPupilDiameter":"3,005875"},
            {"timeStamp":"25.09.2017 18:06:36.8864","leftPos":{"x":"-16,9001924206929","y":"3,88461160788982","z":"56,1994065129416"},"rightPos":{"x":"-10,1420321126478","y":"3,34486136857306","z":"56,0834237367933"},"leftGaze":{"x":"-0,363629186618618","y":"24,2620824531458","z":"7,14445601564266"},"rightGaze":{"x":"-4,504263384347","y":"23,2056102294919","z":"6,75995476228995"},"leftPupilDiameter":"3,104858","rightPupilDiameter":"3,024307"},
            {"timeStamp":"25.09.2017 18:06:36.9334","leftPos":{"x":"-16,9407320929185","y":"3,87290156474623","z":"56,2004726303334"},"rightPos":{"x":"-10,1813528995491","y":"3,34311107269234","z":"56,0867164621378"},"leftGaze":{"x":"0,0382847428729292","y":"24,1641581806759","z":"7,10881664467265"},"rightGaze":{"x":"-4,45922413548337","y":"23,5984198978849","z":"6,90291716721133"},"leftPupilDiameter":"3,072189","rightPupilDiameter":"3,016708"}
    ]
    
    collection.insert_many(docs)

def insertJsonDocs():
    docs = [
            '{"tobiiEyeTracker":{"timeStamp":"25.09.2017 18:06:36.7452","leftPos":{"x":"-16,7315728269386","y":"3,89062108428363","z":"56,2198678361344"},"rightPos":{"x":"-10,0026425550767","y":"3,29426110476243","z":"56,0879127434864"},"leftGaze":{"x":"-3,49850843959982","y":"22,1567167927533","z":"6,37821179543316"},"rightGaze":{"x":"-7,89889571217705","y":"21,4349212191887","z":"6,11551553472114"},"leftPupilDiameter":"3,069977","rightPupilDiameter":"2,963455"}}',
            '{"tobiiEyeTracker":{"timeStamp":"25.09.2017 18:06:36.7943","leftPos":{"x":"-16,7098222900898","y":"3,90436146663274","z":"56,2242540276036"},"rightPos":{"x":"-9,98631284785558","y":"3,30704196490619","z":"56,0891633566908"},"leftGaze":{"x":"-1,72234459305309","y":"22,4207459567531","z":"6,47430475671185"},"rightGaze":{"x":"-5,62868343709524","y":"22,422401237002","z":"6,47490719311872"},"leftPupilDiameter":"3,102768","rightPupilDiameter":"3,005875"}}',
            '{"tobiiEyeTracker":{"timeStamp":"25.09.2017 18:06:36.8864","leftPos":{"x":"-16,9001924206929","y":"3,88461160788982","z":"56,1994065129416"},"rightPos":{"x":"-10,1420321126478","y":"3,34486136857306","z":"56,0834237367933"},"leftGaze":{"x":"-0,363629186618618","y":"24,2620824531458","z":"7,14445601564266"},"rightGaze":{"x":"-4,504263384347","y":"23,2056102294919","z":"6,75995476228995"},"leftPupilDiameter":"3,104858","rightPupilDiameter":"3,024307"}}',
            '{"tobiiEyeTracker":{"timeStamp":"25.09.2017 18:06:36.9334","leftPos":{"x":"-16,9407320929185","y":"3,87290156474623","z":"56,2004726303334"},"rightPos":{"x":"-10,1813528995491","y":"3,34311107269234","z":"56,0867164621378"},"leftGaze":{"x":"0,0382847428729292","y":"24,1641581806759","z":"7,10881664467265"},"rightGaze":{"x":"-4,45922413548337","y":"23,5984198978849","z":"6,90291716721133"},"leftPupilDiameter":"3,072189","rightPupilDiameter":"3,016708"}}'
    ]
    
    result = ""
    for doc in docs:
        result = shapeData(doc)
        collection.insert_one(result)

def shapeData(data):
    omitBeginLen = len('{"tobiiEyeTracker":')
    result = data[omitBeginLen:-1]
    
    print result
    print "##################################"
    
    result = re.sub(r'\"(\-??\d+),(\d+)\"', r'\1.\2', result) # "-16,7315728269386" -> -16.7315728269386
    print result
    return result

if __name__ == "__main__":
    try:
        client = MongoClient(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
        
    dbh = client["mediaExposureTry"]
    collection = dbh["eyesRolling"]
    #insertDocs()
    projection = {
            "_id": 0,
            "relativeTime": 1,
            "leftGaze:x": 1,
            "leftGaze:y": 1
            }
    rm = list(collection.find({}, projection))
    
    #pprint.pprint(rm[0])
    relativeTime = [sensor["relativeTime"] for sensor in rm]
    gazeCoordx = [sensor["leftGaze:x"] for sensor in rm]
    gazeCoordy = [sensor["leftGaze:y"] for sensor in rm]
    
    #gazeCoordxnpArray = np.array(gazeCoordx)
    #gazeCoordynpArray = np.array(gazeCoordy)
    
    fig = plt.figure()
    ax = fig.gca() 
    ax.scatter(gazeCoordx, gazeCoordy, c=relativeTime, cmap=cm.seismic)
    ax.legend()
    
    plt.show()
#    plt.clf()
#    fig, ax = plt.subplots()
#    
#    ax.scatter(timeStampsnpArray, leftPupilDiametersnpArray, alpha = 0.5)
#    plt.show()
    
    
    