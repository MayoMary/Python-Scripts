# Mary McHale, 4th March 2018
# FizzBuzz script https://en.wikipedia.org/wiki/Fizz_buzz
# Topic 3 work

i = 1

while i <= 30:
    if (i % 3 == 0) and (i % 5==0):
        print ("Fizzbuz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5==0:
        print ("Buzz")
    else:
        print(i)
    i = i + 1
    

    