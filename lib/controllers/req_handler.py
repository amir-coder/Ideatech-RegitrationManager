import requests
import configparser
class ReqHandler:


    def __init__(self):
        config = configparser.ConfigParser()
        config.read('../config.ini')
        self.usersRoute = config['DEFAULT']['ConnectionURL'] + ':' + config['DEFAULT']['PORT'] +'/users'

    def userToDB(self, data):
        print(self.usersRoute)
        id = requests.post(self.usersRoute+'/addUser', data = data)
        return id