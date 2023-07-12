import requests
import json
from bs4 import BeautifulSoup


cookies = {
    '_gcl_au': '1.1.1318849234.1684448763',
    '_fbp': 'fb.1.1684448763236.2071813181',
    '_pin_unauth': 'dWlkPU16aGtPV1ExT0RNdE9EVmpNaTAwWWpFNUxUZ3dabUV0TXpNellqQm1aamhpT0RKbQ',
    'aam_uuid': '75161679033535892560053264526393834209',
    '_gac_UA-2936689-28': '1.1685314406.Cj0KCQjw98ujBhCgARIsAD7QeAiVGw-nSu1zLqt9gepWwvfX2zwWmDSADY-k4oSMG5pyrpZwzMEj6cwaAkPpEALw_wcB',
    '_gcl_aw': 'GCL.1685314407.Cj0KCQjw98ujBhCgARIsAD7QeAiVGw-nSu1zLqt9gepWwvfX2zwWmDSADY-k4oSMG5pyrpZwzMEj6cwaAkPpEALw_wcB',
    '_gcl_dc': 'GCL.1685314407.Cj0KCQjw98ujBhCgARIsAD7QeAiVGw-nSu1zLqt9gepWwvfX2zwWmDSADY-k4oSMG5pyrpZwzMEj6cwaAkPpEALw_wcB',
    '_gac_UA-3016345-8': '1.1685314407.Cj0KCQjw98ujBhCgARIsAD7QeAiVGw-nSu1zLqt9gepWwvfX2zwWmDSADY-k4oSMG5pyrpZwzMEj6cwaAkPpEALw_wcB',
    'CUSTOMER_SESSION_ID_COOKIE': 'https://www.saveonfoods.com|a8eb29b8-76a4-49ae-a8fa-ec84d2456f69',
    'TIMEOFFSET_COOKIE_NAME': '-420',
    'AMCVS_9C423E945A72D9EE0A495EF8%40AdobeOrg': '1',
    'AMCV_9C423E945A72D9EE0A495EF8%40AdobeOrg': '1585540135%7CMCMID%7C75355266827745344940027127943754993079%7CMCAAMLH-1688494318%7C9%7CMCAAMB-1688494318%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-2127053844%7CMCOPTOUT-1687896718s%7CNONE%7CvVersion%7C4.4.0',
    '_gaexp': 'GAX1.2.dZmklKFhRUq5r0s8maycVQ.19616.2',
    '_gid': 'GA1.2.1960613887.1687889519',
    'MI9_SHOPPING_MODE': 'pickup',
    'MI9_RSID': '1982',
    '_ga': 'GA1.2.688929380.1684448763',
    '__cf_bm': 'dq.xl24HhJjDf87ZE0Wqvm4mzuAk0WOsCz3ViJhX3R0-1687890304-0-ATzHfg2dNQSN1VCPD8OKkggDYXRaLSmMoDeCN2hZsaH9pjc4Ka5rQ+WvOAC1C4oGRkoZsTMaXovsL8IuW5j3Gion8JbdMu89Q5GYlfOfdXro',
    '_ga_ZM4WBLPQ9B': 'GS1.1.1687889518.8.1.1687890309.55.0.0',
}

headers = {
    'authority': 'www.saveonfoods.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '_gcl_au=1.1.1318849234.1684448763; _fbp=fb.1.1684448763236.2071813181; _pin_unauth=dWlkPU16aGtPV1ExT0RNdE9EVmpNaTAwWWpFNUxUZ3dabUV0TXpNellqQm1aamhpT0RKbQ; aam_uuid=75161679033535892560053264526393834209; _gac_UA-2936689-28=1.1685314406.Cj0KCQjw98ujBhCgARIsAD7QeAiVGw-nSu1zLqt9gepWwvfX2zwWmDSADY-k4oSMG5pyrpZwzMEj6cwaAkPpEALw_wcB; _gcl_aw=GCL.1685314407.Cj0KCQjw98ujBhCgARIsAD7QeAiVGw-nSu1zLqt9gepWwvfX2zwWmDSADY-k4oSMG5pyrpZwzMEj6cwaAkPpEALw_wcB; _gcl_dc=GCL.1685314407.Cj0KCQjw98ujBhCgARIsAD7QeAiVGw-nSu1zLqt9gepWwvfX2zwWmDSADY-k4oSMG5pyrpZwzMEj6cwaAkPpEALw_wcB; _gac_UA-3016345-8=1.1685314407.Cj0KCQjw98ujBhCgARIsAD7QeAiVGw-nSu1zLqt9gepWwvfX2zwWmDSADY-k4oSMG5pyrpZwzMEj6cwaAkPpEALw_wcB; CUSTOMER_SESSION_ID_COOKIE=https://www.saveonfoods.com|a8eb29b8-76a4-49ae-a8fa-ec84d2456f69; TIMEOFFSET_COOKIE_NAME=-420; AMCVS_9C423E945A72D9EE0A495EF8%40AdobeOrg=1; AMCV_9C423E945A72D9EE0A495EF8%40AdobeOrg=1585540135%7CMCMID%7C75355266827745344940027127943754993079%7CMCAAMLH-1688494318%7C9%7CMCAAMB-1688494318%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-2127053844%7CMCOPTOUT-1687896718s%7CNONE%7CvVersion%7C4.4.0; _gaexp=GAX1.2.dZmklKFhRUq5r0s8maycVQ.19616.2; _gid=GA1.2.1960613887.1687889519; MI9_SHOPPING_MODE=pickup; MI9_RSID=1982; _ga=GA1.2.688929380.1684448763; __cf_bm=dq.xl24HhJjDf87ZE0Wqvm4mzuAk0WOsCz3ViJhX3R0-1687890304-0-ATzHfg2dNQSN1VCPD8OKkggDYXRaLSmMoDeCN2hZsaH9pjc4Ka5rQ+WvOAC1C4oGRkoZsTMaXovsL8IuW5j3Gion8JbdMu89Q5GYlfOfdXro; _ga_ZM4WBLPQ9B=GS1.1.1687889518.8.1.1687890309.55.0.0',
    'referer': 'https://www.saveonfoods.com/sm/pickup/rsid/1982/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

def fetchSaveOnMain(query):

    params = {
        'q': query,
    }

    response = requests.get(
        'https://www.saveonfoods.com/sm/pickup/rsid/1982/results',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    # data_json = response.json()

    soup = BeautifulSoup(response.content, 'html.parser')

    product_list = []

    for element in soup.select('[class="AriaProductTitleParagraph--1yc7f4f jFsEKu"]'):
        splitString = element.text.split('$')
        if len(splitString) > 1:
            productName = splitString[0]
            price = splitString[1]
            product = {
                'name': productName.strip(),
                'price': price.strip()
            }
            product_list.append(product)

    data_json = json.dumps(product_list)

    with open("fetch_SaveOn2.json", "w") as outfile:
        json.dump(data_json, outfile)
