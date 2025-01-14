import asyncio
import logging
import logging.config

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

import openpyxl

from datetime import date
# Define variable to load the wookbook
wookbook = openpyxl.load_workbook("priceFromBase.xlsx")
# Define variable to read the active sheet:
worksheet = wookbook.active
name = []
price = []
first_column = worksheet['C']
second_column = worksheet['G']



current_date = date.today()
# Iterate the loop to read the cell values
# for i in range(0, first_column):
#     for col in worksheet.iter_cols(1, worksheet.max_column):
#         result.append(first_column[i].value)

def returnFlags(name):
    if 'RU' in name:
        return name.replace('RU', '🇷🇺')
    elif 'LL/A' in name:
        return name.replace('LL/A', '🇺🇸')
    elif 'EU' in name:
        return name.replace('EU', '🇪🇺')
    elif 'KZ' in name:
        return name.replace('KZ', '🇰🇿')
    elif 'AA' in name:
        return name.replace('AA', '🇦🇪')
    elif 'HN' in name:
        return name.replace('HN/A', '🇮🇳')
    elif 'HN' in name:
        return name.replace('HN', '🇮🇳')
    elif 'MY' in name:
        return name.replace('MY', '🇲🇾')
    elif 'CN' in name:
        return name.replace('CN', '🇨🇳')
    elif 'LZ' in name:
        return name.replace('LZ', '🇨🇱')
    elif 'HK' in name:
        return name.replace('HK', '🇭🇰')
    elif 'VN' in name:
        return name.replace('VN', '🇻🇳')
    elif 'CH' in name:
        return name.replace('CH', '🇨🇳')
    elif 'SA' in name:
        return name.replace('SA', '🇸🇦')
    elif 'US' in name:
        return name.replace('US', '🇺🇸')
    elif 'ZA' in name:
        return name.replace('ZA', '🇿🇦')
    elif 'AFA' in name:
        return name.replace('AFA', '🇿🇦')
    elif 'AFR' in name:
        return name.replace('AFR', '🇿🇦')
    elif 'ZD' in name:
        return name.replace('ZD', '🇪🇺')
    elif 'BA' in name:
        return name.replace('BA', '🇬🇧')
    elif 'GB' in name:
        return name.replace('GB', '🇬🇧')
    elif 'TH/A' in name:
        return name.replace('TH/A', '🇹🇭')
    elif 'J/A' in name:
        return name.replace('J/A', '🇯🇵')
    elif 'QL' in name:
        return name.replace('QL', '🇯🇵')
    elif 'UK' in name:
        return name.replace('UK', '🇬🇧')
    elif 'AF' in name:
        return name.replace('AF', '🇿🇦')
    elif 'VCA' in name:
        return name.replace('VCA', '🇨🇦')
    elif 'XA' in name:
        return name.replace('XA', '🇦🇺')
    elif 'HU' in name:
        return name.replace('HU', '🇭🇺')
    elif 'HUA' in name:
        return name.replace('HUA', '🇭🇺')
    elif 'B/A' in name:
        return name.replace('B/A', '🇬🇧')
    elif 'ZDA' in name:
        return name.replace('ZDA', '🇪🇺')
    elif 'AH' in name:
        return name.replace('AH', '🇦🇪')
    elif 'KG/A' in name:
        return name.replace('KG/A', '🇪🇺')
    elif 'AN/A' in name:
        return name.replace('AN/A', '🇯🇴')
    elif 'ZP/A' in name:
        return name.replace('ZP/A', '🇭🇰')
    elif 'TN/A' in name:
        return name.replace('TN/A', '🇻🇳')
    elif 'TW' in name:
        return name.replace('TW', '🇹🇼')
    elif 'TW/A' in name:
        return name.replace('TW/A', '🇹🇼')
    elif 'VC/A' in name:
        return name.replace('VC/A', '🇨🇦')
    elif 'HX/A' in name:
        return name.replace('HX/A', '🇦🇿')
    elif 'PY' in name:
        return name.replace('PY', '🇦🇪')
    elif 'JP' in name:
        return name.replace('JP', '🇯🇵')
    elif 'QN/A' in name:
        return name.replace('QN/A', '🇪🇺')
    elif 'SG' in name:
        return name.replace('SG', '🇸🇬')
    elif 'BE/A' in name:
        return name.replace('BE/A', '🇧🇷')
    else:
        return f'{name} - '

def returnCurrentDay(date):
    if len(str(date.day)) < 2:
        return f'0{date.day}'
    else:
        return date.day

def returnCurrentMonth(date):
    if len(str(date.month)) < 2:
        return f'0{date.month}'
    else:
        return date.month

def returnHeader():
    txt = (f'{returnCurrentDay(current_date)}.{returnCurrentMonth(current_date)}.{current_date.year}'
            '\n🧑‍💻Работаем с 9:00 до 20:00'
            '\n🚀Доставка'
            '\n❗️В наличии в Севастополе'
            '\n💸Оплата наличными при получении'
            '\n'
            '\n💬ДЛЯ ЗАКАЗА💬'
            '\n📞 WhatsApp: https://wa.me/79787922235')
    return txt

