import requests
import json

key= "AIzaSyDfFjZLdqNvPtdzzEiUNcKPkq3qdfmpTug"
source="borivali"
destination="kandivali"

url="https://maps.googleapis.com/maps/api/distancematrix/json?origins="+source+"&destinations="+destination+"&key="+key
print(url)

ans=requests.get(url)
print(ans,ans.text,type(ans.text))

j_ans=json.loads(ans.text)
print(j_ans['rows'][0]['elements'][0]['distance']['text'])

if (j_ans<=1.5):
    print('cost=rs.20')
else:
    price=j_ans*12.19
    
print(price)
