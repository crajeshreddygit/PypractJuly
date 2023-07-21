class Bird:
    wings = 2

    @classmethod
    def fly(cls, name):
        print(" The {} bird is flying with {} wings".format(name, cls.wings))


Bird.fly("Eagle")
Bird.fly("Parrot")
