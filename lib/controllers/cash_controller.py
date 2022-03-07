

import pandas

from lib.models.user import User


class CashController():
    workshops_cash_path = './assets/cash/workshops_cash.csv'
    participants_cash_path = './assets/cash/workshops_cash.csv'
    cols = ['email', 'id']
    
    @classmethod
    def addUsersToCash(cls, users = [], isParticipant = False):

        path = cls.workshops_cash_path if not isParticipant else cls.participants_cash_path
        df = pandas.read_csv(path, usecols=cls.cols)
        for user in users:
            userCash = user.toCash()
            if userCash['id'] != '000000000000000000000000':
                df = df.append(userCash, ignore_index=True)
                print('LOG: CashController:' + userCash['id'] + ' added to cash')
            else:
                print('LOG: CashController: cannot add ' + userCash['id'] + ' with default id')
        
        df.to_csv(path)

