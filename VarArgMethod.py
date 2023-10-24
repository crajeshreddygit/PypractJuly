class Test:
    def tot(self, *arg):
        tot = 0
        for x in arg:
            tot = tot + x
        #return tot
        print("Total is :{}".format(tot))

t = Test()
t.tot()
print(t.tot(10))
t.tot(10,20)
print(t.tot(10,20,30))
