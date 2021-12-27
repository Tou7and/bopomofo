""" Update changes to the word dictionary.

"""
import json

# TODO: I found are many common errors of the dict, and the dict may need updates
# Or maybe I just call the xpinyin library, and implement the pinyin-to-bopomofo convertion?


def load_dict(json_path):
    with open(json_path, "r") as reader:
        py_dict = json.load(reader)
    return py_dict


def dump_dict(py_dict, json_path):
    with open("data/words.json", "w") as writer:
        json.dump(words, writer)
    return


def update_v1_0_1():
    words = load_dict("src/bopomofo/words.json")


    print("Before:")
    print(words["的"])
    print()


    words["的"] = "ㄉㄜ-"
    words["好"] = "ㄏㄠˇ"


    print("After:")
    print(words["的"])
    print()

    return 

update_v1_0_1()


