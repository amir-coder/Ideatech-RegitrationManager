import base64
import yagmail
from bs4 import BeautifulSoup
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class EmailController:
    #smtp server
    s = yagmail.SMTP(user = os.environ['ORG_EMAIL'], password = os.environ['ORG_MDP'])
    templatePath = './template/template.html'

    @classmethod
    def sendFormatedEmail(cls, subject = 'subject',  toAdress = 'email@gmail.com', ):
        #create msg object
        
        with open('./template/template.html', 'r') as f:
            content = f.read()
        #send msg
        message = Mail(
        from_email= os.environ['EMAIL'],
        to_emails= toAdress,
        subject= subject,
        html_content=str(content))
        try:
            sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(str(e))

    @classmethod
    def sendEmail(cls, subject = '[ByteCraft] IdeaTech check-in protocol!',  toAdress = 'email@gmail.com', attachement = ''):

        # with open('./template/content.txt' , "rb") as file:
        #     cls.s.send(to=toAdress, subject=subject, contents = str(file.read()), attachments = attachement)
        
        cls.s.send(to=toAdress, subject=subject, 
        contents = '''Hey there,
I hope this email finds you excited to rock this weekend!

This a gentle invitation to save this QR code, for check-in purposes to access event's different activities.
Download it and keep it close!

Don't forget to bring your personal computers & gadgets.

Please accept our distinguished salutations.''',
        attachments = attachement)
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
        with open('./template/email.html', 'w') as f:
            f.write(cls.generateFormatedEmailFromTemplate(qrCodePath))