#coding=utf-8
import json, re,sys
#import oauth2 as oauth
import urllib2 as urllib
from collections import Counter 
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
state2=[]
for k,v in states.items(): state2.append(str(k)+':'+str(v).upper())
scores = {} # initialize an empty dictionary
for line in open(sys.argv[1]):
       term, score  = line.split("\t")  # The file is tab-delimited.
       scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair

tweet={}
happy={}
fi = open(sys.argv[2]) 

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
        if  raw.has_key(u'user'):
        	raw_place= raw[u'user']['location']

                conts = re.sub(r'\W+',' ',raw_place.encode('utf-8')).split()
                count_tweet=0
		#print conts
	        for cont in conts:
                    for i in range(len(state2)):
		         if re.search(cont.upper(),state2[i]):
			     count_tweet+=1
                             sname=state2[i].split(':')[0]
 		             if happy.get(sname): 
			       happy[sname]+=twit_score
			     else: happy[sname] =twit_score
top = Counter(happy).most_common()[0]
print top[0],top[1]                  
#for k,v in happy.items(): print k,v
		  



