import osa
import requests
import pprint
from xml.etree.ElementTree import fromstring

# ------------------- PART 1 -------------------
def temperature(degreeFahrenheit):
    response = requests.post(
        'http://www.webservicex.net/ConvertTemperature.asmx',
        headers={
            'Content-Type': 'text/xml; charset=utf-8'
        },
        data='''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ConvertTemp xmlns="http://www.webserviceX.NET/">
      <Temperature>''' + str(degreeFahrenheit) + '''</Temperature>
      <FromUnit>degreeFahrenheit</FromUnit>
      <ToUnit>degreeCelsius</ToUnit>
    </ConvertTemp>
  </soap:Body>
</soap:Envelope>'''
    )

    return (fromstring(response.text)[0][0][0].text)

def average_temperature(text):
    with open(text) as f:
        temperatures = []
        for line in f:
            temp = int(line.strip()[0:2])
            # print(f'{temp}°F is {(temperature(temp))[0:(len(".")+2)]}°C')
            temperatures.append(temp)
        print(f'Average temperature is {temperature(sum(temperatures)/len(temperatures))[0:4]}°C')

print('---------- PART 1 -----------')
average_temperature('temps.txt')
print('------------------------------')

# ------------------- PART 2 -------------------