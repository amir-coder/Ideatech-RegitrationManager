from lib.consts.workshops import WorkshopEnum
from lib.controllers import qr_code_generator
from lib.controllers.cash_controller import CashController
from lib.controllers.mainController import MainController
from lib.controllers.tab_data_controller import TabDataController
from lib.models.user import User
from lib.models.workshop import Workshop


def main():
    #testing user generation
    #print(TabDataController.getWorkshops())
    MainController.registerCompetition()



# ai_workshop = Workshop(name= WorkshopEnum.ds.value)
# TabDataController.readWorkshopParticipants(
#     workshop=ai_workshop,
#     workshopName='ds',
# )

# for participant in ai_workshop.getParticipants():
#     print(participant.toDict())


# #testing user generation
#     user  = User("testpy9@gmail.com", 'Amir', 'Almamou')
#     user.saveToDB()
#     print(user.toDict())
#     user.exportToQR()

if __name__ == '__main__':
    main()