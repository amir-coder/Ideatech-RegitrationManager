import json
import requests

from config import Config


class ReqHandler:

    port = Config.PORT
    url = Config.ConnectionURL
    usersRoute = url + ':' + port +'/users'



    @classmethod
    def userToDB(cls, data = {}):
        #masking id from data
        sendData = {
            "email": data['email'],
            "firstname" : data['firstname'],
            "familyname" : data['familyname'],
            "checkedIn" : data['checkedIn'],
            "role" : data["role"],
            "workshop" : data["workshop"],
        }
        res = requests.post(cls.usersRoute+'/add', data = sendData)
        #if user added or user exists return updated id
        if res.status_code == 200 or res.status_code == 400:
            #update data
            data = json.loads(res.content)
            print(data['_id'])
            return data['_id']