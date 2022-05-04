import requests
from requests.structures import CaseInsensitiveDict


def call():
    url = "https://efei-dev1.fa.la1.oraclecloud.com:443/xmlpserver/services/PublicReportService";
    headers = CaseInsensitiveDict()
    headers = {'content-type': 'text/xml'}
    payload="""
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pub="http://xmlns.oracle.com/oxp/service/PublicReportService">
   <soapenv:Header/>
   <soapenv:Body>
      <pub:runReport>
         <pub:reportRequest>
        
            <pub:parameterNameValues>
               <!--Zero or more repetitions:-->
               <pub:item>         
                  <pub:name>p_invoice_id</pub:name>
                  <pub:values>
                     <!--Zero or more repetitions:-->
                     <pub:item>300000021159041</pub:item>
                  </pub:values>
               </pub:item>
            </pub:parameterNameValues>
            <pub:reportAbsolutePath>/Custom/Integration/treinamento/abg/queryInvoicesRPT.xdo</pub:reportAbsolutePath>
            <pub:sizeOfDataChunkDownload>-1</pub:sizeOfDataChunkDownload>
         </pub:reportRequest>
         <pub:userID>INT_TREINAMENTO</pub:userID>
         <pub:password>Oracle123</pub:password>
      </pub:runReport>
   </soapenv:Body>
</soapenv:Envelope>
    """;

    resp = requests.post(url, headers=headers, data=payload)

    print(resp.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    call()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
