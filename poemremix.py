# Open file 
f = open(r"poem.txt", "r")
lines = []
for line in f.readlines():
    lines.append(line.rstrip())
for element in lines:
    print(element)

#Lines Backward
textfile = open("poem.txt")
lines = textfile. readlines()
for line in reversed(lines):
    print(line)
textfile. close()

#Lines Random
