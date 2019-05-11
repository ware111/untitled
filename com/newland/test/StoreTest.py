import json

def input_number():
    number = input("请输入你喜欢的数字\n")
    fs = open("c:\\file11.json", "w")
    json.dump(number, fs)


def load_number():
    try:
        fs = open("c:\\file11.json")
    except FileNotFoundError:
        return None
    else:
        number = json.load(fs)
        return number


if load_number():
    print(load_number())
else:
    input_number()