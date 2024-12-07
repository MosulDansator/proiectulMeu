
#We imported/took data from another file(date.txt) into this one to work with them

with open('date.txt') as f:
    numere = [int(line.strip()) for line in f]
print(numere)