import requests # requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

tempJson = rjson['RealtimeCityAir']['row']
print(tempJson)

for json in tempJson:
    print(json['IDEX_MVL'])