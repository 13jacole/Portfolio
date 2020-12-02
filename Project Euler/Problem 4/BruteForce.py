# Brute Force Method

#Largest possible product of two 3-digit numbers = 999*999 = 998001 --> largest palindrome beneath this is 997799
#Lowest possible product of two 3-digit numbers = 100*100 = 10000 --> smallest palindrome above this is 10001

###METHODOLOGY###
# 1) Starting at 997799, decrement until palindrome.
# 2) Starting at 999, decrement and check multiplicands until both are 3-digit and factors.
#######

#Returns True if input is palindrome
def checkPalindrome(n):
    return str(n) == str(n)[::-1]

def main():
    limit = 997799 # Largest possible palindrome product of two 3-digit numbers
    for i in range(limit, 10000, -1):
        if checkPalindrome(i):
            for j in range(999, 99, -1): # Check all 3-digit numbers in descending order
                ### Since we only want 3-digit numbers:
                ### If i/j > 999, then one of the multiplicands would be 4 digit or more.
                ### Because we are checking in descending order, we should find the higher multiplicand first. So if j^2 is less than i, we have found the lesser multiplicand, and should stop checking numbers.
                if (i/j > 999) or (j*j < i):
                    break
                if i%j == 0:
                    mult1 = j
                    mult2 = i/j
                    print("Palindrome " + str(i) + " is the product of " + str(mult1) + " and " + str(mult2))
                    exit()
                            
main()