#! /usr/bin/python

import argparse
import sys
import urllib2

from lib import gtfs_realtime_pb2

def Display(feed_message):
    print feed_message

parser = argparse.ArgumentParser(description='Read a GTFS-realtime Protocol Buffer file.')
parser.add_argument("-f", "--file", dest="file",
                  help="file to read", metavar="FILE")
parser.add_argument("-u", "--url", dest="url",
                  help="URL to read")

args = vars(parser.parse_args())

if args['file'] is None and args['url'] is None:
    raise ValueError('File or URL required.')

feed_message = gtfs_realtime_pb2.FeedMessage()

if args['file']:
    f = open(args['file'], "rb")
    feed_message.ParseFromString(f.read())
    f.close()
else:
    response = urllib2.urlopen(args['url'])
    feed_message.ParseFromString(response.read())    

Display(feed_message)