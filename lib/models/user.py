

import json
from lib.controllers.qr_code_generator import QrCodeGenerator
from lib.controllers.req_handler import ReqHandler
from lib.models.role import Role
from lib.models.workshop import Workshop


class User:
    #id following MongoDB ObjectId convention
    id='000000000000000000000000'
    email = ''
    firstname = ''
    familyname = ''
    checkedIn = False
    role = Role.default.value
    workshop = Workshop.default.value

    def __init__(self, email, firstname, familyname, checkedIn=False, role=Role.default, workshop= Workshop.default):
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
            "role" : self.role.value,
            "workshop" : self.workshop.value,
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
            "role" : self.role.value,
            "workshop" : self.workshop.value,
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