from sys import argv
if len(argv) != 4:
    print('USAGE: python3 project.py <password> <input_file> <output_file>')
    exit()

if not (argv[1].isalnum()):
    print('ERROR: Password must be a string with lowercase or uppercase letters or numbers.')
    exit()

if len(argv[1]) < 10 or len(argv[1]) > 15:
    print('ERROR: Password must have between 10-15 characters.')
    exit()
    
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
