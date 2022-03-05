
import qrcode

class Generator():
    exportsPath = "./exports"
    
    
    def __init__(self):
        self.__class__.exportsPath = "./exports/"
    
    def qr_from_id(self, id):
        qrobj = qrcode.make(id)
        return qrobj
    
    @classmethod
    def export_img(cls, qrobj, filename = "name"):
        filename = filename + ".png"
        qrobj.save(cls.exportsPath + filename)
    
    def generate(self, ids = []):

        for id in ids:
            qrobj = self.qr_from_id(id)
            self.export_img(qrobj, id)
