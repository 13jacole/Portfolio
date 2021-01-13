#Let's try brute force

import math

sumsquare = 0
squaresum = 0

for x in range(1, 101):
    sumsquare += (x**2)
    squaresum += x
    
squaresum = squaresum**2

print("the difference between the sum of the squares and the square of the sums of the first 100 natural numbers is: " + str(squaresum - sumsquare))

##PROBLEM PRESENTS THE QUESTION BACKWARDS -- It wants square of the sum - sum of the square