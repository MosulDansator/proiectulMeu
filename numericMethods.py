import math

def twoVectors(n:int,u:list,v:list):
    w = []
    for i in range(n):
        w.append(u[i] + v[i])
    print(w)

n = 2               
a = [1,1]
b = [2,3]
twoVectors(n,a,b)

def scalarProduct(n,u,v):
    p = 0
    for i in range(n):
        p = p + u[i] * v[i]
    print(p)
scalarProduct(n,a,b)

def twoMatrix(n,A,B):
    C = [[],[]]
    for i in range(n):
        for j in range(n):
            C[i].append(A[i][j] + B[i][j])
    print(C) 
n = 2
A = [[1,2],[3,4]]
B = [[1,2],[3,4]]
twoMatrix(n,A,B)

def twoMatrixMultiplied(n,A,B):
    C = []
    for i in range(n):
        C.append([])
    print(C)
    for i in range(n):
        for j in range(n):
            C[i].append(0)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = A[i][k] * B[k][j] + C[i][j]
    print(C)
twoMatrixMultiplied(n,A,B)

def twoPolinomsMultiplied(n,r,q):
    p = []
    for i in range(2*n+1):
        p.append(0)
    for i in range(n+1):
        for j in range(n+1):
            k = i+j-1
            p[k] = (r[i] * q[j] + p[k])
    print(p)
x = [-2,3,4]
y = [1,-5,6]
n = 2 # polinom power 
twoPolinomsMultiplied(n,x,y)

def polinomEvaluation(n,a,xcrt):
    v = a[n]
    for i in range(n,0,-1):
        v = a[i] + v * xcrt
    print(v)
n = 2
a = [2,4,5]
xcrt = 1
polinomEvaluation(n,a,xcrt)

def my_eps(x):
    e = 1
    while(x + e > x):
        e = e/2
    e = e * 2
    print(e)
my_eps(1)

def my_sinus(x,er):
    t = x
    s = t
    k = 1
    i = 1
    while(abs(t) > er):
        k += 2
        t = -t * x**2/k/(k-1)
        s = s + t
        i += 1
    print(s,i) #sinusul unghiului dat si numarul de iterati ca sa ajunga la eroarea impusa
x = math.pi/2
er = 1e-6
my_sinus(x,er)

