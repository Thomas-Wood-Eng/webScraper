import requests
import json

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en',
    'Business-User-Agent': 'PCXWEB',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.nofrills.ca',
    'Referer': 'https://www.nofrills.ca/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Site-Banner': 'nofrills',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-apikey': '1im1hL52q9xvta16GlSdYDsTsG0dmyhF',
}

def fetchNoFrillsMain(query):

    json_data = {
        'pagination': {
            'from': 0,
            'size': 48,
        },
        'banner': 'nofrills',
        'cartId': 'bf7c4cf0-e6fb-498d-a81a-47227c56c12e',
        'lang': 'en',
        'date': '02072023',
        'storeId': '7411',
        'pcId': None,
        'pickupType': 'STORE',
        'term': query,
        'userData': {
            'domainUserId': 'e996cb6e-66e5-4ae1-bfa9-76860fb67e4f',
            'sessionId': 'c67428bd-fc4f-4f72-b0da-2844705cb3b2',
        },
    }

    response = requests.post('https://api.pcexpress.ca/product-facade/v4/products/search', headers=headers, json=json_data)

    with open("fetch_nofrills.json", "w") as outfile:
        json.dump(response.json(), outfile)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"pagination":{"from":0,"size":48},"banner":"nofrills","cartId":"bf7c4cf0-e6fb-498d-a81a-47227c56c12e","lang":"en","date":"02072023","storeId":"7411","pcId":null,"pickupType":"STORE","term":"bread","userData":{"domainUserId":"e996cb6e-66e5-4ae1-bfa9-76860fb67e4f","sessionId":"c67428bd-fc4f-4f72-b0da-2844705cb3b2"}}'
#response = requests.post('https://api.pcexpress.ca/product-facade/v4/products/search', headers=headers, data=data)
