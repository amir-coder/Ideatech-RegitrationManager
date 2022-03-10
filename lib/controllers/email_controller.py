import base64
import email
from pydoc import classname
from config import Config
import smtplib 
import imghdr
import yagmail
from email.message import EmailMessage
from bs4 import BeautifulSoup


class EmailController:
    #smtp server
    s = yagmail.SMTP(user = Config.EMAIL, password = Config.MDP)
    templatePath = './template/index.html'

    @classmethod
    def sendEmail(cls, subject = 'subject',  toAdress = 'email@gmail.com', ):
        #create msg object
        
        with open('./template/index3.html', 'r') as f:
            content = f.read()
        #send msg
        cls.s.send(to=toAdress, subject=subject, contents = content, )

    @classmethod
    def generateBase64FromQR(cls, qrCodePath = ""):
        qrCodePath = './exports/' + qrCodePath
        with open(qrCodePath,"rb") as f:
            stri = str(base64.b64encode(f.read()))
        print(stri[2:-1])
        print()
        return stri[2:-1]


    @classmethod
    def generateFormatedEmailFromTemplate(cls, qrCodePath = ""):
        src= "data:image/png;base64," + cls.generateBase64FromQR(qrCodePath=qrCodePath)
        with open(cls.templatePath, 'rb') as html_file:
            soup = BeautifulSoup(html_file.read(), features='html.parser')
            for img in soup.find_all('img'):
                if 'data' in img['src']:
                    print('found img with src: ' + img['src'])
                    img['src'] = src
                    print('src: '+ img['src'])
        
        content  = soup.prettify()
        with open('./template/email.html', 'w') as f:
            f.write(content)
        
        f.close()
        html_file.close()
    @classmethod
    def sendEmailtest(cls, adress = "", qrCodePath = ""):
        with open('./template/index2.html', 'w') as f:
            f.write(cls.generateFormatedEmailFromTemplate(qrCodePath))