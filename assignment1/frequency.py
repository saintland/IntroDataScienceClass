#coding=utf-8
import json, re
#import oauth2 as oauth
import urllib2 as urllib
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def main():
    
    tweet_file = open(sys.argv[1])
    #hw()
    
    #lines(tweet_file)
  
    scores = {} # initialize an empty dictionary

    fi = open(sys.argv[1]) 
 
    for myline in fi:
	raw = json.loads(myline)
	if u'text' not in raw.keys():
		continue #print "empty text, ", raw[u'delete']
		
        else: 
	 twit=raw[u'text']
	 conts = re.sub(r'\W+',' ',twit.encode('utf-8')).split()
	 twit_score= int(0)
         for txt in conts:
	     if txt.lower() in scores.keys():
		    scores[txt.lower()]+=1
             else:
	            scores[txt.lower()]=1
        
    
    total_occur=sum(scores.values())
    for k,v in scores.items(): 
       print  k,float(v)/total_occur
       #print 'Total occurs:', total_occur
if __name__ == '__main__':
    main()
