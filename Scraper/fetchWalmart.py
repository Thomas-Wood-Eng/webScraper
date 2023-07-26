import requests
import json
from bs4 import BeautifulSoup

cookies = {
    'localStoreInfo': 'eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9',
    'deliveryCatchment': '1061',
    'walmart.shippingPostalCode': 'L5V2N6',
    'defaultNearestStoreId': '1061',
    'vtc': 'X-kHNU-YzpqEN_s1S9N6dc',
    '_gcl_au': '1.1.149649038.1686690202',
    'walmart.id': 'de61fb8c-2df9-4149-8de0-3659ae60c63e',
    'DYN_USER_ID': 'f682a38e-5b84-4650-93f3-411bd1489b74',
    'WM_SEC.AUTH_TOKEN': 'MTAyOTYyMDE4w9wp7DeLjQBQWUugVVSsZ4hI7GCQWO/5xIkxMOJyGQY8cCVFko3qRcDsz475SM50l8QfdGDMrSvyFALHRdo05Kcdfq4mNA5xN/uKlJqle6u2+LcJszfxamCuPuZK6ZZYj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj0hZMeZoEPgyQ6o9D9kwICfo0HDBWHjT40rnfwvMubtbdkfTZGBoB3TVcVKQPAk6Enb/SoGFgAYL9DGZ8K45WCXDCcb9mgycy9jtT1uIyOBHZ7tuNselduDvcbxPJs52xgT/92ZNC3WJf6s9BNFQlHt5PM7AHv1xKbbaRXVE00exlZye7L8yYghLDNMRmsBHEu3ZM4WFXyPrNQJuUaRDK+UDXuGBdrOQ+ae6aQNvxCQ0Er1eX9YGQ0laieVMoEr348=',
    'LT': '1686690202245',
    '_ga': 'GA1.2.1735497846.1686690203',
    's_ecid': 'MCMID%7C75072090933447434350062214536000005346',
    '_cs_c': '0',
    '_fbp': 'fb.1.1686690203608.1098807550',
    '__gads': 'ID=786437f4c0ae93f3:T=1686690202:RT=1686778831:S=ALNI_Mai4hYuqUcXcodVSUx32umcMiINqA',
    '__gpi': 'UID=0000099a9eb25cc5:T=1686690202:RT=1686778831:S=ALNI_MbMj-epclTbvowOITIzqLxE2xZ8xA',
    'userSegment': '50-percent',
    'walmart.nearestLatLng': '"49.2245,-122.691"',
    'NEXT_GEN.ENABLED': '1',
    '_pxvid': 'bb2d29a4-0a2d-11ee-ae86-668dfb3b01a9',
    '_gid': 'GA1.2.276863929.1689788721',
    'kndctr_C4C6370453309C960A490D44_AdobeOrg_identity': 'CiY3NTA3MjA5MDkzMzQ0NzQzNDM1MDA2MjIxNDUzNjAwMDAwNTM0NlIOCKSKyLSLMRgBKgNPUjLwAfXVhvqWMQ==',
    'wmt.c': '0',
    'ENV': 'ak-eus-t1-prod',
    'bstc': 'XhUFdBqB8F4IuTQ5F5sV4Q',
    'xpa': '12TNt|18laY|1iNRR|20jZP|4Kq-Y|5sfML|AvWMt|G_K_Y|KX9zf|KxDCx|OAQpG|OCyta|PaKuv|Qligk|RxMsL|S2NR7|S9Aer|Sek64|VUeER|Zsz8o|cGOTQ|cMouF|fTP7G|gUGfp|hBUkh|jE0bf|qRHgs|uAQc6|uk0R3',
    'exp-ck': '12TNt118laY11iNRR120jZP15sfML1G_K_Y3KxDCx1OAQpG1Qligk1RxMsL1S2NR73S9Aer4Sek643VUeER1Zsz8o1cGOTQ1fTP7G1gUGfp1uk0R31',
    'ak_bmsc': '438AAACF58FB68E03B2CEE1F912632BE~000000000000000000000000000000~YAAQjk3bFyTvDm6JAQAASbhBcRSug2xxeVvUCKsEfPYqJZhiYBfkUWEizRLY7xSlrSWWW5lZ0Odh3/1DvftPzsPUAs/0EYNrBuPjO4tv8WQryFcJvNBVw4hHwXOhyHGL9k8Cpv8oLXev//k8Y7CfuoM+RqQNWoqY5r6nAk0xtusDGaX4Mb2/dlZ1uhhfCuPctxjPyWQV99Ksmey5NV+8rMupfh0tzW7oq9zA2X5soA+qsixUrHMTkdIW1xLmJQEwpHz6kjQUxzWROYbalX371LUT+G6cgqEErxbphF42XpP9rC9g4pOJRSf/bdDiMNhGeLFXTEELyLV8FcEIsLqT0GSY3Hf1ZjYiEat3zIzfbO4Z+XiHAIAPBHeRf5WBBCHzTDMZLQxM4cBTCg==',
    '_cs_mk_aa': '0.1413512196661768_1689822277466',
    'pxcts': '2b0a782d-26aa-11ee-997c-634c45477163',
    '_pxff_idp_c': '1,s',
    '_uetsid': '07dcc1b0265c11ee8fae2fac44739034',
    '_uetvid': 'bb5a54b00a2d11ee892d29b6507e87ca',
    'WM.USER_STATE': 'GUEST|Guest',
    'xpm': '1%2B1689822279%2BX-kHNU-YzpqEN_s1S9N6dc~%2B0',
    '_gat': '1',
    's_visit': '1',
    'cartId': 'b3fbe170-6593-4215-9272-dcbb5aad5ef9',
    'kndctr_C4C6370453309C960A490D44_AdobeOrg_cluster': 'or2',
    'AMCVS_C4C6370453309C960A490D44%40AdobeOrg': '1',
    'AMCV_C4C6370453309C960A490D44%40AdobeOrg': '-1124106680%7CMCIDTS%7C19558%7CMCMID%7C75072090933447434350062214536000005346%7CMCAAMLH-1690427078%7C9%7CMCAAMB-1690427078%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1689829478s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0',
    's_cc': 'true',
    'headerType': 'grocery',
    'gpv_Page': 'Browse%3A%20Grocery',
    '_cs_cvars': '%7B%221%22%3A%5B%22appName%22%2C%22landing-page%22%5D%7D',
    'walmart.nearestPostalCode': 'V3Y9Z0',
    's_gnr': '1689822284293-Repeat',
    'authDuration': '{"lat":"1689822286700000","lt":"1689822286700000"}',
    'cto_bundle': '8Y5-vF9yY1JUaiUyQks1QXI2aFJzYmxFTW9FSGs4bE4yeTRVVHR6dU02JTJGODd4R2l6dHd3WlF3RzZPU1pSYUJvdFFnY05WR0dneVh6UVF1QldPVHhYUTNtZEtJZkFRMlh2U0R5Zm9mOUtUU3hLQ3lwZXQ0MktSMCUyQkdSeVgzUkVHNUdJVnA5MXBvenNGTk1HJTJGMWJMNFlWcG1WZDAxUSUzRCUzRA',
    '_cs_id': '72f4dc7a-8442-ac5e-e8d3-200930d4304b.1686690203.6.1689822284.1689822277.1.1720854203155',
    '_cs_s': '3.0.0.1689824084667',
    '_px3': '4d8abb010ef70f8d5d7fce6c492b62fd1dcf27feee9b426e9ee92925dc2e3302:jbwk/GpCYi2MbKu4+u2XrB/q06gijB+p7N5+qXS6SL/um5yenlt+Y8CpSehOe0yy8TVbcfCNhd9IGrA0AalZ8w==:1000:rZF5fszKpBat/MuMwhDfNCBVxi4Ef0KzQKP/YLSW9ke65P+xUXpFYDZZ8KfV+Vx2FP+dH1jqSV2e7TtoKErX9L8QoxpQUVS4F5airwHcvIsRVWYVo0ibv+uOFQaNx4JbZaCKEHuIyn01u9UegYTLlgiGHMmvCdCLZcfbHlGukwbZFN3Aimc44qvXwYDxoC6NHnDhkPmRXMgMDXKZppjE5A==',
    'seqnum': '14',
    'TS010110a1': '01b62b3da246bd49900856184d216a2560985ea03c0987891ed37d8908e7ba0a77c086abd7c1825e38f7d16f3e217ba92912a44f09',
    'TS01ea8d4c': '01b62b3da246bd49900856184d216a2560985ea03c0987891ed37d8908e7ba0a77c086abd7c1825e38f7d16f3e217ba92912a44f09',
    'TS0180da25': '01b62b3da246bd49900856184d216a2560985ea03c0987891ed37d8908e7ba0a77c086abd7c1825e38f7d16f3e217ba92912a44f09',
    'TSe62c5f0d027': '08a583dc17ab2000681e6fe4bc687e30b401f47bbf09c540934776733432baa12fafce8ec46db5d6081d089358113000a1c248253aa6dfd72a75fc833b5984ff5e545c5f17d0800a3022c1a49a2e82fc3061e7666c6da778460d0b803b7ecba4',
    'bm_sv': '862797DC5EC5B2B6CB7A687929C1B8D8~YAAQjk3bF4T3Dm6JAQAApN5BcRTrnzDKN0YNRXFMU6MvqGtCpeEzI1WhYP/IbmA9QYGLI2X1FhaTAMZ84M2wziHgQjkNX8/rgOW3L9Uh40Ir8I39TNaBNvqyxVNW99/s/zh72FW1FKt3nFAss2sGMRjeleLG7Bxyr8sukhkZrnTrGEf1hsTFB2TZWGe95u8uWBiRQ/UkjJYDENMRZ88mjSry+dN2cemIgKL24u4bN/8Tq4YmdLuk8RND0edihS8d/g==~1',
    '_pxde': '42d18347f8e649181cb912f0ed056e6f2968493a5ef5b7feb4ef0f2d5f96bbe0:eyJ0aW1lc3RhbXAiOjE2ODk4MjIzMDg4NjB9',
    's_sq': 'wmicanadaprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DBrowse%25253A%252520Grocery%2526link%253DCancel%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DBrowse%25253A%252520Grocery%2526pidt%253D1%2526oid%253Dfunctionhr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DFORM',
}

