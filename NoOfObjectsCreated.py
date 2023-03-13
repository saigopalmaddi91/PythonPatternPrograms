class Test:
    count = 0

    def __init__(self):
        Test.count += 1

    @classmethod
    def getNumOfObjects(cls):
        print("Total number of objects created : ", cls.count)


Test.getNumOfObjects()
t1 = Test()
Test.getNumOfObjects()
t2 = Test()
Test.getNumOfObjects()
t3 = Test()
Test.getNumOfObjects()
