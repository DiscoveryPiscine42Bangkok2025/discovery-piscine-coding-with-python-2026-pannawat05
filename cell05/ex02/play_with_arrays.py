#!/usr/bin/env python3
arr =  [2, 8, 9, 48, 8, 22, -12, 2]
arr2 = [x+2 for x in arr if x > 5]
print("Original array:", arr)
print("new array:", arr2)