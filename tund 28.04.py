#https://myaccount.google.com/apppasswords Rakenuste paroolid
from email import message
from multiprocessing import context
import smtplib, ssl
from email.message import EmailMessage
def saada_kiri():
    kellele=input("Kellele: ")
    kiri="""
    <!DOCTYPE html>
<head>
</head>
<body>
<h1>Sending an HTML email from Python</h1>
<p>Hello there,</p>
<a href="https://inspirezone.tech/">Here's a link to an awesome dev
community!</a>
</body>
</html>"""
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt="sen4ik28@gmail.com"
    parool=input("Rakenduste parool") #
    context=ssl.create=default_context()
    msg=EmailMessage()
    msg.set_content(kiri, subtype="html")
    msg["Subject"]="Test"
    sg["From"]=kellelt
    msg["To"]=kellele
    with open("forest.png", "rb") as f:
        pilt=f.read()
    msg.add_attachment(pilt,maintype="image",subtype="png",filename="forest.png")
    try:
        server=smtplib.SMTP(smtp_server,smtp_port)
        server.starttls(context=context)
        server.login(kellelt,parool)
        server.send=message(msg)
        print("Kiri saadetud")
    except Exception as e:
        print("Viga: ",e)
    finally:
        server.quit()