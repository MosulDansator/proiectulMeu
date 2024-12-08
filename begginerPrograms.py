import math
#in python you dont really need to specify which data you want to attend to a variable
#exemple you can say x = 2 and the compiler will suggest 2 is a number(integer)

x = 2
print(x)

#There are 4 fundamenta data types:
# list
# string
# integr 
# boolean

#Check if a numbers is odd or not

def checkIsOdd(n:int):
    if n % 2 == 0:
        print("Is odd")
    else:
        print("Is not odd")

#Check if a number is prime

def isPrime(n):
    prime = True
    for i in range(2,n // 2 + 1):
        if n % i == 0:
            prime = False
            break
    if prime == True:
        print("Its prime")
    else:
        print("Its not prime")
    
#Check if a number is palindrom ex: 12321
def isPalindrom(n):
    clone = n
    alt = 0
    while(n):
        alt = alt * 10 + n%10
        n //= 10
    if clone == alt:print("Is palindrom")
    else:print("Its not palindrom")

#Nth fibbonaci number
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

#Sum of divizors
def sumOfDiv(n):
    sum = 1
    for i in range(2,n // 2 + 1):
        if n % i == 0:
            sum += i
    #another method
    i = 2
    sum = 1
    while(n != 1):
        if n % i == 0:
            sum += i
            n //= i
        i += 1
         
#Check if a list is palindrom        
def ckListPal(v:list):
    # return v == v[::-1] #my fav trick you can do this is one line but lets do it anyways

    pal = True 
    for i in range(len(v) // 2):
        j = len(v) - i - 1
        if v[i] != v[j]:
            pal = False
            break
    if pal == True:print("Palindrom")
    else:print("Not Palindrom")

#Decompose a number as sum of powers of 2  ex: 9 = 2^3 + 2^0 
def sumPow2(n):
    sum = []
    nth = int(math.sqrt(n))
    while(n != 1 and n != 0):
        if 2**nth <= n:
            sum.append(2**nth) 
            n -= 2**nth
        elif 2**nth > n:
            nth -= 1
    if n == 1: sum.append(1)
    print(sum)

#determines the number in the string that has the lowest first digitl if more have the same
#choose the bigger one

def lastMinDigit(v):
    minDig = 10
    maxNr = 0
    for nr in v:
        if minDig > nr % 10:
            minDig = nr % 10
            if nr > maxNr:
                maxNr = nr
    print(maxNr)

#greatest common divizor between two numbers (Euclid)
def gcd(x,y):
    while(x != y):
        if x > y:
            x -= y
        else:
            y -= x
    print(x)
gcd(86,43)

#least common multiple
def lcd(a,b):
    n = a
    m = b
    while(n != m):
        if n > m : 
            m += b
        else:
            n += a
    print(n)

#decompose in prime factors 120 = 2^2 + 5^1 + 7^1
def primeFactors(n):
    dict =  {}
    d = 2
    while(n != 1):
        if n % d == 0:
            p = 0
            while(n % d == 0):
                n //= d
                p += 1 
            dict[d] = p 
        d += 1
    print(dict)

#Transform from base 10 in base b

def base10toB(nr,b):
    digits = []
    while(nr / b != 0):
        digits.insert(0,nr%b)
        nr //= b
    print(f"{digits} in base {b} from 10")
base10toB(24,2)

#Transfrom from base b in base 10
def baseBto10(nr,b):
    n = 0
    i = 0
    while(nr):  
        n += nr%10 * b**i
        nr //= 10
        i += 1
    print(n)
baseBto10(11000,2)