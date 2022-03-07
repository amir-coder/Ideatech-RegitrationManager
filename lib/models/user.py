

import json
from lib.controllers.qr_code_generator import QrCodeGenerator
from lib.controllers.req_handler import ReqHandler
from lib.consts.roles import Role
#from lib.consts.workshops import WorkshopEnum


class User:
    #id following MongoDB ObjectId convention
    id='000000000000000000000000'
    email = ''
    firstname = ''
    familyname = ''
    checkedIn = False
    role = Role.default.value
    workshop = 'no_workshop'

    def __init__(self, email, firstname, familyname, checkedIn=False, role=Role.default, workshop= 'no_workshop'):
        self.email = email
        self.firstname = firstname
        self.familyname = familyname
        self.checkedIn = checkedIn
        self.role = role
        self.workshop = workshop

    def toJson(self):
        #converting to dict
        data = {
            #"id":self.id,
            "email": self.email,
            "firstname" : self.firstname,
            "familyname" : self.familyname,
            "checkedIn" : 'True' if self.checkedIn else 'False' ,
            "role" : self.role,
            "workshop" : self.workshop,
        }

        #converting to json
        jsonData = json.dumps(data)
        return jsonData

    def toDict(self):
        #converting to dict
        data = {
            "_id": self.id,
            "email": self.email,
            "firstname" : self.firstname,
            "familyname" : self.familyname,
            "checkedIn" : json.dumps(self.checkedIn),
            "role" : self.role,
            "workshop" : self.workshop,
        }
        return data
    
    def toCash(self):
        data = {
            "id": self.id,
            "email": self.email,
        }
        return data

    def saveToDB(self):
        self.id = ReqHandler.userToDB(data = self.toDict())
    
    def exportToQR(self):
        #testing if id is changed from default value
        if id != '000000000000000000000000':
            QrCodeGenerator.generate(id= self.id, filename= self.firstname + '-'+  self.familyname + '-'+ self.id)
        else:
            print('LOG: export user: '+ self.email + ' failed because id is on default value.')