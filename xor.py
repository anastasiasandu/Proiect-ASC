from sys import argv

f = open(argv[2], "rb")
g = open(argv[3], "wb")

s = bytearray(f.read())
f.close()
key = bytearray(argv[1], encoding="UTF-8")

content = []
n = len(argv[1])
i = 0

for _, byte in enumerate(s):
    content.append(byte ^ key[i])
    i = (i + 1) % n

g.write(bytearray(content))
g.close()