fn = input("enter filename")
f=open(fn,'w')
while True:
    inp = input("enter data to write")
    f.write(inp + '\n')
    op = input("do you want to add more Y/N?")
    if op.lower().strip(" ")=='n':
        break
f.close()

print("completed")
