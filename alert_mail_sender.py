import smtplib
from email.message import EmailMessage
from pymongo import MongoClient

def email_sender(receiver_id, name , pincode , vaccine, fee):
    mongo_server_url = "mongodb+srv://Abhiney:95958678@cluster0.nkzew.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = MongoClient(mongo_server_url)
    db = "Secrets"
    collection = "Email"
    secret = client[db][collection].find_one()
    sender_id = secret['email']
    sender_password =  secret['password']
    msg = EmailMessage()
    body = f"Hey {name} !! \n\nCongratulations you have successfully set the alert for Covid-19 Vaccination slot !!\n\nBelow are the information about the vaccination slot which you have preferred\n\nPincode: {pincode}\nVaccine : {vaccine}\nFee : {fee}\n\n We will get back to you with Vaccination slot soon.\n\nThank you."
    msg.set_content(body)
    msg['subject'] = "Available Slots"
    msg["to"] = receiver_id
    msg['from'] = sender_id
    s = smtplib.SMTP('smtp.gmail.com' , 587 )
    s.starttls()
    s.login(sender_id , sender_password)
    s.send_message(msg)
    s.quit()
