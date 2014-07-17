#coding=utf-8
import json, re,sys
#import oauth2 as oauth
import urllib2 as urllib
from collections import Counter 

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

top10 = Counter(tweet).most_common()[:10]

for my in top10:
    print my[0],my[1]
