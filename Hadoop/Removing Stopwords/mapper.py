#!/usr/bin/python
stopwords = open("stopword.txt",'r').read().split()
import sys
s=""
for line in sys.stdin:	
        line = line.strip()
        words =line.split()   
        for i in words:
        	if i  not in stopwords:
        		s=s+i+" "
        	
        s=s+". "
        
print(s)
        
