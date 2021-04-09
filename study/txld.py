import requests
import json
import warnings
import re

warnings.filterwarnings('ignore')

header = 'https://txld2019.com/api/goods/listByStoreId?pageId=1&pageSize=999&storeId='
store = {

    # Diligentia
    'Diligentia_Bittern' : '2beo0f',
    'Diligentia_Buffet' : '7p4o0f',
    'Diligentia_Boiled' : 'cbeo0f',
    'Diligentia_Dry_Pot' : '0beo0f',
    'Diligentia_Spicy_Hot_Pot' : 'sbeo0f',
    'Diligentia_Night_Snack' : 'tbeo0f',
    'Diligentia_Drinks' : '1beo0f',

    # Harmonia
    'Harmonia_Grilled_Baked' : 'qesp0f',
    'Harmonia_Fastfood' : 'resp0f',
    'Harmonia_Drinks' : 'pesp0f',

    # LunaMarina
    'LunaMarina_Buffet' : '9esp0f',
    'LunaMarina_Siu_Mei' : 'fesp0f',
    'LunaMarina_Guangdong_Food' : 'mesp0f',
    'LunaMarina_Teppanyaki' : 'nesp0f',
    'LunaMarina_Drinks' : 'kesp0f',

    # Pandora
    'Pandora_Fishes' : 'gaeo0f',
    'Pandora_Donburi' : '8beo0f',
    'Pandora_Korea' : 'bbeo0f',
    'Pandora_Braised_Chicken' : '4beo0f',
    'Pandora_Fried' : '5beo0f',
    'Pandora_Guokui' : 'jaeo0f',
    'Pandora_Japanese' : '6beo0f',
    'Pandora_Rise_Noodle' : 'vbeo0f',

    # SC2/F
    'SC2/F_Siu_Mei' : '82eo0f',

    # acupofTEA
    'acupofTEA' : '0wle1f',

    # Coffee
    'Huiyin_Coffee' : 'lfoe1f',
    'Bowen_Coffee' : 'ewle1f'

}
    
#text = open('meals.txt', 'w', encoding='utf-8')
for key,value in store.items():
    url = header + value
    meal_get = requests.get(url, verify = False)
    meal_list = json.loads(meal_get.text)
    print(key)
    #text.write(key + '\n')
    for meals in meal_list['data']['list'][0]['list']:
        print(''.join(re.findall('[\u4e00-\u9fa5]',meals['goodsTitle'])))
        #text.write(meals['goodsTitle'] + '\n')
    print()
    #text.write('\n')
#text.close()
input()