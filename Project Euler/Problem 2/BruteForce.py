
#Calculates and returns next number in Fib sequence
def NextFib(p1, p2):
    return p1 + p2

#Determines if a number n is even
def isEven(n):
    if n%2==0:
        return True
    else:
        return False
        
def main():
    arr = [1, 1]
    sum = 0
    #Brute Force get fib array
    while arr[-1] < 4000000:
        arr.append(NextFib(arr[-1], arr[-2]))
    #remove last item, which is equal to or greater than 4 mil
    arr.pop()
    
    for x in arr:
        if isEven(x):
            sum = sum + x
    
    print("The sum of all even numbered Fib Numbers below 4 mil: " + str(sum))
    
main()