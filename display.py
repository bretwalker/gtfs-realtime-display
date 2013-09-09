#! /usr/bin/python

import sys
import urllib2

from lib import gtfs_realtime_pb2

def Display(feed_message):
    print feed_message
    
feed_message = gtfs_realtime_pb2.FeedMessage()
    
response = urllib2.urlopen(sys.argv[1])
feed_message.ParseFromString(response.read())

Display(feed_message)