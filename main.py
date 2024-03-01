import json
import pygsheets

client = pygsheets.authorize(service_account_file="creds.json")

spreadsheet = client.open("Pay2Games translations")
sheet = spreadsheet.sheet1

translations = {
    # 'ru': {},
    'en': {},
    'my': {},
    'id': {},
    'uzb': {},
}

def processKey(obj, keyName, value):
    # если в названии поля есть точка – генерируем еще один словарь
    if (keyName.count('.') > 0):
        key, subKey = keyName.split('.', 1)
        if (key not in obj):
            obj[key] = {}
        processKey(obj[key], subKey, value)
    else:
        obj[keyName] = value

    return obj

for row in sheet:
    key, *values = row[:6]
    values.pop(0) # удаляем RU
    
    for i, lang in enumerate(translations):
        # пропускаем 1ю строчку или строки с пустым ключом/без имени
        if key == '' or key == 'Key' or key.isnumeric():
            continue

        processKey(translations[lang], key, values[i])

with open('locales.json', 'w', encoding='utf-8') as f:
    json.dump(
        translations, 
        f, 
        ensure_ascii = False, 
        # indent=2
    )