
from lib.consts.workshops import WorkshopEnum
from lib.controllers import qr_code_generator
from lib.controllers.cache_controller import CashController
from lib.controllers.email_controller import EmailController
from lib.controllers.main_controller import MainController
from lib.controllers.req_handler import ReqHandler
from lib.controllers.tab_data_controller import TabDataController
from lib.models.user import User
from lib.models.workshop import Workshop


def main():
    MainController.sendEmails(mailsListPath='./assets/cache/workshops_cache.csv')


if __name__ == '__main__':
    main()