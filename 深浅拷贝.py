import copy

if __name__ == "__main__":
    #浅拷贝

    # 可变基础类型 - 不创建新地址
    a = 10
    b = copy.copy(a)

    print(f"a: {id(a)}")
    print(f"b: {id(b)}")

    # 可变
    list1 = [1, 2, 3, 4]
    list2 = list1.copy()

    print(f"list1: {id(list1)}")
    print(f"list2: {id(list2)}")

    list1 = [1]
    print(list1)
    print(list2)

    #深拷贝
    a = 10
    b = copy.deepcopy(a)


    print(f"a {id(a)}")
    print(f"b {id(b)}")

    tuple1 = (1, 2)
    tuple2 = copy.deepcopy(tuple1)


    print(f"tuple1 {id(tuple1)}")
    print(f"tuple2 {id(tuple2)}")





