import sys
from bopomofo import Bopomofo


DECODER = Bopomofo()


def check_words(input_text):
    print("-"*10)
    print("Decode output:")
    print(DECODER.trans(input_text))
    print()

    print("Is it in the lexicon?")
    print(input_text in DECODER.words)
    print()


if __name__ == "__main__":
    while True:
        x = input(">>> ")
        check_words(x)
