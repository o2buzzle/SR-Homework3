from core_interactions import interpreter


def main():
    while True:
        command = input(">>> ")
        print(interpreter(command))


if __name__ == "__main__":
    main()
