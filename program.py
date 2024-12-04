#verifcam daca e palindrom
n = int(input()) #1221
clona = n
alt = 0
while(n):
	alt = alt*10 + n%10
	n //= 10
if clona == alt:
	print("e palindrom")
else:
	print("nu e palindrom")

