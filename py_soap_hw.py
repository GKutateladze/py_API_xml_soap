import osa
import requests
import pprint
from xml.etree.ElementTree import fromstring


#------------------- PART 1 -------------------
client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')

def temperature(temp, fromUnit, toUnit):
    return client.service.ConvertTemp(temp, fromUnit, toUnit)

def average_temperature(text):
    with open(text) as f:
        temperatures = []
        for line in f:
            temp = int(line.strip()[0:2])
            # print(f'{temp}°F is {(temperature(temp))[0:(len(".")+2)]}°C')
            temperatures.append(temp)
        print(f'Average temperature is {round(int(float(temperature(sum(temperatures)/len(temperatures), "degreeFahrenheit", "degreeCelsius"))))}°C')

average_temperature('temps.txt')
print('-----------------------------')


#------------------- PART 2 -------------------
def currencies(amount, fromCurrency):
    response = requests.post(
        'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx',
        headers={
            'Content-Type': 'text/xml; charset=utf-8'
        },
        data='''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ConvertToNum xmlns="http://webservices.cloanto.com/currencyserver/">
      <licenseKey></licenseKey>
      <fromCurrency>''' + str(fromCurrency) +  '''</fromCurrency>
      <toCurrency>RUB</toCurrency>
      <amount>''' + str(amount) + '''</amount>
      <rounding>true</rounding>
      <date></date>
      <type></type>
    </ConvertToNum>
  </soap:Body>
</soap:Envelope>'''
    )

    return (fromstring(response.text)[0][0][0].text)

with open('currencies.txt') as f:
    total_flight = []
    for line in f:
        flight = (line.strip()).split(' ')
        #print(flight[0], round(int(float(currencies(flight[1], flight[2])))), 'RUB')
        total_flight.append(int(float(currencies(flight[1], flight[2]))))
    print(f'TOTAL cost: {sum(total_flight)} RUB')
    print('-----------------------------')


#------------------- PART 3 -------------------
client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')

def distance(distance, frm, to):
    return client.service.ChangeLengthUnit(distance, frm, to)


with open('travel.txt') as f:
    split_list = []
    for line in f:
        lenght = (line.strip().split(' '))
        split_list.append(lenght[1])
    real_numbers = []
    for item in split_list:
        if ',' in item:
            split = item.split(',')
            real_numbers.append(int(float(split[0]+split[1])))
        elif ',' not in item:
            real_numbers.append(int(float(item)))

    print(f'TOTAL distance: {(round((distance(sum(real_numbers), "Miles", "Kilometers")),2))} KM')
