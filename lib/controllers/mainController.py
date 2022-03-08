


#class that contains global functions
from lib.consts.workshops import WorkshopEnum
from lib.controllers.cash_controller import CashController
from lib.controllers.tab_data_controller import TabDataController
from lib.models.workshop import Workshop


class MainController:

    @classmethod
    def registerWorkshops(cls):
        #create workshops
        ai_workshop = Workshop(name=WorkshopEnum.ds.value)
        mobile_workshop = Workshop(name=WorkshopEnum.mobile.value)
        react_workshop = Workshop(name=WorkshopEnum.react.value)
        uiux_workshop = Workshop(name=WorkshopEnum.uiux.value)
        print('LOG: workshop created')

        #read participants
        TabDataController.readWorkshopParticipants(workshopName='ds', workshop=ai_workshop)
        TabDataController.readWorkshopParticipants(workshopName='mobile', workshop=mobile_workshop)
        TabDataController.readWorkshopParticipants(workshopName='react', workshop=react_workshop)
        TabDataController.readWorkshopParticipants(workshopName='uiux', workshop=uiux_workshop)

        #save participants to DB
        ai_workshop.saveParticipantsToDB()
        mobile_workshop.saveParticipantsToDB()
        react_workshop.saveParticipantsToDB()
        uiux_workshop.saveParticipantsToDB()

        #save to cash file
        CashController.addUsersToCash(ai_workshop.getParticipants())
        CashController.addUsersToCash(mobile_workshop.getParticipants())
        CashController.addUsersToCash(react_workshop.getParticipants())
        CashController.addUsersToCash(uiux_workshop.getParticipants())

    @classmethod
    def registerCompetition(cls):

        #read participants
        participants = TabDataController.readCompetitionParticipants()
        #save participants to DB
        for participant in participants:
            participant.saveToDB()

        #save to cash file
        CashController.addUsersToCash(participants, isParticipant=True)
