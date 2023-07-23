import requests
import json

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en',
    'Business-User-Agent': 'PCXWEB',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.realcanadiansuperstore.ca',
    'Referer': 'https://www.realcanadiansuperstore.ca/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Site-Banner': 'superstore',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-apikey': '1im1hL52q9xvta16GlSdYDsTsG0dmyhF',
}

def fetchSuperstoreMain(query):

    json_data = {
        'pagination': {
            'from': 0,
            'size': 48,
        },
        'banner': 'superstore',
        'cartId': '2b0481d4-4c1e-4cee-aa26-45894a1a9f4d',
        'lang': 'en',
        'date': '21062023',
        'storeId': '1077',
        'pcId': None,
        'pickupType': 'STORE',
        'term': query,
        'userData': {
            'domainUserId': '7fcbe398-1fb4-4bad-b1a2-cbd44a2bad91',
            'sessionId': '23468f0a-9513-47ef-8757-07a9d0327d7d',
        },
    }

    response = requests.post('https://api.pcexpress.ca/product-facade/v4/products/search', headers=headers, json=json_data)

    # print(response.json())

    with open("fetch_superstore.json", "w") as outfile:
        json.dump(response.json(), outfile)
        
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"pagination":{"from":0,"size":48},"banner":"superstore","cartId":"2b0481d4-4c1e-4cee-aa26-45894a1a9f4d","lang":"en","date":"21062023","storeId":"1077","pcId":null,"pickupType":"STORE","term":"milk","userData":{"domainUserId":"7fcbe398-1fb4-4bad-b1a2-cbd44a2bad91","sessionId":"23468f0a-9513-47ef-8757-07a9d0327d7d"}}'
#response = requests.post('https://api.pcexpress.ca/product-facade/v4/products/search', headers=headers, data=data)
