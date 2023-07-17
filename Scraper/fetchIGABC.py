import requests
import json

cookies = {
    'ai_user': 'SijcaDFyu+BkFWEFkzTuTR|2023-06-22T02:09:22.603Z',
    '_gcl_au': '1.1.121533017.1687399763',
    '_gid': 'GA1.2.58434186.1687399763',
    '_gat_gtag_UA_45289020_6': '1',
    '_ga': 'GA1.2.1871665208.1687399763',
    '_gat_GKTracker': '1',
    'ai_session': 'amYoZNcAMrnUKnxUTDZEvY|1687399763808|1687399763808',
    '_ga_D2TKF4ZXY0': 'GS1.2.1687399763.1.1.1687399792.0.0.0',
    '_ga_WF5K8BB407': 'GS1.1.1687399762.1.1.1687399792.0.0.0',
}

headers = {
    'AUTH_TOKEN': 'null',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'CONNECTION_ID': 'null',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'ai_user=SijcaDFyu+BkFWEFkzTuTR|2023-06-22T02:09:22.603Z; _gcl_au=1.1.121533017.1687399763; _gid=GA1.2.58434186.1687399763; _gat_gtag_UA_45289020_6=1; _ga=GA1.2.1871665208.1687399763; _gat_GKTracker=1; ai_session=amYoZNcAMrnUKnxUTDZEvY|1687399763808|1687399763808; _ga_D2TKF4ZXY0=GS1.2.1687399763.1.1.1687399792.0.0.0; _ga_WF5K8BB407=GS1.1.1687399762.1.1.1687399792.0.0.0',
    'Origin': 'https://shop.igabc.com',
    'Referer': 'https://shop.igabc.com/port_moody',
    'SESSION_ID': 'KAboLWRnrutpvZLE8gqe9I0xN0hj8kqw0+9TCZIxF2znjzrnmkVnuzA/z7obSnAkpgMZvRg9ldhSDdlxq6QXJs6AtQOpwEHLXOayKQXP0KH4jjgW6A4AAea5uSCmlLXT+/3Hd4QRRvOFALw0YQAExvbgm0EJFl1MfB6khdkZhz3xIamK8NYimuQDh8jFdPJ8Mgv9jRuY/VAEuDIvWTKOnA==',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'SessionKey': 'c32a6eff-7aba-4494-afc7-ffa387091c3c',
    'TIMESTAMP': '1687399792914',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51',
    'appVersion': '12978',
    'chainID': 'cca333fd-ef09-4a1c-bf78-62d262ab332f',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sourcepage': '/search',
    'storeID': '5d9504ee-ff3c-4db3-aaba-d4b9f8dc723e',
}



json_data = {
    'page': 1,
    'Filters': {
        'Filters': [],
        'LastSelectedFilter': None,
        'SearchWithinTerm': None,
    },
    'orderby': 'Relevance',
}

def fetchIGABCMain(term):
    
    params = {
       'term': term,
    }

    response = requests.post(
        'https://shop.igabc.com/api/v2/products/search',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
)


    with open("fetch_IGA-BC.json", "w") as outfile:
        json.dump(response.json(), outfile)\
            
            
            

            