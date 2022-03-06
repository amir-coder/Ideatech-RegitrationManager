

import json
from lib.controllers.req_handler import ReqHandler
from lib.models.role import Role
from lib.models.workshop import Workshop


class User:
    id=''
    email = ''
    firstname = ''
    familyname = ''
    checkedIn = False
    role = Role.default
    workshop = Workshop.default

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
            "id":self.id,
            "email": self.email,
            "firstname" : self.firstname,
            "familyname" : self.familyname,
            "checkedIn" : self.checkedIn,
            "role" : self.role,
            "workshop" : self.workshop,
        }

        #converting to json
        jsonData = json.dumps(data)
        return jsonData

    def toDict(self):
        #converting to dict
        data = {
            id:self.id,
            "email": self.email,
            "firstname" : self.firstname,
            "familyname" : self.familyname,
            "checkedIn" : self.checkedIn,
            "role" : self.role,
            "workshop" : self.workshop,
        }
        return data
    
    def  saveToDB(self):
        self.id = ReqHandler.userToDB(self.toDict)