import requests
import json

cookies = {
    'language': 'en-CA',
    '_gcl_au': '1.1.1369475709.1687037896',
    '_rdt_uuid': '1687037896435.a697989c-11d0-492e-934a-eaf4611ef2d5',
    '_tt_enable_cookie': '1',
    '_ttp': 'OmJOvCnMigkH8vZV_07xPumM8pF',
    '_pin_unauth': 'dWlkPU5USmlaR05rTnpJdE16azROQzAwTWpVMExUazVaakl0TURJellqYzFOVE5tWVRnMw',
    '__qca': 'P0-443113613-1687037896539',
    'IR_gbd': 'voila.ca',
    '_gid': 'GA1.2.1388179783.1687393169',
    'privacyAccepted': 'True',
    'IR_PI': '450d4f25-0d57-11ee-a59d-0153f21be4f3%7C1687479629836',
    '_gat_UA-139908819-1': '1',
    'AWSALB': 'bNlJs1aHrv4+V0Wt3jsuKU7uLmBg7zhYmY9bvO6MdLmtvvdmidXDdH46nNAe+rZ0giQQ/U0f3NJ/PDGrzcRU5JfFoe0E5BBeLlNVN4o3B9wHX9kqhMfXWjTnsuqv',
    'AWSALBCORS': 'bNlJs1aHrv4+V0Wt3jsuKU7uLmBg7zhYmY9bvO6MdLmtvvdmidXDdH46nNAe+rZ0giQQ/U0f3NJ/PDGrzcRU5JfFoe0E5BBeLlNVN4o3B9wHX9kqhMfXWjTnsuqv',
    'VISITORID': 'MTVkMjY5NTYtZDUxYy00NTI3LWEwMzQtYjlmODJiMmIyYmFkOjE2ODczOTQ3MDg0NTA=',
    'global_sid': 'H4sjw9Q-oMFfdK4c8FTMkOwwaJeOKCOPX5G-d8NrpV33IU1EQemP-QaYrko5ZPUzPMTjt4n6YXZnb_bR2IPNzx_9CQoDA1Bc',
    '_ga_RTNXXBP29W': 'GS1.1.1687393168.2.1.1687394709.0.0.0',
    '_ga_0BSQDG2TSQ': 'GS1.1.1687393168.2.1.1687394709.46.0.0',
    'IR_16756': '1687394709283%7C0%7C1687394709283%7C%7C',
    '_ga': 'GA1.2.800181071.1687037896',
    '_uetsid': '73d6a7e0109211ee830b3bc33f3c5342',
    '_uetvid': '44f525d00d5711ee8e26d9877f126139',
}

headers = {
    'authority': 'voila.ca',
    'accept': 'application/json; charset=utf-8',
    'accept-language': 'en-US,en;q=0.9',
    'client-route-id': '969e7904-ad63-4c7f-bec1-49b06ef051f9',
    # 'cookie': 'language=en-CA; _gcl_au=1.1.1369475709.1687037896; _rdt_uuid=1687037896435.a697989c-11d0-492e-934a-eaf4611ef2d5; _tt_enable_cookie=1; _ttp=OmJOvCnMigkH8vZV_07xPumM8pF; _pin_unauth=dWlkPU5USmlaR05rTnpJdE16azROQzAwTWpVMExUazVaakl0TURJellqYzFOVE5tWVRnMw; __qca=P0-443113613-1687037896539; IR_gbd=voila.ca; _gid=GA1.2.1388179783.1687393169; privacyAccepted=True; IR_PI=450d4f25-0d57-11ee-a59d-0153f21be4f3%7C1687479629836; _gat_UA-139908819-1=1; AWSALB=bNlJs1aHrv4+V0Wt3jsuKU7uLmBg7zhYmY9bvO6MdLmtvvdmidXDdH46nNAe+rZ0giQQ/U0f3NJ/PDGrzcRU5JfFoe0E5BBeLlNVN4o3B9wHX9kqhMfXWjTnsuqv; AWSALBCORS=bNlJs1aHrv4+V0Wt3jsuKU7uLmBg7zhYmY9bvO6MdLmtvvdmidXDdH46nNAe+rZ0giQQ/U0f3NJ/PDGrzcRU5JfFoe0E5BBeLlNVN4o3B9wHX9kqhMfXWjTnsuqv; VISITORID=MTVkMjY5NTYtZDUxYy00NTI3LWEwMzQtYjlmODJiMmIyYmFkOjE2ODczOTQ3MDg0NTA=; global_sid=H4sjw9Q-oMFfdK4c8FTMkOwwaJeOKCOPX5G-d8NrpV33IU1EQemP-QaYrko5ZPUzPMTjt4n6YXZnb_bR2IPNzx_9CQoDA1Bc; _ga_RTNXXBP29W=GS1.1.1687393168.2.1.1687394709.0.0.0; _ga_0BSQDG2TSQ=GS1.1.1687393168.2.1.1687394709.46.0.0; IR_16756=1687394709283%7C0%7C1687394709283%7C%7C; _ga=GA1.2.800181071.1687037896; _uetsid=73d6a7e0109211ee830b3bc33f3c5342; _uetvid=44f525d00d5711ee8e26d9877f126139',
    'referer': 'https://voila.ca/products/search?q=Milk',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51',
}

params = {
    'limit': '50',
    'offset': '0',
    'term': 'Bread',
}

response = requests.get('https://voila.ca/api/v5/products/search', params=params, cookies=cookies, headers=headers)


with open("fetch_safeway.json", "w") as outfile:
        json.dump(response.json(), outfile)