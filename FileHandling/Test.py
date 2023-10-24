from datetime import datetime

f = open("F:\PypractJuly\PytestFile.txt",'w')
f.write("raj")
f.write(" reddy\n")

l= ["Sadhana"," NandaGopal", " Manasa"]
f.writelines(l)
f.close()
print(f.closed)
