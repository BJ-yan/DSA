#列表集合推导式
#生成1 - 5列表

list1 = [i for i in range(1, 6)]
list2 = [i for i in range(6, 11)]
set1 = {i for i in range(1, 6)}
dict1 = {list1[i] : list2[i] for i in range(len(list1))}

print(dict1)

my_generator = (i for i in range(1, 6))
print(my_generator)

# 生成器中获取数据
# next
# 遍历

print(next(my_generator))

def get_generator():
    for i in range(1, 6):
        yield i
    print("方法还执行了")
    return "执行结束"

print(get_generator())

def example():
    x = 1
    y = 10
    while x < y:
        yield x
        print("example 方法执行了")
        x += 1

for value in example():
    print(value)
