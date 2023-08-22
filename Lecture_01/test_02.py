from zeep import Client


#### Библиотека zeep для SOAP

#### Проверка ЭЦП в SOAP

wsdl = "http://dss.cryptopro.ru/verify/service.svc?wsdl"
sign = '''

'''
client = Client(wsdl=wsdl)

def test_step1():
    assert client.service.VerifySignature('CMS', sign)['Result']
