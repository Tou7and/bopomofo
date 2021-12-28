from dragonmapper.hanzi import to_pinyin
from dragonmapper.transcriptions import pinyin_to_zhuyin

def hanzi_to_zhuyin(text):
    text = text.strip()
    text_ls = list(text)
    text = " ".join(text_ls)

    pinyin = to_pinyin(text)
    zhuyin = pinyin_to_zhuyin(pinyin)
    return zhuyin

if __name__ == "__main__":
    with open("samples.csv", "r") as reader:
        lines = reader.readlines()

    for line in lines:
        zhu = hanzi_to_zhuyin(line)
        print(zhu)

