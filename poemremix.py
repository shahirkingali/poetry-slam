# Open file 
f = open(r"poem.txt", "r")
lines = []
for line in f.readlines():
    lines.append(line.rstrip())
for element in lines:
    print(element)

#Lines Backward
def lines_printed_backward():
    poem = open("poem.txt")
    lines = poem.readlines()
for line in reversed(lines):
    print(line)

#Lines Random
def lines_printed_random(words):
    random_lines = len(words)
    for i in range(len(words)):
        line_index = random.randint(1, random_lines-1)
        print(words[line_index])

#Lines Custom




