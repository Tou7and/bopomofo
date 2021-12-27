import time
from bopomofo import Bopomofo

# TEXT = "如果他能從這扇門望見日出的美景，你又何必要求他走向那扇窗去 聆 聽鳥鳴呢？你聽你的鳥鳴，他看他的日出，彼此都會有 等量 的美的感受。人與人偶有 摩擦 ，往往都是由於缺乏那分雅量的 緣故 。因此，為了減少摩擦，增進和諧，我們必須努力 培養 雅量。"

TEXT = "你聽你的鳥鳴，他看他的日出"
DECODER = Bopomofo()

def test_trans(input_text):

    result = DECODER.trans(input_text)
    print(input_text)
    print(result)
    assert  result == "ㄋㄧˇ ㄊㄧㄥ- ㄋㄧˇ ㄉㄧˊ ㄉㄧㄠˇ ㄇㄧㄥˊ ， ㄊㄚ- ㄎㄢˋ ㄊㄚ- ㄉㄧˊ ㄖˋ ㄔㄨ-", "FAIL to make a equal bopomofo translation."
    print("test-trans: Pass")

test_trans(TEXT)

# print(DECODER.trans("的"))
print(DECODER.trans("好"))
print(DECODER.trans("好的"))
