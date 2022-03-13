

import pandas

from lib.models.user import User


class CacheController():
    workshops_cache_path = './assets/cash/workshops_cash.csv'
    participants_cache_path = './assets/cash/participants_cash.csv'
    cols = ['email', 'id']
    
    @classmethod
    def addUsersToCache(cls, users = [], isParticipant = False, cachePath = ''):
        if cachePath != '':
            path = cachePath
        else:
            path = cls.workshops_cache_path if not isParticipant else cls.participants_cache_path
        df = pandas.read_csv(path, usecols=cls.cols)
        for user in users:
            userCache = user.toCash()
            if userCache['id'] != '000000000000000000000000':
                df = df.append(userCache, ignore_index=True)
                print('LOG: CacheController:' + userCache['id'] + ' added to cash')
            else:
                print('LOG: CacheController: cannot add ' + userCache['id'] + ' with default id')
        
        df.to_csv(path)
        del df

