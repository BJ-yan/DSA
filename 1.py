class Singer(object):
    def __init__(self, name, song):
        self.name = name
        self.song = song

    def fans(self):
        print(f"“{self.name}歌手的{self.song}歌曲持续打榜，粉丝为喜欢的歌手打call”")

if __name__ == "__main__":
    with open('./singer.txt', 'r', encoding = 'utf-8') as fa:
        data = fa.readlines()
        class_list = []
        for line in data:
            pair_data = line.split(" ")
            for pair in pair_data:
                single_data = pair.split("，")
                class_list.append(Singer(single_data[1], single_data[0]))

        for instance in class_list:
            instance.fans()
