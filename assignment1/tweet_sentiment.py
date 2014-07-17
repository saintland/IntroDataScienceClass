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
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
    scores = {} # initialize an empty dictionary
    for line in open(sys.argv[1]):
       term, score  = line.split("\t")  # The file is tab-delimited.
       scores[term] = int(score)  # Convert the score to an integer.


    fi = open(sys.argv[2]) 
    tweet={}
    for myline in fi:
	raw = json.loads(myline)
	if raw.has_key(u'text'):	
	 twit=raw[u'text']
	 conts = re.sub(r'\W+',' ',twit.encode('utf-8')).split()
	 twit_score= int(0)
         for txt in conts:
	     if scores.has_key(txt.lower()):
		    #print "%s has no existing score, add as 0"%txt
		    #scores[txt.lower()]=0
	           twit_score += scores[txt.lower()]

         tweet[twit]=twit_score
        else: 
         	twit='NoText'
         	twit_score=0
                tweet[twit]=twit_score
	 
    for k,v in tweet.items(): 
       print  v

if __name__ == '__main__':
    main()
