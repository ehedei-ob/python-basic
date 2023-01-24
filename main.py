f = open('file.txt', 'w')
f.write('Hello World!\n')
f.close()

f = open('file.txt', 'r+')
f.readline()
f.write('Segunda línea\n')
f.seek(0)

text = f.read()
f.close()

print(text)