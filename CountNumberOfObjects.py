class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count + 1
        print("Object creating :", Test.count)

    @classmethod
    def getNumberOfObject(cls):
        print("total objects created :",Test.count)

Test.getNumberOfObject()
t=Test()

t1=Test()

t2=Test()
Test.getNumberOfObject()
