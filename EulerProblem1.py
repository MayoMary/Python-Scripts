# Mary McHale, 4th March 2018
# Project Euler Problem 1
# Week No new topic 
# https://www.microsoftstream.com/video/a08d3239-5866-4671-902f-5d352f9135a2

sum = 0
i = 1

while i < 1000:
    if i % 3 ==0:
        sum = sum + i
    elif i % 5 == 0:
        sum = sum + i
    i = i + 1    
print("Sum of multiples of 3 and 5 less than 1,000:",sum)
  