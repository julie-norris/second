# Enter your code here. Read input from STDIN. Print output to STDOUT
import requests, pprint, json
import re
import os

HTTPS_PROXY_USERNAME="US2Dq2geUCxe28VMpEdqgZ4Y"
HTTPS_PROXY_PASSWORD="9d7ce132-9fa4-406d-8344-a1ae28a3a2e4"
#os.environ['HTTPS_PROXY'] = #'https://HTTPS_PROXY_USERNAME:HTTPS_PROXY_PASSWORD@tntdaon6yff.s#andbox.verygoodproxy.com:8080'

def stored_data():
    data = {"secret":"anythingiwant"}    
    return(json.dumps(data))
    
def send_data(result):
    response = requests.post(url = "https://HTTPS_PROXY_USERNAME:HTTPS_PROXY_PASSWORD@tntdaon6yff.sandbox.verygoodproxy.com:8080", data=result, headers = {'content-type': 'application/json'})
    assert response.status_code==200
    return(response.json())

def output_data(secure_data):
    response = requests.post(url = "https://tntdaon6yff.SANDBOX.verygoodproxy.com",data=secure_data, headers = {'content-type': 'application/json'})
    assert response.status_code==200
    return(response.json())


if __name__ == '__main__':
    result=stored_data()
    print(result)
    secure_data=send_data(result)
    print(secure_data)
    output_data=output_data(secure_data)
    print(output_data)
