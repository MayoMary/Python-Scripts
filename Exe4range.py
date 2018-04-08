print ("program1 started")
good = 0
a = 1
b = 1
# Limit is the maximum number that the answer can be
limit = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
limit = limit + 1

for a in range(1, limit,1):
    if good == 10:
        print(a - 1, " is the answer")
        print ("program ended")
        quit()
    
good = 0
    for b in range(1, 10,1):
        if a % b ==0:
        good = good + 1

  
print ("program ended")

