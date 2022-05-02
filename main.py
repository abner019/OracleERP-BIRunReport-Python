import requests
from requests.structures import CaseInsensitiveDict


def call():
    url = "http://osbdev.odebrecht.com/OdbSOA-NotificationManager/NotificationManager2Port";
    headers = CaseInsensitiveDict()
    headers = {'content-type': 'text/xml'}
    payload="""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soa="http://www.odebrecht.com/soa">
           <soapenv:Header/>
           <soapenv:Body>
              <soa:getSoaInterface>
                 <!--Optional:-->
                 <eventName>xxod.psft_classif_cont_mwd_ret</eventName>
                 <!--eventName>xxod.mwd_xml_Lamborghini_dfe</eventName-->
              </soa:getSoaInterface>
           </soapenv:Body>
        </soapenv:Envelope>    
    """;

    resp = requests.post(url, headers=headers, data=payload)

    print(resp.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    call()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
