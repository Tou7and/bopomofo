import json
from pathlib import Path


WORD_PATH = Path(__file__).resolve().with_name('words.json')


class Bopomofo:
    """ Convert Mandarin Hanzi to Bopomofo.

    Usage:
    >> from bopomofo import Bopomofo
    >> bopo = Bopomofo()
    >> pinyin = Bopomofo.trans("你好")
    >> print(pinyin)

    """
    def __init__(self, word_path=str(WORD_PATH)):
        with open(word_path, "r") as reader:
            self.words = json.load(reader)

    def trans_word(self, text):
        if text in self.words:
            return self.words[text]
        else:
            return text

    def trans(self, text):
        ret = ""
        buf = ""
        for x in text:
            if x not in self.words:
                ret = ret + ' ' + self.trans_word(buf)
                buf = ""
                ret = ret + ' ' + self.trans_word(x)
                continue
            if buf + x not in self.words:
                ret = ret + ' ' + self.trans_word(buf)
                buf = x
            else:
                buf = buf + x
        ret = ret + ' ' + self.trans_word(buf)
        return ret[1:]


