class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg = msg

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg = msg

try:
    age = int(input("enter age : "))
    if age > 60 :
        raise TooOldException("Too old to marry")
    elif age < 18 :
        raise TooYoungException("Too early to marry")
    elif age >18 and age < 60:
        print("Eligible")
    else:
        print("invalid inputs")

except Exception as msg:
    print("Except Class name : ", msg.__class__.__name__)
    print("Exception description : ",msg)
