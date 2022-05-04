import requests
from requests.structures import CaseInsensitiveDict
from xml.etree import ElementTree
import base64


def call():

    ################# Declaracao de Variaveis
    encodedBase64 = '';
    decodedString = '';

    contador = 1;



    # Enpoint do Webservice SOAP
    url = "https://efei-dev1.fa.la1.oraclecloud.com:443/xmlpserver/services/PublicReportService";
    #Instanciando Header
    headers = CaseInsensitiveDict()
    #Attribuindo content-Type no Header
    headers = {'content-type': 'text/xml'}
    #Declarando Request
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
    #Enviando Request para o Webservice e guardando a responsta
    resp = requests.post(url, headers=headers, data=payload)
    #Recuperando o conteudo da resposta e guardando em um dom
    dom = ElementTree.fromstring(resp.content)
    #Declarando as namespaces utilizadas
    namespaces= {
        'soap' : 'http://schemas.xmlsoap.org/soap/envelope/',
        'a':'http://xmlns.oracle.com/oxp/service/PublicReportService'
    }
    #Recuperando valores por xpath
    reportBytes = dom.findall(
        './soap:Body'
        '/a:runReportResponse'
        '/a:runReportReturn'
        '/a:reportBytes',
        namespaces,
    )
    #Recuperand string em base64
    for reportByte in reportBytes:
        encodedBase64 = reportByte.text
    #Executando um decode
    decodedString = base64.b64decode(encodedBase64)


    print(decodedString)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    call()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
