import requests
import getpass 

def malcoreDomainCheck(domainCheck):
    url = "https://api.malcore.io/api/urlcheck"

    apikey = getpass.getpass(input="Please enter your api key: "stream=None)
    payload = {"url": domainCheck}
    headers = {
        "accept": "application/json",
        "apiKey": apikey
    }

    response = requests.request('POST',url, headers=headers, data=payload)
    r = response.json()
    data = r['data']
    
    return data
