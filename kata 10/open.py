def main():
    try:
        open("mars.jpg")
    except FileNotFoundError as err:
        print("got a problem trying to read the file:", err)

if __name__ == '__main__':
    main()


def main():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")

if __name__ == '__main__':
    main()