from bopomofo import Bopomofo


DECODER = Bopomofo()
ERROR_LOG = "FAIL to make a correct translation."


def test_trans_1():
    print("-"*30)
    input_text = "你聽你的鳥鳴，他看他的日出"
    result = DECODER.trans(input_text)
    print(input_text)
    print(result)
    assert  result == "ㄋㄧˇ ㄊㄧㄥ- ㄋㄧˇ ㄉㄧˊ ㄉㄧㄠˇ ㄇㄧㄥˊ ， ㄊㄚ- ㄎㄢˋ ㄊㄚ- ㄉㄧˊ ㄖˋ ㄔㄨ-", ERROR_LOG
    print("test-trans-1: Pass")
    print()


def test_trans_2():
    print("-"*30)
    input_text = "吃苦當吃補"
    result = DECODER.trans(input_text)
    print(input_text)
    print(result)
    assert  result == "ㄔ- ㄎㄨˇ ㄉㄤ- ㄔ- ㄅㄨˇ", ERROR_LOG
    print("test-trans-2: Pass")
    print()


test_trans_1()
test_trans_2()

