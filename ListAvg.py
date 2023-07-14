class Test:
    @staticmethod
    def avg(list1):
        result = sum(list1)/len(list1)
        print("Avg is :", result)
        
    @staticmethod
    def wish(name):
        for i in range(10):
            print("Good Work :", i, " time ", name)


list1 = [10, 20, 30, 40]

Test.avg(list1)
Test.wish("Rajesh")
