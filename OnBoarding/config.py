def main():
    try:
        configuration = open('config.txt')
        print("succes open file!")
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()