headers = {
    'authority': 'www.walmart.ca',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9; deliveryCatchment=1061; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; vtc=X-kHNU-YzpqEN_s1S9N6dc; _gcl_au=1.1.149649038.1686690202; walmart.id=de61fb8c-2df9-4149-8de0-3659ae60c63e; DYN_USER_ID=f682a38e-5b84-4650-93f3-411bd1489b74; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE4w9wp7DeLjQBQWUugVVSsZ4hI7GCQWO/5xIkxMOJyGQY8cCVFko3qRcDsz475SM50l8QfdGDMrSvyFALHRdo05Kcdfq4mNA5xN/uKlJqle6u2+LcJszfxamCuPuZK6ZZYj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj0hZMeZoEPgyQ6o9D9kwICfo0HDBWHjT40rnfwvMubtbdkfTZGBoB3TVcVKQPAk6Enb/SoGFgAYL9DGZ8K45WCXDCcb9mgycy9jtT1uIyOBHZ7tuNselduDvcbxPJs52xgT/92ZNC3WJf6s9BNFQlHt5PM7AHv1xKbbaRXVE00exlZye7L8yYghLDNMRmsBHEu3ZM4WFXyPrNQJuUaRDK+UDXuGBdrOQ+ae6aQNvxCQ0Er1eX9YGQ0laieVMoEr348=; LT=1686690202245; _ga=GA1.2.1735497846.1686690203; s_ecid=MCMID%7C75072090933447434350062214536000005346; _cs_c=0; _fbp=fb.1.1686690203608.1098807550; __gads=ID=786437f4c0ae93f3:T=1686690202:RT=1686778831:S=ALNI_Mai4hYuqUcXcodVSUx32umcMiINqA; __gpi=UID=0000099a9eb25cc5:T=1686690202:RT=1686778831:S=ALNI_MbMj-epclTbvowOITIzqLxE2xZ8xA; userSegment=50-percent; walmart.nearestLatLng="49.2245,-122.691"; NEXT_GEN.ENABLED=1; _pxvid=bb2d29a4-0a2d-11ee-ae86-668dfb3b01a9; _gid=GA1.2.276863929.1689788721; kndctr_C4C6370453309C960A490D44_AdobeOrg_identity=CiY3NTA3MjA5MDkzMzQ0NzQzNDM1MDA2MjIxNDUzNjAwMDAwNTM0NlIOCKSKyLSLMRgBKgNPUjLwAfXVhvqWMQ==; wmt.c=0; ENV=ak-eus-t1-prod; bstc=XhUFdBqB8F4IuTQ5F5sV4Q; xpa=12TNt|18laY|1iNRR|20jZP|4Kq-Y|5sfML|AvWMt|G_K_Y|KX9zf|KxDCx|OAQpG|OCyta|PaKuv|Qligk|RxMsL|S2NR7|S9Aer|Sek64|VUeER|Zsz8o|cGOTQ|cMouF|fTP7G|gUGfp|hBUkh|jE0bf|qRHgs|uAQc6|uk0R3; exp-ck=12TNt118laY11iNRR120jZP15sfML1G_K_Y3KxDCx1OAQpG1Qligk1RxMsL1S2NR73S9Aer4Sek643VUeER1Zsz8o1cGOTQ1fTP7G1gUGfp1uk0R31; ak_bmsc=438AAACF58FB68E03B2CEE1F912632BE~000000000000000000000000000000~YAAQjk3bFyTvDm6JAQAASbhBcRSug2xxeVvUCKsEfPYqJZhiYBfkUWEizRLY7xSlrSWWW5lZ0Odh3/1DvftPzsPUAs/0EYNrBuPjO4tv8WQryFcJvNBVw4hHwXOhyHGL9k8Cpv8oLXev//k8Y7CfuoM+RqQNWoqY5r6nAk0xtusDGaX4Mb2/dlZ1uhhfCuPctxjPyWQV99Ksmey5NV+8rMupfh0tzW7oq9zA2X5soA+qsixUrHMTkdIW1xLmJQEwpHz6kjQUxzWROYbalX371LUT+G6cgqEErxbphF42XpP9rC9g4pOJRSf/bdDiMNhGeLFXTEELyLV8FcEIsLqT0GSY3Hf1ZjYiEat3zIzfbO4Z+XiHAIAPBHeRf5WBBCHzTDMZLQxM4cBTCg==; _cs_mk_aa=0.1413512196661768_1689822277466; pxcts=2b0a782d-26aa-11ee-997c-634c45477163; _pxff_idp_c=1,s; _uetsid=07dcc1b0265c11ee8fae2fac44739034; _uetvid=bb5a54b00a2d11ee892d29b6507e87ca; WM.USER_STATE=GUEST|Guest; xpm=1%2B1689822279%2BX-kHNU-YzpqEN_s1S9N6dc~%2B0; _gat=1; s_visit=1; cartId=b3fbe170-6593-4215-9272-dcbb5aad5ef9; kndctr_C4C6370453309C960A490D44_AdobeOrg_cluster=or2; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; AMCV_C4C6370453309C960A490D44%40AdobeOrg=-1124106680%7CMCIDTS%7C19558%7CMCMID%7C75072090933447434350062214536000005346%7CMCAAMLH-1690427078%7C9%7CMCAAMB-1690427078%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1689829478s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; s_cc=true; headerType=grocery; gpv_Page=Browse%3A%20Grocery; _cs_cvars=%7B%221%22%3A%5B%22appName%22%2C%22landing-page%22%5D%7D; walmart.nearestPostalCode=V3Y9Z0; s_gnr=1689822284293-Repeat; authDuration={"lat":"1689822286700000","lt":"1689822286700000"}; cto_bundle=8Y5-vF9yY1JUaiUyQks1QXI2aFJzYmxFTW9FSGs4bE4yeTRVVHR6dU02JTJGODd4R2l6dHd3WlF3RzZPU1pSYUJvdFFnY05WR0dneVh6UVF1QldPVHhYUTNtZEtJZkFRMlh2U0R5Zm9mOUtUU3hLQ3lwZXQ0MktSMCUyQkdSeVgzUkVHNUdJVnA5MXBvenNGTk1HJTJGMWJMNFlWcG1WZDAxUSUzRCUzRA; _cs_id=72f4dc7a-8442-ac5e-e8d3-200930d4304b.1686690203.6.1689822284.1689822277.1.1720854203155; _cs_s=3.0.0.1689824084667; _px3=4d8abb010ef70f8d5d7fce6c492b62fd1dcf27feee9b426e9ee92925dc2e3302:jbwk/GpCYi2MbKu4+u2XrB/q06gijB+p7N5+qXS6SL/um5yenlt+Y8CpSehOe0yy8TVbcfCNhd9IGrA0AalZ8w==:1000:rZF5fszKpBat/MuMwhDfNCBVxi4Ef0KzQKP/YLSW9ke65P+xUXpFYDZZ8KfV+Vx2FP+dH1jqSV2e7TtoKErX9L8QoxpQUVS4F5airwHcvIsRVWYVo0ibv+uOFQaNx4JbZaCKEHuIyn01u9UegYTLlgiGHMmvCdCLZcfbHlGukwbZFN3Aimc44qvXwYDxoC6NHnDhkPmRXMgMDXKZppjE5A==; seqnum=14; TS010110a1=01b62b3da246bd49900856184d216a2560985ea03c0987891ed37d8908e7ba0a77c086abd7c1825e38f7d16f3e217ba92912a44f09; TS01ea8d4c=01b62b3da246bd49900856184d216a2560985ea03c0987891ed37d8908e7ba0a77c086abd7c1825e38f7d16f3e217ba92912a44f09; TS0180da25=01b62b3da246bd49900856184d216a2560985ea03c0987891ed37d8908e7ba0a77c086abd7c1825e38f7d16f3e217ba92912a44f09; TSe62c5f0d027=08a583dc17ab2000681e6fe4bc687e30b401f47bbf09c540934776733432baa12fafce8ec46db5d6081d089358113000a1c248253aa6dfd72a75fc833b5984ff5e545c5f17d0800a3022c1a49a2e82fc3061e7666c6da778460d0b803b7ecba4; bm_sv=862797DC5EC5B2B6CB7A687929C1B8D8~YAAQjk3bF4T3Dm6JAQAApN5BcRTrnzDKN0YNRXFMU6MvqGtCpeEzI1WhYP/IbmA9QYGLI2X1FhaTAMZ84M2wziHgQjkNX8/rgOW3L9Uh40Ir8I39TNaBNvqyxVNW99/s/zh72FW1FKt3nFAss2sGMRjeleLG7Bxyr8sukhkZrnTrGEf1hsTFB2TZWGe95u8uWBiRQ/UkjJYDENMRZ88mjSry+dN2cemIgKL24u4bN/8Tq4YmdLuk8RND0edihS8d/g==~1; _pxde=42d18347f8e649181cb912f0ed056e6f2968493a5ef5b7feb4ef0f2d5f96bbe0:eyJ0aW1lc3RhbXAiOjE2ODk4MjIzMDg4NjB9; s_sq=wmicanadaprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DBrowse%25253A%252520Grocery%2526link%253DCancel%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DBrowse%25253A%252520Grocery%2526pidt%253D1%2526oid%253Dfunctionhr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DFORM',
    'referer': 'https://www.walmart.ca/cp/grocery',
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

def fetchWalmartMain(param):
    

    params = {
        'q': param,
        'c': '10019',
    }
    
    productList = []

    response = requests.get('https://www.walmart.ca/search', params=params, cookies=cookies, headers=headers)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the script tag containing the data
    script_tag = soup.find('script', text=lambda t: "__PRELOADED_STATE__" in t)

    # Extract the JSON-like data from the script tag
    data_start = script_tag.text.find("{")
    data_end = script_tag.text.rfind("}") + 1
    data = json.loads(script_tag.text[data_start:data_end])
    
    #print(data)
    
    for product_id, product_info in data["results"]["entities"]["products"].items():
        
        product = {}
        
        name = product_info["name"]
        productSize = product_info["description"]
        productID = product_info["id"]
        unit = productSize.split()
        #print(unit[1])
        
        size = {}
        
        product["name"] = name
        size["amount"] = unit[0]
        size["unit"] = unit[1]
        product["size"] = size
        product["merchant_productId"] = productID


        for sku_id, sku_info in product_info["skus"].items():
            for nested_product_info in sku_info["endecaDimensions"]:
                if nested_product_info["name"] == "Price":
                    price = nested_product_info["value"]
                if nested_product_info["name"] == "OnlineStatus":
                    onlineAvailability = nested_product_info["value"]
                if nested_product_info["name"] == "StoreStatus":
                    storeAvailability = nested_product_info["value"]
                if nested_product_info["name"] == "Brand":
                    brand = nested_product_info["value"]
                    
            

            for images in sku_info["images"]:
                image = images["thumbnail"]["url"]

        
            #print("Price:", price)
            #print("Online Availability:", onlineAvailability)
            #print("Store Availability:", storeAvailability)
            #print("Brand:", brand)
            #print("Thumbnail Image:", image)
            
        product["total_price"] = price
        product["brand"] = brand
        product["merchant"] = "Walmart"
        product["onlineAvailable"] = onlineAvailability
        product["inStoreAvailable"] = storeAvailability
        product["image_link"] = image
        product["storeID"] = ""
        product["unit_price"] = "Need exact Price"
        
        
        productList.append(product)
        
    #print(productList)
    
    return productList

fetchWalmartMain('bread')