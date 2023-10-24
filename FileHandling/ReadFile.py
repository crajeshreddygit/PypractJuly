f = open("F:\PypractJuly\PytestFile.txt", 'r')
data = f.readlines()
print(data)
print("-----")
for line in data:
    print(line,end='')

f.close()
