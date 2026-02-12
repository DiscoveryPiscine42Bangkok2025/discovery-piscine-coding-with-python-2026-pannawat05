#!/usr/bin/env python3
import sys

if len(sys.argv)  > 1:
    l = len(sys.argv) 
    print(f'parameters: {l -1}')
    i = 1
    while i < l:
        print(sys.argv[i],':',len(sys.argv[i]))
        i += 1

else:
    print('none')



