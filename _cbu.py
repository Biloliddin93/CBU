import requests
import onevizion
import datetime
import json

with open('settings.json', 'rb') as PFile:
    password_data = json.loads(PFile.read().decode('utf-8'))

url = password_data['URLSITE']
login = password_data['UserName']
password = password_data['Password']

cbu_list_request = onevizion.Trackor(trackorType='CBU', URL=url, userName=UserName, password=Password)

headers = {'Content-type':'application/json','Content-Encoding':'utf-8'}
url_cbu = 'http://cbu.uz/ru/arkhiv-kursov-valyut/json/'
answer = requests.get(url_cbu, headers=headers)
response = answer.json()

for data in response:
    cbu_list_request.create(
        fields={'CBU_CCY':data['Ccy'],
                'CBU_CCYNM_EN':data['CcyNm_EN'],
                'CBU_CCYNM_RU':data['CcyNm_RU'],
                'CBU_CCYNM_UZ':data['CcyNm_UZ'],
                'CBU_CODE':data['Code'],
                'CBU_DATE':str((datetime.datetime.now()).strftime("%Y-%m-%d")),
                'CBU_NOMINAL':data['Nominal'],
                'CBU_RATE':data['Rate'],
                'CBU_STATUS':1}
        )