import os
fn = input("enter file")
if os.path.isfile(fn):
    print("file exist :", fn)
    lc = wc = cc = 0
    f = open(fn, 'r')
    for line in f:
        c = len(line.split())
        cc += len(line)
        wc += c
        lc += 1
    print("total lines is :", lc)
    print("total words :", wc)
    print("total Chars :", cc)
    f.close()
else:
    print("file not exists")
