#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print(sys.argv[1])
elif len(sys.argv)<= 1:
    print('none')
    

    


#./aff_first_param.py | cat -e

#./aff_first_param.py "Code Ninja" "Numerique" "42" | cat -e