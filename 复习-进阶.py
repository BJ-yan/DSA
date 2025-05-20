class AAA():
   def __init__(self):
        self.__name = "abc"
# 实现一个闭包
def fun_outer():
    num = 10
    def fun_inner(number):
        nonlocal num
        num += number
        return num
    return fun_inner

#实现一个装饰器
def checker(fn):
    def inner():
        print("run checker")
        fn()

    return inner

@checker
def original_func():
    print("original func print")

#装饰器有参有返回值
def checkerPlus(fn):
    def inner(a, b):
        print("increase run")
        a += 10
        b += 10
        return fn(a, b)
    return inner

@checkerPlus
def originalFuncPlus(a, b):
        return a + b

# 多个装饰器

def checkStatus(fn):
    def inner(*args, **kwargs):
        print("status check")
        fn(*args, **kwargs)
    return inner

def checkCondition(fn):
    def inner(*args, **kwargs):
        print("condition check")
        fn(*args, **kwargs)
    return inner

# @checkCondition
# @checkStatus
def origian(**kwargs):
    sum = 0

    for kwarg in kwargs.values():
        sum += kwarg

    print(sum)



if __name__ == "__main__":
    string1 = "abcdefg"

    # 切片
    slice = string1[:len(string1): 7]
    print(slice)

    #find
    find1 = string1.find('cde')
    print(find1)
    find2 = string1.find("aaa")
    print(find2)
    find3 = string1.find("cd", 3, len(string1))
    print(find3)

    string2 = "aaaabbbccdd"
    find4 = string2.count('a')
    print(find4)

    string3 = string2.replace('a', "^", 1)
    print(string3)

    print(string3.join("123"))

    set = {1, 2, "a"}

    for i, element in enumerate(set):
        print(i, element)

    #列表推导式
    list1 = [[i for i in range(10) if i % 2 == 0] for j in range(10)]
    print(list1)

    print(fun_outer()(10))

    original_func()


    print(originalFuncPlus(19, 19))

    a = 10
    b = {"a": 11, "b": 12}

    origian(a = 10 , b = 11)