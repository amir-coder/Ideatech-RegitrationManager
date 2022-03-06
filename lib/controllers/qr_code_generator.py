
from fileinput import filename
import qrcode

class QrCodeGenerator():
    exportsPath = "./exports/"
    
    
    def __init__(self):
        self.__class__.exportsPath = "./exports/"
    
    def qr_from_id(id):
        qrobj = qrcode.make(id)
        return qrobj
    
    @classmethod
    def export_img(cls, qrobj, filename = "name"):
        filename = filename + ".png"
        qrobj.save(cls.exportsPath  + filename)
    
    def generate(id, filename = 'filename'):
        qrobj = __class__.qr_from_id(id)
        __class__.export_img(qrobj, filename= filename)
