import osa
value_a = 2
value_b = 3
value_c = 4

client = osa.Client('http://www.dneonline.com/calculator.asmx?WSDL')

def function(a, b, c):
    return client.service.Multiply(
    client.service.Add(a,b),
    c
    )

print(function(1,2,3))


#     response = requests.post(
#         'http://www.dneonline.com/calculator.asmx',
#         headers = {
#             'Content-Type': 'text/xml; charset=utf-8'
#         },
#         data ='''<?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <Add xmlns="http://tempuri.org/">
#       <intA>''' + str(a) + '''</intA>
#       <intB>''' + str(b) + '''</intB>
#     </Add>
#   </soap:Body>
# </soap:Envelope>'''