#!/usr/bin/env python3
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
mult = n1*n2
sign = 'positive' if mult > 0 else 'negative' if mult < 0 else 'positive and negative'
print(f"{n1} x {n2} = {mult} \n The result is {sign}")
