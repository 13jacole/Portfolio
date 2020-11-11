
def ThreeOrFive(n):
    if n%3 == 0 or n%5 == 0:
        return True
    else:
        return False

def main():
    total = 0
    for i in range(3, 1000):
        if ThreeOrFive(i):
            total = total + i
    
    print("The sum of all natural numbers, that are multiples of 3 or 5, below 1000 are: " + str(total))
    
main()