from email.mime import base
import yagmail
import base64
with open("b.png","rb") as f:
    stri = base64.b64encode(f.read())
    print(stri)


with open("f",'w') as f:
    f.write(str(stri)[2:-1])


