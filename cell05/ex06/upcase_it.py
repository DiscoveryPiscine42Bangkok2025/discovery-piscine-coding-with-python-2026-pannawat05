#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print(sys.argv[1].upper())
elif len(sys.argv)<= 1:
    print('none')
    

    


#./upcase_it.py  | cat -e
#./upcase_it.py "initiation" | cat -e