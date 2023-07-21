class outer:
    def __init__(self):
        print("This is Outer class constructor")

    class inner:
        def __init__(self):
            print("This is Inner class constructor")

        def m1(self):
            print("Inner class method")


o = outer()

i = o.inner()
i.m1()
outer().inner().m1()

