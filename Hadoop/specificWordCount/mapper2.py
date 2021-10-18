#!/usr/bin/python
import sys
a=sys.stdin.readline()
a=str(a.strip())
for line in sys.stdin:	
        line = line.strip()
        words =line.split()        
	for word in words:
		if(word==a):
                	print '%s\t%s' %(word,1)
