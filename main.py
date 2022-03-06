from lib import qr_code_generator


def main():
    #testing qr code creation
    gen = qr_code_generator.QrCodeGenerator()
    gen.generate(["123123", "456456"])
    return 0


if __name__ == '__main__':
    main()