import base64
import json
import os
import requests

from lib.controllers.email_controller import EmailController


class ReqHandler:

    port = os.environ['PORT']
    url = os.environ['ConnectionURL']
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
    
    def uploadImg(path=''):
        url = ''
        with open('./exports/'  + path, "rb") as file:
            url = "https://api.imgbb.com/1/upload"
            payload = {
                "key":os.environ['IMG_UPLOAD_KEY'],
                "image": base64.b64encode(file.read()),
            }
            res = requests.post(url, payload)
        print(res)
        file.close()
        return res