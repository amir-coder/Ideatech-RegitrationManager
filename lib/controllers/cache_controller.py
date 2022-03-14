import pandas



class CacheController():
    workshops_cache_path = './assets/cache/workshops_cache.csv'
    participants_cache_path = './assets/cache/participants_cache.csv'
    cols = ['email', 'id']
    
    @classmethod
    def addUsersToCache(cls, users = [], isParticipant = False, cachePath = ''):
        if cachePath != '':
            path = cachePath
        else:
            path = cls.workshops_cache_path if not isParticipant else cls.participants_cache_path
        df = pandas.read_csv(path, usecols=cls.cols)
        for user in users:
            userCache = user.tocache()
            if userCache['id'] != '000000000000000000000000':
                df = df.append(userCache, ignore_index=True)
                print('LOG: CacheController:' + userCache['id'] + ' added to cache')
            else:
                print('LOG: CacheController: cannot add ' + userCache['id'] + ' with default id')
        
        df.to_csv(path)
        del df

