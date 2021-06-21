from flask.templating import render_template
import requests
from requests import api
from flask import Flask, request
import re

from werkzeug.utils import redirect

app = Flask(__name__)

URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"

def Cowin_api(pincode,vaccine,new_date):
    response = requests.get(URL,
        params={
            "pincode" : pincode,
            "date" : new_date,
            "vaccine" : vaccine,
            "age" : "45"
    })
    data = response.json()
    l = []
    for i in range(0,len(data['sessions'])):
        if(data['sessions'][i]['available_capacity'] > 0 and data['sessions'][i]['min_age_limit'] <= 45):
            res = (str(data['sessions'][i]['address']),str(data['sessions'][i]['available_capacity']),str(data['sessions'][i]['available_capacity_dose1']),str(data['sessions'][i]['available_capacity_dose2']))
            l.append(res)
        print(l)
    return l


@app.route('/',methods= ["GET","POST"])
def index():
    if request.method == "POST":
        vaccine = request.form["Vaccine"]
        pincode = request.form["pin_code"]
        date = request.form["Date"]
        new_date = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
        result = Cowin_api(pincode,vaccine,new_date)
        return render_template("index.html",res = result)
    else:
        return render_template("index.html")
        

if __name__ == '__main__':
    app.run(use_reloader = True,debug=True)
   