import  json


def get_stored_name():
    try:
        fs = open("c:\\file2.json")
    except FileNotFoundError:
        return None
    else:
        username = json.load(fs)
        return username


def set_username():
    fs = open("c:\\file.json2", 'a')
    username = input("请输入你的用户名")
    json.dump(username, fs)


def login():
    username = get_stored_name();
    if username:
       print("welcome to back")
    else:
        set_username()
        print("Hi,friend")


login()