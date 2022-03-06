from lib.controllers import qr_code_generator
from lib.models.user import User


def main():
    #testing user generation
    user  = User("email@gmail.com", 'Amir', 'Almamou')
    print(user.toDict())
    return 0


if __name__ == '__main__':
    main()