from sys import argv
f = open(argv[1], "rb")
g = open(argv[2], "rb")
s = f.read()
o = g.read()
f.close()
g.close()
w=""
for i in range(0,30):
    w=w+chr(s[i] ^ o[i])


t=w[0:2]
p=w[0:2]
index=1
while t!=-1:
    index += 1
    v=w[0:index]
    m=w[index:]
    t=m.find(v)
    p=w[0:index-1]
print(p)