for x in range(len(first_column)): 
    if first_column[x].value:
        if second_column[x].value is not None and second_column[x].value != "Опт" and first_column[x].value != "Наименование":
            name.append(f'{returnFlags(first_column[x].value)}{second_column[x].value}')


BOT_TOKEN = '7797795450:AAGS2CY8V0D6lhK9FHfU8afMbWx40PEOctY'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

removeDouble = list(dict.fromkeys(name))

def baseFix(name):
    if ('Пломба' not in name and 'Обменка' not in name and '"A' not in name and '"B' not in name 
        and '"C' not in name and '""' not in name and '"обменка' not in name and 'Демо' not in name):
        return name

def getApple(a):
    isAppleiPhone = False
    
    isAppleWatchSE2023 = False
    isAppleWatchS8 = False
    isAppleWatchS9 = False
    isAppleWatchS10 = False
    isAppleWatchUltra = False
    
    isAppleiPad = False
    isAppleMacbook = False
    isAppleiMac = False
    #################
    res = []
    res.append("📲 **Apple**")
    for i in a:
        if ("AirPods" in i or 'Apple Magic' in i or 'Apple Battery' in i or 'Apple TV' in i or 'Apple HomePod' in i or 'Apple AirTag' in i) and baseFix(i):
            res.append(i)
    #######################
    for i in a:
        if "iPhone" in i and baseFix(i):
            isAppleiPhone = True
    if isAppleiPhone is True:
        res.append("")
        res.append("📲 **Apple iPhone**")
    for i in a:
        if "iPhone" in i and baseFix(i):
            res.append(i)
    #######################
    for i in a:
        if ("SE 2023 Gen" in i or "Watch SE 2023" in i) and baseFix(i):
            isAppleWatchSE2023 = True   
    if isAppleWatchSE2023 is True:
        res.append("")
        res.append("⌚️ **Apple Watch SE 2023**")
    for i in a:
        if ("SE 2023 Gen" in i or "Watch SE 2023" in i) and baseFix(i):
            res.append(i)
    #######################    
    for i in a:
        if ("Apple Watch S8" in i) and baseFix(i):
            isAppleWatchS8 = True   
    if isAppleWatchS8 is True:
        res.append("")
        res.append("⌚️ **Apple Watch S8**")
    for i in a:
        if ("Apple Watch S8" in i) and baseFix(i):
            res.append(i) 
    #######################    
    for i in a:
        if ("Apple Watch S9" in i) and baseFix(i):
            isAppleWatchS9 = True   
    if isAppleWatchS9 is True:
        res.append("")
        res.append("⌚️ **Apple Watch S9**")
    for i in a:
        if ("Apple Watch S9" in i) and baseFix(i):
            res.append(i) 
    #######################    
    for i in a:
        if ("Apple Watch S10" in i) and baseFix(i):
            isAppleWatchS10 = True   
    if isAppleWatchS10 is True:
        res.append("")
        res.append("⌚️ **Apple Watch S10**")
    for i in a:
        if ("Apple Watch S10" in i) and baseFix(i):
            res.append(i) 
    #######################    
    for i in a:
        if ("Apple Watch Ultra" in i) and baseFix(i):
            isAppleWatchUltra = True   
    if isAppleWatchUltra is True:
        res.append("")
        res.append("⌚️ **Apple Watch Ultra**")
    for i in a:
        if ("Apple Watch Ultra" in i) and baseFix(i):
            res.append(i) 
    #######################    
    for i in a:
        if ("iPad" in i) and baseFix(i):
            isAppleiPad = True   
    if isAppleiPad is True:
        res.append("")
        res.append("📟 **Apple iPad**")
    for i in a:
        if ("iPad" in i) and baseFix(i):
            res.append(i)
    #######################    
    for i in a:
        if ("MacBook" in i) and baseFix(i):
            isAppleMacbook = True   
    if isAppleMacbook is True:
        res.append("")
        res.append("💻 **Apple MacBook**")
    for i in a:
        if ("MacBook" in i) and baseFix(i):
            res.append(i)
    #######################    
    for i in a:
        if ("iMac" in i) and baseFix(i):
            isAppleiMac = True   
    if isAppleiMac is True:
        res.append("")
        res.append("💻 **Apple iMac**")
    for i in a:
        if ("iMac" in i) and baseFix(i):
            res.append(i)
    
    return '\n'.join([str(i) for i in res])

@dp.message()
async def echo_message(message: types.Message):
    btn = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton(text='Return Price from base')]
    ])
    
    if message.text == 'Return Price from base':
        await message.answer(returnHeader(), reply_markup=btn)
        await message.answer(getApple(name), reply_markup=btn)
    # await message.answer(get(name[50:100]), reply_markup=btn)
    # await message.answer(get(name[100:150]), reply_markup=btn)
    # await message.answer(get(name[150:200]), reply_markup=btn)
    # await message.answer(get(name[200:250]), reply_markup=btn)

    
    

    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text="iPhone 11 128 Black - 35000"
    # )
    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text="Detected message...",
    #     reply_to_message_id=message.message_id
    # )
    
    # await message.reply(text=message.text)

async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())