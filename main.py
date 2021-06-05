import requests
from requests import api



url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"

def Cowin_api(Pin_number,date,vaccine,age):
    response = requests.get(url,
        params={
            "pincode" : Pin_number,
            "date" : date,
            "vaccine" : vaccine
    })
    data = response.json()
    print("\t\tADDRESS\t\t\t\tAVAILABLE SLOTS")
    for i in range(0,len(data['sessions'])):
        if(data['sessions'][i]['available_capacity'] > 0 and data['sessions'][i]['min_age_limit'] <= age):
            print(data['sessions'][i]['address'] + "\t\t" + str(data['sessions'][i]['available_capacity']))

def User_details():
    option = input("1.COVISHIELD\n2.COVAXIN\nSelect the vaccine: ")
    Pin_number = input("enter the pin number: ")
    date = input("Enter the date: ")
    if(option == '1'):
        vaccine = "COVISHIELD"
    else:
        vaccine = "COVAXIN"
    age = int(input("Enter the minimum age: "))
    Cowin_api(Pin_number,date,vaccine,age)

if __name__ == '__main__':
   User_details()