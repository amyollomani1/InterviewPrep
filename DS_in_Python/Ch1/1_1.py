import random

def main():
    print(is_multiple(100,20))
    print(is_multiple(5,20))
    print(is_even(5))
    print(is_even(150))
    print(minmax([1,2,3,4,5,6]))
    print(minmax([1,2,10,4,5,6,0]))
    print(minmax2([1,2,10,4,5,6,0]))
    print(sumSquares(4)) # 1 + 4 + 9 + 16
    print(sumSquares2(4)) # 1 + 4 + 9 + 16
    print(sumOddSquares(5)) #1 + 9 + 25
    print([k for k in range(-8,8+1) if k %2 == 0])
    print(choice([1,2,10,4,5,6,0]))



def is_multiple(n,m):
    if n%m == 0:
        return True 
    return False

def is_even(k):
    isEven = True
    for i in range(1,k+1):
        isEven = not isEven
    return isEven
    
def minmax(data):
    min = 10000
    max = -1000
    for val in data:
        if min>val:
            min = val
        if max < val:
            max = val
    return min, max

def minmax2(data):
    return min(data), max(data)

def sumSquares(n):
    s = 0 
    for i in range(n+1):
        s += i * i
    return s

def sumSquares2(n):
    return sum([k*k for k in range(1,n+1)])
 
def sumOddSquares(n):
    return sum([k*k for k in range(1,n+1) if k%2==1])

#reutnrs random val from data
def choice(data):
    return(data[random.randrange(0,len(data))])

def distinctPairs(data):
    for i in range(len(data)):
        for k in range(i+1, len(data)):
            if (data[i] + data[k] )%2==0:
                return data[i], data[k]
    return 0,0
    


if __name__ == "__main__":
    main()  # This tells compiler to run the main program

