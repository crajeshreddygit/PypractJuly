with open("testwith.txt",'w') as f:
    f.write("rajesh\n")
    f.write("reddy\n")
    f.write("challa\n")
    print("is file closed:",f.closed)
print("Is 2nd file close: ",f.closed)
