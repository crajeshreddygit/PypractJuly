f1 = open("F:\PypractJuly\PytestFile.txt", 'r')
f2 = open("f2.txt",'w')
data = f1.read()
f2.write(data)
f1.close()
f2.close()
