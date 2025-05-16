class Test(object):
    def __init__(self, tag):
        self.tag = tag

    @classmethod
    def cMethod(cls):
        print("类方法调用")

    @staticmethod
    def sMethod():
        print("静态方法调用")


if __name__ == "__main__":
    #调用类方法
    Test.cMethod()

    Test.sMethod()