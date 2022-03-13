import enum
import pandas as pd
from lib.consts.roles import Role
from lib.models.user import User
from lib.models.workshop import Workshop
#class to manipulate tabular data (.xlsx files)

class WorkshopSheetNames(enum.Enum):
    uiux = 4
    ds = 6
    react = 5
    mobile = 3
    default = 0
    

class TabDataController:

    #filter columns
    cols = ['firstname', 'familyname', 'email']
    cacheCols = ['email', 'id']

    workshopsDF = {
        "react": pd.read_csv('./assets/workshops/Workshop results - React.csv', usecols=cols),
        "ds": pd.read_csv('./assets/workshops/Workshop results - AI.csv', usecols=cols),
        "uiux" :pd.read_csv('./assets/workshops/Workshop results - UI_UX.csv', usecols=cols),
        "mobile" :pd.read_csv('./assets/workshops/Workshop results - Mob Dev.csv', usecols=cols),
    }

    competitionParticipantsDFCols = {
        'email': 6,
        'firstname': 1,
        'familyname': 2,
        'team_field1': 13,
        'team_field2': 14,
    }

    orgenizersDFCols = {
        'email': 1,
        'firstname': 2,
    }

    competitionParticipantsDF = pd.read_csv('./assets/competition/ideatech registrations - all-final.csv').astype(str)
    orgenizersDF = pd.read_csv('./assets/orgenizers/ideaTECH organisers.csv').astype(str)

    #TODO: add competition DF


    @classmethod
    def getWorkshops(cls):
        return cls.workshops["react"]

    #update Workshop object from csv registrations
    @classmethod
    def readWorkshopParticipants(cls, workshopName = "react", workshop = Workshop()):
        df = cls.workshopsDF[workshopName]
        #adding the participants and saving to cache
        for index in range(0, df.shape[0]):
            workshop.addParticipant(firstname = df.at[index, 'firstname'], familyname = df.at[index, 'familyname'], email  = df.at[index, 'email'])
    
    #return  list of Users from csv ideatech registrations
    @classmethod
    def readCompetitionParticipants(cls):
        df = cls.competitionParticipantsDF
        participants = []
        #adding the participants and saving to cache
        for index in range(0, df.shape[0]):
            email = df.iat[index, cls.competitionParticipantsDFCols['email']]
            if email != 'nan':
                #register user
                firstname = df.iat[index, cls.competitionParticipantsDFCols['firstname']]
                familyname = df.iat[index, cls.competitionParticipantsDFCols['familyname']]
                team_field1 = df.iat[index, cls.competitionParticipantsDFCols['team_field1']]
                team_field2 = df.iat[index, cls.competitionParticipantsDFCols['team_field2']]
                team = team_field1 if team_field1 != 'nan' else team_field2
                team ='ESI-ALGIERS' if 'esi' in team.lower() else team
                team= 'no_team' if team == 'nan' else team
                participants.append(User(
                    email=email,
                    familyname=familyname,
                    firstname=firstname,
                    role=Role.default.value,
                    team= team
                ))
        
        return participants


    #return  list of Users from csv ideatech registrations
    @classmethod
    def readcache(cls, cachePath = './assets/cache/test.csv'):
        df = pd.read_csv(cachePath, usecols=cls.cacheCols).astype(str)
        adresses = []
        tmp = {
            'email' :'',
            'id' : '',
        }

        for index in range(0, df.shape[0] ):
            tmp = {
            'email' :df.at[index, 'email'],
            'id' : df.at[index, 'id'],
            }
            adresses.append(tmp)
            print(index)
        
        return adresses

        
    @classmethod
    def readOrgenizers(cls):
        df = cls.orgenizersDF
        orgenizers = []
        #adding the participants and saving to cache
        for index in range(0, df.shape[0]):
            email = df.iat[index, cls.orgenizersDFCols['email']]
            if email != 'nan':
                #register user
                firstname = df.iat[index, cls.orgenizersDFCols['firstname']]
                familyname = ''
                orgenizers.append(User(
                    email=email,
                    familyname=familyname,
                    firstname=firstname,
                    role='orgenizer'
                ))
        
        return orgenizers

            
    @classmethod
    def readTrainers(cls):
        df = cls.trainerssDF
        trainers = []
        #adding the participants and saving to cache
        for index in range(0, df.shape[0]):
            email = df.iat[index, cls.orgenizersDFCols['email']]
            if email != 'nan':
                #register user
                firstname = df.iat[index, cls.orgenizersDFCols['firstname']]
                familyname = ''
                trainers.append(User(
                    email=email,
                    familyname=familyname,
                    firstname=firstname,
                    role='trainer'
                ))
        
        return trainers


