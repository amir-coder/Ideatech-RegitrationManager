import enum
import pandas as pd
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

    workshopsDF = {
        "react": pd.read_csv('./assets/workshops/Workshop results - React.csv', usecols=cols),
        "ds": pd.read_csv('./assets/workshops/Workshop results - AI.csv', usecols=cols),
        "uiux" :pd.read_csv('./assets/workshops/Workshop results - UI_UX.csv', usecols=cols),
        "mobile" :pd.read_csv('./assets/workshops/Workshop results - Mob Dev.csv', usecols=cols),
    }

    #TODO: add competition DF


    @classmethod
    def getWorkshops(cls):
        return cls.workshops["react"]

    #return updated Workshop object from csv registrations
    @classmethod
    def readWorkshopParticipants(cls, workshopName = "react", workshop = Workshop()):
        df = cls.workshopsDF[workshopName]
        #adding the participants and saving to cash
        for index in range(0, df.shape[0]):
            workshop.addParticipant(firstname = df.at[index, 'firstname'], familyname = df.at[index, 'familyname'], email  = df.at[index, 'email'])


