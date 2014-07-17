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
   # hw()
    #lines(sent_file)
    #lines(tweet_file)
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
       term, score  = line.split("\t")  # The file is tab-delimited.
       scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair

    fi = open(sys.argv[2]) 
    tweet={}
    word={}
    for line in fi:
	raw = json.loads(line)
	if u'text' not in raw.keys():
		continue #print "empty text, ", raw[u'delete']
		
        else: 
	 twit=raw[u'text']
	 conts = re.sub(r'\W+',' ',twit.encode('utf-8')).split()
	 twit_score= int(0)
         for txt in conts:
	     if txt.lower() in scores.keys():
		    #print "%s has no existing score, add as 0"%txt
		    #scores[txt.lower()]=0
	            twit_score += scores[txt.lower()]
         tweet[twit]=twit_score
	 
	 for txt in conts:
	     if txt.lower()  not in scores.keys(): #assign mean score 
			word[txt.lower()]= tweet[twit]/len(conts)
    for k,v in word.items(): 
       print  k,v

if __name__ == '__main__':
    main()
