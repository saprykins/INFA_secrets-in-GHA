import requests
import os

# URL = os.environ['IICS_LOGIN_URL']
# USERNAME = os.environ['IICS_USERNAME']
# PASSWORD = os.environ['IICS_PASSWORD']

user_name = os.environ.get('IICS_USERNAME')
# user_name = "TestServiceAccount_cicd"
# user_password = os.environ['IICS_PASSWORD']
user_password = os.environ.get('IICS_PASSWORD')
# user_password = "***"

# LOGIN TO INFA

# is used to get icSessionId
url = 'https://dm-em.informaticacloud.com/ma/api/v2/user/login'

myobj = {
    "@type":"login",
    "username":user_name,
    "password": user_password
}

# x is response from INFA
x = requests.post(url, json = myobj)

# make response as json to be able to read as dictionary
json_obj = x.json()

# informatica session id
session_id = json_obj["icSessionId"]
print(session_id)

