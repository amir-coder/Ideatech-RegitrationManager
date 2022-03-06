from lib.controllers import qr_code_generator
from lib.models.user import User


def main():
    #testing user generation
    user  = User("testpy9@gmail.com", 'Amir', 'Almamou')
    user.saveToDB()
    print(user.toDict())
    user.exportToQR()
    return 0


if __name__ == '__main__':
    main()