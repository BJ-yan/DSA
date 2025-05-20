# 匹配字符
import re

print(re.match("\.it", ".it"))
print(re.search("\d+.+", "iiiit666aaa777999").group())

#替换 complie(正则表达式1).sub(用来替换的字符串s1， 要被替换的字符串s2)
#把s2中满足1的替换成s1

#语法糖：
#re.sub(正则表达式， 用来替换的字符串s1， 要被替换的字符串s2)
#string.replace 也可以替换，但不支持正则
s1 = "车主说，你的刹车片该换了啊，嘿嘿"

rg = r"啊|嘿"

rg_objcet = re.compile(rg)

result = rg_objcet.sub('a', s1)
print(result)

def outer():
    num = 5
    def inner():
        nonlocal num
        num = num * 2
        return num
    return inner

func = outer()
result = func()

print(result)