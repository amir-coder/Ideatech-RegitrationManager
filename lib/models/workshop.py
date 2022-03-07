from lib.consts.roles import Role

from lib.models.user import User
from lib.consts.workshops import WorkshopEnum

class Workshop():

    #list of participants type user
    participants = []

    def __init__(self, name = WorkshopEnum.default.value):
        self.name = name

    
    def addParticipant(self, email = 'useremail@email.com', firstname = 'pronoun', familyname = 'lastname'):
        self.participants.append(User(
            workshop= self.name,
            role = Role.in_workshop.value,
            email=email,
            firstname=firstname,
            familyname=familyname,
        ))
        print('LOG: participant '+email+' added to workshop ' +self.name)

    def getParticipants(self):
        return self.participants
    
    
    def updateParticipant(self, email = 'email', id = 'id'):
        for participant in self.participants:
            if participant.email == email:
                participant.id = id
    
    def saveParticipantsToDB(self):
        if len(self.participants) != 0:
            for participant in self.participants:
                participant.saveToDB()
                print('LOG: participant '+participant.email+' in workshop ' +self.name +' saved to db')
    
    def exportParticipantsToQR(self):
        if len(self.participants) != 0:
            for participant in self.participants:
                participant.exportToQR()
                print('LOG: participant '+participant.email+' in workshop ' +self.name +' exported to QR')