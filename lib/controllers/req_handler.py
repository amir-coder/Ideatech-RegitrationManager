from models.user import User
import env.consts as cts
import requests
class ReqHandler:

    usersRoute = cts.CONNECTIONURL + ':' + cts.PORT +'/users'
    def userToDB(self, data):
        id = requests.post(self.usersRoute+'/addUser', data = data)
        
        return id