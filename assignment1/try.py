#coding=utf-8
import json, re,sys
#import oauth2 as oauth
import urllib2 as urllib

fi = open(sys.argv[1]) 
tweet={}
for line in fi:
	raw = json.loads(line)
        if 'entities' in raw.keys():
	     if raw['entities']['hashtags'] is not None:
	        hnames= raw['entities']['hashtags']
		for single in hnames:
 		     htag=single[u'text']
		     if htag.lower() in tweet.keys():
 				tweet[htag.lower()]+=1
		     else:
				tweet[htag.lower()]=1
        if u'user' in raw.keys():
        	raw_place= raw[u'user']['location']
                conts = re.sub(r'\W+',' ',raw_place.encode('utf-8')).split()
	        for cont in conts:
                  




