import requests
try:
    response = requests.get('http://pudim.com.br')

except:
    print("\33[31mO site está inacessível no momento! \33[m")
else:
    print("\33[32mSite em perfeito funcionamento\33[m")
    