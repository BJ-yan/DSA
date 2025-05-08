if __name__ == "__main__":
    max_str = "woaiheima, buguanheimahaishibaima, zhaodaogongzuojiushihaoma"

    min_str = "heima"

    # count统计
    result = max_str.count(min_str)
    print("#1: ", result)

    #split, 每次切割等于找到一次，因此总数为，list长度-1
    list1 = max_str.split(min_str)
    print(list1)
    result = len(list1) - 1
    print("#2: ", result)

    #替换处理
    new_str = max_str.replace(min_str, "")
    result = (len(max_str) - len(new_str)) // len(min_str)
    print("#3: ", result)

    #find + 切片
    result = 0
    while(max_str.find(min_str) != -1):
        start_index = max_str.find(min_str) + len(min_str)
        max_str = max_str[start_index:]
        result += 1
    print("#4：", result)
