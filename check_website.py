import requests
producturl="*****"

res =  requests.get(producturl, timeout=20)
print(res)
