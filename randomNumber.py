#!/usr/bin/python
import random

print "Lucky Numbers! 10 numbers will be generated."
print "If one of them is a 'number that you input', you lose!"
inputNumber = input("Input some number: ")
count = 0
while count < 10:
    num = random.randint(1, 11)
    print num
    if num == inputNumber:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"
