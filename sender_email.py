import smtplib

try:
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.starttls()
    sender_email = "smartengineer0786@gmail.com"
    sender_pass = "ojsk kz tvkc"

    reciever_email = input("plz enter reciever email : ")
    subject = input("plz enter subject : ")
    body = input("plz write your message : ")
    server.login(sender_email,password=sender_pass)
    
    message = f"Subject :{subject}\n\n{body}"
    
    server.sendmail(sender_email,reciever_email,message)
    print("email successfully sent")
    server.quit()


except Exception as e:
    print(e) 