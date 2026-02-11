#!/usr/bin/env python3
import sys


if len(sys.argv) == 3:
    substring = sys.argv[1]  
    full_text = sys.argv[2]  
    
    
    result = full_text.count(substring)
    
    print(result)

else:
    print('none')