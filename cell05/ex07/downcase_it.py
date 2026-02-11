#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print(sys.argv[1].lower())
elif len(sys.argv)<= 1:
    print('none')
    

    


#./downcase_it.py  | cat -e
#./downcase_it.py "INITIATION" | cat -e
