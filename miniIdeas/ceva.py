import sys

print(f"test cu {sys.argv[1:]}")
#lista = list(int(sys.argv[1:]))
lista = []
for i in range(1,len(sys.argv)):
    lista.append(int(sys.argv[i]))
print(lista)
sumaListei = sum(lista)
prim = True
for i in range(1,sumaListei//2 + 1):
    if sumaListei % i == 0:
        prim = False
        break
if prim == True: print("suma listei e un nr prim")
else: print(f"suma listei:{sumaListei} nu este un numar prim")