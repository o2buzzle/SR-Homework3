from re import I
from core_interactions import interpreter
from preprocess import preprocess


def main():
    while True:
        command = input(">>> ")
        prep_query = preprocess(command)
        print(interpreter(prep_query))


if __name__ == "__main__":
    main()
