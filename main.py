from lib import generator


def main():
    #testing qr code creation
    gen = generator.Generator()
    gen.generate(["123123", "456456"])
    return 0


if __name__ == '__main__':
    main()