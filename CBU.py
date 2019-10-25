import httplib2 as http
import json
import requests
import dateutil.parser

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse



uri = 'http://cbu.uz/ru/arkhiv-kursov-valyut/json/'


target = urlparse(uri)
method = 'GET'
body = ''

h = http.Http()


response, currency = h.request(
        target.geturl(),
        method,
        body
      )

# assume that content is a json reply
# parse content with the json module
dataa = json.loads(currency)


urls = 'https://pmi.gov.uz/api/v3/trackor_types/CBU/trackors'
headersx = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8',
            'Authorization': 'Basic Qmlsb2xpZGRpbm5hcG06MTIzNDU2Nzg5MA=='
            }

le = len(dataa)

i = 0
while i < le:
  jsonx = '{ "fields":{ "CBU_CCY": "'+dataa[i]['Ccy']+'",'
  jsonx +='"CBU_CCYNM_EN": "'+dataa[i]['CcyNm_EN']+'",'
  jsonx +='"CBU_CCYNM_RU": "'+dataa[i]['CcyNm_RU']+'",'
  jsonx +='"CBU_CCYNM_UZ": "'+dataa[i]['CcyNm_UZ']+'",'
  jsonx +='"CBU_CODE": "'+dataa[i]['Code']+'",'
  jsonx +='"CBU_DATE": "'+str( dateutil.parser.parse(dataa[i]['Date']).date())+'",'
  jsonx +='"CBU_NOMINAL": "'+dataa[i]['Nominal']+'",'
  jsonx +='"CBU_RATE": "'+dataa[i]['Rate']+'",'
  jsonx +='"CBU_STATUS": 1  }}'
  
  answer = requests.post(urls, data=json.dumps(json.loads(jsonx)), headers=headersx)
  print(answer)
  i += 1