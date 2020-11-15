#Factoring solution using Fundamental Theorem of Arithmetic

num = 600851475143
new = num
LargestFact = 0
counter = 2

while (counter^2 <= new):
    if new%counter == 0:
        new = new/counter
        LargestFact = counter
    else:
        if counter == 2:
            counter = 3
        else:
            counter += 2
if new > LargestFact:
    LargestFact = new
    
print("The greated prime factor of " + str(num) + " is: " + str(int(LargestFact))) # Added int() to remove trailing ".0"