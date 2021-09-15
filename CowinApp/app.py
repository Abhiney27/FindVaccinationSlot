from logging import error
from flask import Flask , render_template, request
import requests
from datetime import date, datetime
from pymongo import MongoClient
app = Flask("CowinApp")
hostname = "0.0.0.0"
port = "1234"

mongo_sever_url = "mongodb://127.0.0.1:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false"
client = MongoClient(mongo_sever_url)

db = "vaccine"
collection = "users"

@app.route("/" , methods=["GET" , "POST"])
def home():
    return render_template("index.html" , out = "")

@app.route("/FindCenter" , methods = ["GET", "POST"])
def get_center():
    if request.method == "POST":
        pincode = request.form.get("pincode")
        date = request.form.get("date")
        url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}"
        response = requests.get(url)
        if response.status_code ==  200:
            global out
            out = response.json()
            return render_template("index.html" , out = out)
        elif response.status_code == 404:
            return render_template("index.html" , out = "You have entered wrong pincode")
    return render_template("index.html")

@app.route("/Alert")
def route_to_alert():
    return render_template("Alert.html")

@app.route('/alert_mail' , methods = ['Post' , 'GET'])
def send_alert_mail():
    if request.method == 'POST':
        email = request.form.get("email")
        pincode = request.form.get("pincode")
        vaccine = request.form.get("vaccine")
        fee = request.form.get("fee")
        current_date = datetime.now(IST).strftime('%d-%m-%Y')
        current_time = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')
        # date = str(current_date.day) + "-" + str(current_date.month) + "-" + str(current_date.year)
        vaccine = vaccine.upper()
        fee = fee.replace(fee[0] , fee[0].upper())
        client[db][collection].insert({"email" : email , "pincode": pincode, "vaccine_type" : vaccine, "fee_type" : fee, "RegisterTime" : current_time})
     
    return render_template("Alert.html" , alert = "You have set the alert" +"\n" + "We will update you when the slot is available(as per your preference) for you")
    # return render_template("Alert.html")

app.run(debug=True , host=hostname , port=port)
