import copy

if __name__ == "__main__":

    a = 10
    b = copy.copy(a)

    print(f"a: {id(a)}")
    print(f"b: {id(b)}")


