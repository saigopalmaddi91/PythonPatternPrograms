class Bird:
    wings = 2

    @classmethod
    def fly(cls, name):
        print(f"{name} is flying with {cls.wings} wings")


Bird.fly("Parrot")
Bird.fly("Eagle")
