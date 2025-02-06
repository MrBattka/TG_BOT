import asyncio
import logging
import logging.config

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
import aiogram.utils.markdown as md

import openpyxl

from datetime import date
# Define variable to load the wookbook
wookbook = openpyxl.load_workbook("../priceFromBase.xlsx")
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
    elif 'HN/A' in name:
        return name.replace('HN/A', '🇮🇳')
    elif 'HN' in name and 'MUHN2' not in name:
        return name.replace('HN', '🇮🇳')
    elif 'MY' in name and 'MYDA' not in name:
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
    elif 'US' in name and 'USB-C' not in name:
        return name.replace('US', '🇺🇸')
    elif 'ZA' in name:
        return name.replace('ZA', '🇿🇦')
    elif 'AFA' in name:
        return name.replace('AFA', '🇿🇦')
    elif 'AFR' in name:
        return name.replace('AFR', '🇿🇦')
    elif 'ZD/A' in name:
        return name.replace('ZD/A', '🇪🇺')
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
            '\n💬*ДЛЯ ЗАКАЗА*💬'
            '\n📞 WhatsApp: * https://wa.me/79787922235 *')
    return txt

for x in range(len(first_column)): 
    if first_column[x].value:
        if second_column[x].value is not None and second_column[x].value != "Опт" and first_column[x].value != "Наименование":
            name.append(f'{returnFlags(first_column[x].value)}{second_column[x].value}')


BOT_TOKEN = '7797795450:AAGS2CY8V0D6lhK9FHfU8afMbWx40PEOctY'
# CHANNEL_ID = -1001289177853 # TG Default
CHANNEL_ID = -1002384328012 # TG Test

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

removeDouble = list(dict.fromkeys(name))

def baseFix(name):
    if ('Пломба' not in name and 'Обменка' not in name and '"A' not in name and '"B' not in name 
        and '"C' not in name and '""' not in name and '"обменка' not in name and 'Демо' not in name):
        return name

def getApple(a):
    def fixName(name):
        replaceMacbook = name.replace("MacBook ", "")
        replaceApple = replaceMacbook.replace("Apple ", "")
        replaceWatch = replaceApple.replace("Watch ", "")
        fixUSB = replaceWatch.replace("🇺🇸B-C", 'USB-C - ')
        fixMUHN = fixUSB.replace("MU🇮🇳", 'MUHN')
        return fixMUHN.replace("iPhone ", "")
    isApple = False
        
    isAppleiPhone = False
    isiPhone11 = False
    isiPhone12 = False
    isiPhone13 = False
    isiPhone14 = False
    isiPhone15 = False
    isiPhone15Pro = False
    isiPhone15ProMax = False
    isiPhone16 = False
    isiPhone16Pro = False
    isiPhone16ProMax = False
    
    isAirPods2 = False
    isAirPodsPro2 = False
    isAirPods3 = False
    isAirPods4 = False
    
    isAppleWatchSE2023 = False
    isAppleWatchSE2024 = False
    isAppleWatchS8 = False
    isAppleWatchS9 = False
    isAppleWatchS10 = False
    isAppleWatchUltra = False
    
    isAppleiPad = False
    isAppleMacbook = False
    isAppleiMac = False
    #################
    res = []
    for i in a:
        if ('Apple Magic' in i or 'Apple Battery' in i or 'Apple TV' in i or 'Apple HomePod' in i or 'Apple AirTag' in i or 'Apple Pencil' in i) and baseFix(i):
            isApple = True
    res.append("📲 *Apple*")
    for i in a:
        if ('Apple Magic' in i or 'Apple Battery' in i or 'Apple TV' in i or 'Apple HomePod' in i or 'Apple AirTag' in i or 'Apple Pencil' in i) and baseFix(i):
            res.append(fixName(i))
            
    #######################
    for i in a:
        if "AirPods 2" in i and baseFix(i):
            isAirPods2 = True
    if isAirPods2 is True and isApple is True:
        res.append("")
    for i in a:
        if "AirPods 2" in i and baseFix(i):
            res.append(fixName(i))
            #######################
    for i in a:
        if "AirPods Pro" in i and baseFix(i):
            isAirPodsPro2 = True
    if isAirPodsPro2 is True:
        res.append("")
    for i in a:
        if "AirPods Pro" in i and baseFix(i):
            res.append(fixName(i))
            #######################
    for i in a:
        if "AirPods 3" in i and baseFix(i):
            isAirPods3 = True
    if isAirPods3 is True:
        res.append("")
    for i in a:
        if "AirPods 3" in i and baseFix(i):
            res.append(fixName(i))
            #######################
    for i in a:
        if "AirPods 4" in i and baseFix(i):
            isAirPods4 = True
    if isAirPods4 is True:
        res.append("")
    for i in a:
        if "AirPods 4" in i and baseFix(i):
            res.append(fixName(i))            

    #######################
    for i in a:
        if "iPhone" in i and baseFix(i):
            isAppleiPhone = True
    if isAppleiPhone is True:
        res.append("")
        res.append("📲 *Apple iPhone*")
            
     #######################
    for i in a:
        if "iPhone 11" in i and baseFix(i):
            isiPhone11 = True
    if isiPhone11 is True:
        res.append("")
    for i in a:
        if "iPhone 11" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone 12" in i and baseFix(i):
            isiPhone12 = True
    if isiPhone12 is True and isiPhone11 is True:
        res.append("")
    for i in a:
        if "iPhone 12" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone 13" in i and baseFix(i):
            isiPhone13 = True
    if isiPhone13 is True and (isiPhone12 is True or isiPhone11 is True):
        res.append("")
    for i in a:
        if "iPhone 13" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone 14" in i and baseFix(i):
            isiPhone14 = True
    if isiPhone14 is True and (isiPhone13 is True or isiPhone12 is True or isiPhone11 is True):
        res.append("")
    for i in a:
        if "iPhone 14" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone 15" in i and "iPhone 15 Pro" not in i and baseFix(i):
            isiPhone15 = True
    if isiPhone15 is True and (isiPhone14 is True or isiPhone13 is True or isiPhone12 is True or isiPhone11 is True):
        res.append("")
    for i in a:
        if "iPhone 15" in i and baseFix(i):
            res.append(fixName(i))
            
    #######################
    for i in a:
        if "iPhone 15 Pro" in i and "iPhone 15 Pro Max" not in i and baseFix(i):
            isiPhone15Pro = True
    if (isiPhone15Pro is True and (isiPhone15 is True or isiPhone14 is True or isiPhone13 is True or 
        isiPhone12 is True or isiPhone11 is True)):
        res.append("")
    for i in a:
        if "iPhone 15 Pro" in i and baseFix(i):
            res.append(fixName(i)) 
    #######################
    for i in a:
        if "iPhone 15 Pro Max" in i and baseFix(i):
            isiPhone15ProMax = True
    if (isiPhone15ProMax is True and (isiPhone15Pro is True or isiPhone15 is True or isiPhone14 is True or 
        isiPhone13 is True or isiPhone12 is True or isiPhone11 is True)):
        res.append("")
    for i in a:
        if "iPhone 15 Pro Max" in i and baseFix(i):
            res.append(fixName(i))
     #######################
    for i in a:
        if "iPhone 16" in i and "iPhone 16 Pro" not in i and baseFix(i):
            isiPhone16 = True
    if (isiPhone16 is True and (isiPhone15ProMax is True or isiPhone15Pro is True or isiPhone15 is True or 
        isiPhone14 is True or isiPhone13 is True or isiPhone12 is True or isiPhone11 is True)):
        res.append("")
    for i in a:
        if "iPhone 16" in i and "iPhone 16 Pro" not in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone 16 Pro" in i and "iPhone 16 Pro Max" not in i and baseFix(i):
            isiPhone16Pro = True
    if (isiPhone16Pro is True and (isiPhone16 is True or isiPhone15ProMax is True or isiPhone15Pro is True or isiPhone15 is True or 
        isiPhone14 is True or isiPhone13 is True or isiPhone12 is True or isiPhone11 is True)):
        res.append("")
    for i in a:
        if "iPhone 16 Pro" in i and "iPhone 16 Pro Max" not in i and baseFix(i):
            res.append(fixName(i)) 
    #######################
    for i in a:
        if "iPhone 16 Pro Max" in i and baseFix(i):
            isiPhone16ProMax = True
    if (isiPhone16ProMax is True and (isiPhone16Pro is True or isiPhone16 is True or isiPhone15ProMax is True or isiPhone15Pro is True 
        or isiPhone15 is True or isiPhone14 is True or isiPhone13 is True or isiPhone12 is True or isiPhone11 is True)):
        res.append("")
    for i in a:
        if "iPhone 16 Pro Max" in i and baseFix(i):
            res.append(fixName(i))    
            
            
    #######################
    for i in a:
        if ("SE 2023 Gen" in i or "Watch SE 2023" in i) and baseFix(i):
            isAppleWatchSE2023 = True   
    if isAppleWatchSE2023 is True:
        res.append("")
        res.append("⌚️ *Apple Watch SE 2023*")
    for i in a:
        if ("SE 2023 Gen" in i or "Watch SE 2023" in i) and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if ("SE 2024 Gen" in i or "Watch SE 2024" in i) and baseFix(i):
            isAppleWatchSE2024 = True   
    if isAppleWatchSE2024 is True:
        res.append("")
        res.append("⌚️ *Apple Watch SE 2024*")
    for i in a:
        if ("SE 2024 Gen" in i or "Watch SE 2024" in i) and baseFix(i):
            res.append(fixName(i))
    #######################    
    for i in a:
        if ("Apple Watch S8" in i) and baseFix(i):
            isAppleWatchS8 = True   
    if isAppleWatchS8 is True:
        res.append("")
        res.append("⌚️ *Apple Watch S8*")
    for i in a:
        if ("Apple Watch S8" in i) and baseFix(i):
            res.append(fixName(i)) 
    #######################    
    for i in a:
        if ("Apple Watch S9" in i) and baseFix(i):
            isAppleWatchS9 = True   
    if isAppleWatchS9 is True:
        res.append("")
        res.append("⌚️ *Apple Watch S9*")
    for i in a:
        if ("Apple Watch S9" in i) and baseFix(i):
            res.append(fixName(i)) 
    #######################    
    for i in a:
        if ("Apple Watch S10" in i) and baseFix(i):
            isAppleWatchS10 = True   
    if isAppleWatchS10 is True:
        res.append("")
        res.append("⌚️ *Apple Watch S10*")
    for i in a:
        if ("Apple Watch S10" in i) and baseFix(i):
            res.append(fixName(i)) 
    #######################    
    for i in a:
        if ("Apple Watch Ultra" in i) and baseFix(i):
            isAppleWatchUltra = True   
    if isAppleWatchUltra is True:
        res.append("")
        res.append("⌚️ *Apple Watch Ultra*")
    for i in a:
        if ("Apple Watch Ultra" in i) and baseFix(i):
            res.append(fixName(i)) 
    #######################    
    for i in a:
        if ("iPad" in i) and baseFix(i):
            isAppleiPad = True   
    if isAppleiPad is True:
        res.append("")
        res.append("📟 *Apple iPad*")
    for i in a:
        if ("iPad" in i) and baseFix(i):
            res.append(fixName(i))
    #######################    
    for i in a:
        if ("MacBook" in i) and baseFix(i):
            isAppleMacbook = True   
    if isAppleMacbook is True:
        res.append("")
        res.append("💻 *Apple MacBook*")
    for i in a:
        if ("MacBook" in i) and baseFix(i):
            res.append(fixName(i))
    #######################    
    for i in a:
        if ("iMac" in i) and baseFix(i):
            isAppleiMac = True   
    if isAppleiMac is True:
        res.append("")
        res.append("💻 *Apple iMac*")
    for i in a:
        if ("iMac" in i) and baseFix(i):
            res.append(fixName(i))
    
    return '\n'.join([str(i) for i in res])

def getSamsung(a):
    def fixName(name):
        return name.replace("Samsung Galaxy", '')
    
    isGalaxyPhone = False
    
    isGalaxyA05 = False
    isGalaxyA06 = False
    isGalaxyA15 = False
    isGalaxyA16 = False
    isGalaxyA25 = False
    isGalaxyA35 = False
    isGalaxyA53 = False
    isGalaxyA55 = False
    isGalaxyS22 = False
    isGalaxyS23 = False
    isGalaxyS23Plus = False
    isGalaxyS23FE = False
    isGalaxyS23Ultra = False
    isGalaxyS24 = False
    isGalaxyS24Plus = False
    isGalaxyS24FE = False
    isGalaxyS24Ultra = False
    isGalaxyZFlip5 = False
    isGalaxyZFlip6 = False
    isGalaxyZFold5 = False
    isGalaxyZFold6 = False
    
    
    isGalaxyTab = False
    #################
    res = []
    for i in a:
        if "Samsung Galaxy" in i and 'Galaxy Tab' not in i and baseFix(i):
            isGalaxyPhone = True
    if isGalaxyPhone is True:
        res.append("📲 *Samsung Galaxy*")
    #######################
    for i in a:
        if "Samsung Galaxy A05" in i and baseFix(i):
            isGalaxyA05 = True
    if isGalaxyA05 is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy A05" in i and baseFix(i):
            res.append(fixName(i))
            
    #######################
    for i in a:
        if "Samsung Galaxy A06" in i and baseFix(i):
            isGalaxyA06 = True
    if isGalaxyA06 is True and isGalaxyA05 is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy A06" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy A15" in i and baseFix(i):
            isGalaxyA15 = True
    if isGalaxyA15 is True and (isGalaxyA06 is True or isGalaxyA05 is True):
        res.append("")
    for i in a:
        if "Samsung Galaxy A15" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy A16" in i and baseFix(i):
            isGalaxyA16 = True
    if isGalaxyA16 is True and (isGalaxyA15 is True or isGalaxyA06 is True or isGalaxyA05 is True):
        res.append("")
    for i in a:
        if "Samsung Galaxy A16" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy A25" in i and baseFix(i):
            isGalaxyA25 = True
    if isGalaxyA25 is True and (isGalaxyA16 is True or isGalaxyA15 is True or isGalaxyA06 is True or isGalaxyA05 is True):
        res.append("")
    for i in a:
        if "Samsung Galaxy A25" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy A35" in i and baseFix(i):
            isGalaxyA35 = True
    if (isGalaxyA35 is True and (isGalaxyA25 is True or isGalaxyA16 is True or isGalaxyA15 is True or isGalaxyA06 is True 
                                                     or isGalaxyA05 is True)):
        res.append("")
    for i in a:
        if "Samsung Galaxy A35" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy A53" in i and baseFix(i):
            isGalaxyA53 = True
    if (isGalaxyA53 is True and (isGalaxyA35 is True or isGalaxyA25 is True or isGalaxyA16 is True or isGalaxyA15 is True  
                                                     or isGalaxyA05 is True or isGalaxyA06 is True)):
        res.append("")
    for i in a:
        if "Samsung Galaxy A53" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy A55" in i and baseFix(i):
            isGalaxyA55 = True
    if (isGalaxyA55 is True and (isGalaxyA53 is True or isGalaxyA35 is True or isGalaxyA25 is True or isGalaxyA16 is True or isGalaxyA15 is True  
                                                     or isGalaxyA05 is True or isGalaxyA06 is True)):
        res.append("")
    for i in a:
        if "Samsung Galaxy A55" in i and baseFix(i):
            res.append(fixName(i))
            
    #######################
    for i in a:
        if "Samsung Galaxy S22" in i and baseFix(i):
            isGalaxyS22 = True
    if isGalaxyS22 is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S22" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy S23" in i and "Samsung Galaxy S23 Ultra" not in i and "Samsung Galaxy S23 FE" not in i and "Samsung Galaxy S23+" not in i and baseFix(i):
            isGalaxyS23 = True
    if isGalaxyS23 is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S23" in i and "Samsung Galaxy S23 Ultra" not in i and "Samsung Galaxy S23 FE" not in i and "Samsung Galaxy S23+" not in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy S23+" in i and baseFix(i):
            isGalaxyS23Plus = True
    if isGalaxyS23Plus is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S23+" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy S23 FE" in i and baseFix(i):
            isGalaxyS23FE = True
    if isGalaxyS23FE is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S23 FE" in i and baseFix(i):
            res.append(fixName(i))
   #######################
    for i in a:
        if "Samsung Galaxy S23 Ultra" in i and baseFix(i):
            isGalaxyS23Ultra = True
    if isGalaxyS23Ultra is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S23 Ultra" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy S24" in i and "Samsung Galaxy S24 Ultra" not in i and "Samsung Galaxy S24 FE" not in i and "Samsung Galaxy S24+" not in i and baseFix(i):
            isGalaxyS24 = True
    if isGalaxyS24 is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S24" in i and "Samsung Galaxy S24 Ultra" not in i and "Samsung Galaxy S24 FE" not in i and "Samsung Galaxy S24+" not in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy S24 FE" in i and baseFix(i):
            isGalaxyS24FE = True
    if isGalaxyS24FE is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S24 FE" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy S24+" in i and baseFix(i):
            isGalaxyS24Plus = True
    if isGalaxyS24Plus is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S24+" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy S24 Ultra" in i and baseFix(i):
            isGalaxyS24Ultra = True
    if isGalaxyS24Ultra is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S24 Ultra" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy Z Flip 5" in i and baseFix(i):
            isGalaxyZFlip5 = True
    if isGalaxyZFlip5 is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy Z Flip 5" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy Z Flip 6" in i and baseFix(i):
            isGalaxyZFlip6 = True
    if isGalaxyZFlip6 is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy Z Flip 6" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy Z Fold 5" in i and baseFix(i):
            isGalaxyZFold5 = True
    if isGalaxyZFold5 is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy Z Fold 5" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy Z Fold 6" in i and baseFix(i):
            isGalaxyZFold6 = True
    if isGalaxyZFold6 is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy Z Fold 6" in i and baseFix(i):
            res.append(fixName(i))
            
            
    #######################
    for i in a:
        if "Galaxy Tab" in i and baseFix(i):
            isGalaxyTab = True
    if isGalaxyTab is True:
        res.append('')
        res.append("📟 *Galaxy Tab*")
    for i in a:
        if ('Galaxy Tab' in i) and baseFix(i):
            res.append(i)
    
    return '\n'.join([str(i) for i in res])

def getCoros(a):
    def fixName(name):
        replaceAsus = name.replace("Asus ", '')
        replaceCoros = replaceAsus.replace("Coros ", '')
        replaceSony = replaceCoros.replace("Sony ", '')
        replaceOnePlus = replaceSony.replace("OnePlus ", '')
        replaceZTE = replaceOnePlus.replace("ZTE ", '')
        return replaceZTE.replace("Dyson ", '')
    
    isHuawei = False
    isCoros = False
    isGoogle = False
    isPS = False
    isGoPro = False
    isFinis = False
    isAsus = False
    isNothing = False
    isOnePlus = False
    isZTE = False
    isDyson = False
    isSony = False
    #################
    res = []
    for i in a:
        if "Huawei" in i and baseFix(i):
            isHuawei = True
    if isHuawei is True:
        res.append("📲 *Huawei*")
    for i in a:
        if "Huawei" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if ('Coros' in i or 'COROS' in i) and baseFix(i):
            isCoros = True
    if isCoros is True:
        res.append('')
        res.append("📲 *Coros*")
    for i in a:
        if ('Coros' in i or 'COROS' in i) and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Google" in i and baseFix(i):
            isGoogle = True
    if isGoogle is True:
        res.append('')
        res.append("📲 *Google*")
    for i in a:
        if 'Google' in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if ("PlayStation" in i or "DualSense" in i or "Xbox" in i) and baseFix(i):
            isPS = True
    if isPS is True:
        res.append('')
        res.append("🎮 *Playstation / Xbox* 🎮")
    for i in a:
        if ("PlayStation" in i or "DualSense" in i or "Xbox" in i) and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if ("GoPro" in i or "Protective" in i or "El Grande" in i or '3-Way' in i) and baseFix(i):
            isGoPro = True
    if isGoPro is True:
        res.append('')
        res.append("📹 *GoPro*")
    for i in a:
        if ("GoPro" in i or "Protective" in i or "El Grande" in i or '3-Way' in i) and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Finis" in i and baseFix(i):
            isFinis = True
    if isFinis is True:
        res.append('')
        res.append("📲 *Finis*")
    for i in a:
        if "Finis" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Asus" in i and baseFix(i):
            isAsus = True
    if isAsus is True:
        res.append('')
        res.append("📲 *Asus*")
    for i in a:
        if "Asus" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Nothing" in i and baseFix(i):
            isNothing = True
    if isNothing is True:
        res.append('')
        res.append("📲 *Nothing Phone*")
    for i in a:
        if "Nothing" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "OnePlus" in i and baseFix(i):
            isOnePlus = True
    if isOnePlus is True:
        res.append('')
        res.append("📲 *OnePlus*")
    for i in a:
        if "OnePlus" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "ZTE" in i and baseFix(i):
            isZTE = True
    if isZTE is True:
        res.append('')
        res.append("📲 **ZTE**")
    for i in a:
        if "ZTE" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Dyson" in i and baseFix(i):
            isDyson = True
    if isDyson is True:
        res.append('')
        res.append("📲 *Dyson*")
    for i in a:
        if "Dyson" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Xperia" in i and baseFix(i):
            isSony = True
    if isSony is True:
        res.append('')
        res.append("📲 *Sony*")
    for i in a:
        if "Xperia" in i and baseFix(i):
            res.append(fixName(i))
    
    return '\n'.join([str(i) for i in res])

def getXiaomiYandexJBL(a):
    def fixName(name):
        fixPoco = name.replace("Pocophone", 'Poco')
        replaceRedmi = fixPoco.replace("Redmi Note", 'Note')
        fixMI = replaceRedmi.replace("Xiaomi 1", 'Mi 1')
        return fixMI.replace("Xiaomi ", '')
    
    isXiaomi = False
    isPocophone = False
    isYandex = False
    isJBL = False
    isShokz = False
    
    isMiTV = False
    isXiaomi12 = False
    isXiaomi13 = False
    isXiaomi14 = False
    isXiaomiRedmi12 = False
    isXiaomiRedmi13 = False
    isXiaomiRedmi14 = False
    isXiaomiNote13 = False
    isXiaomiNote13Pro4G = False
    isXiaomiNote13Pro5G = False
    isXiaomiNote13ProPlus = False
    isXiaomiNote14 = False
    isXiaomiNote14Pro4G = False
    isXiaomiNote14Pro5G = False
    isXiaomiNote14ProPlus = False
    isPocoC61 = False
    isPocoC65 = False
    isPocoC75 = False
    isPocoM5 = False
    isPocoM6 = False
    isPocoF6 = False
    isPocoX5 = False
    isPocoX6 = False
    #################
    res = []
    for i in a:
        if "Xiaomi" in i and baseFix(i):
            isXiaomi = True
    if isXiaomi is True:
        res.append("📲 *Xiaomi*")
    #######################
    for i in a:
        if "MI TV" in i and baseFix(i):
            isMiTV = True      
    for i in a:
        if "MI TV" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Redmi 12" in i and baseFix(i):
            isXiaomiRedmi12 = True
    if isXiaomiRedmi12 is True:
        res.append("")
    for i in a:
        if "Redmi 12" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Redmi 13" in i and baseFix(i):
            isXiaomiRedmi13 = True
    if isXiaomiRedmi13 is True and (isXiaomiRedmi12 is True or isMiTV is True):
        res.append("")
    for i in a:
        if "Redmi 13" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Redmi 14" in i and baseFix(i):
            isXiaomiRedmi14 = True
    if isXiaomiRedmi14 is True and (isXiaomiRedmi13 is True or isXiaomiRedmi12 is True or isMiTV is True):
        res.append("")
    for i in a:
        if "Redmi 14" in i and baseFix(i):
            res.append(fixName(i))
            
    #######################        
    for i in a:
        if "Redmi Note 13" in i and "Redmi Note 13 Pro" not in i and baseFix(i):
            isXiaomiNote13 = True
    if isXiaomiNote13 is True and (isXiaomiRedmi14 is True or isXiaomiRedmi13 is True or isXiaomiRedmi12 is True or isMiTV is True):
        res.append("")
    for i in a:
        if "Redmi Note 13" in i and "Redmi Note 13 Pro" not in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Redmi Note 13 Pro 4G" in i and baseFix(i):
            isXiaomiNote13Pro4G = True
    if (isXiaomiNote13Pro4G is True and (isXiaomiNote13 is True or isXiaomiRedmi14 is True or isXiaomiRedmi13 is True 
                                                                    or isXiaomiRedmi12 is True or isMiTV is True)):
        res.append("")
    for i in a:
        if "Redmi Note 13 Pro 4G" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Redmi Note 13 Pro 5G" in i and baseFix(i):
            isXiaomiNote13Pro5G = True
    if (isXiaomiNote13Pro5G is True and (isXiaomiNote13Pro4G is True or isXiaomiNote13 is True or isXiaomiRedmi14 is True 
                                         or isXiaomiRedmi13 is True or isXiaomiRedmi12 is True or isMiTV is True)):
        res.append("")
    for i in a:
        if "Redmi Note 13 Pro 5G" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Redmi Note 13 Pro Plus" in i and baseFix(i):
            isXiaomiNote13ProPlus = True
    if (isXiaomiNote13ProPlus is True and (isXiaomiNote13Pro5G is True or isXiaomiNote13Pro4G is True or isXiaomiNote13 is True  
                                         or isXiaomiRedmi13 is True or isXiaomiRedmi12 is True or isMiTV is True or isXiaomiRedmi14 is True)):
        res.append("")
    for i in a:
        if "Redmi Note 13 Pro Plus" in i and baseFix(i):
            res.append(fixName(i))
            
    #######################        
    for i in a:
        if "Redmi Note 14" in i and "Redmi Note 14 Pro" not in i and baseFix(i):
            isXiaomiNote14 = True
    if isXiaomiNote14 is True:
        res.append("")
    for i in a:
        if "Redmi Note 14" in i and "Redmi Note 14 Pro" not in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Redmi Note 14 Pro 4G" in i and baseFix(i):
            isXiaomiNote14Pro4G = True
    if isXiaomiNote14Pro4G is True:
        res.append("")
    for i in a:
        if "Redmi Note 14 Pro 4G" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Redmi Note 14 Pro 5G" in i and baseFix(i):
            isXiaomiNote14Pro5G = True
    if isXiaomiNote14Pro5G is True:
        res.append("")
    for i in a:
        if "Redmi Note 14 Pro 5G" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Redmi Note 14 Pro Plus" in i and baseFix(i):
            isXiaomiNote14ProPlus = True
    if isXiaomiNote14ProPlus is True:
        res.append("")
    for i in a:
        if "Redmi Note 14 Pro Plus" in i and baseFix(i):
            res.append(fixName(i))
            
    #######################        
    for i in a:
        if "Xiaomi 12" in i and baseFix(i):
            isXiaomi12 = True
    if isXiaomi12 is True:
        res.append("")
    for i in a:
        if "Xiaomi 12" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Xiaomi 13" in i and baseFix(i):
            isXiaomi13 = True
    if isXiaomi13 is True:
        res.append("")
    for i in a:
        if "Xiaomi 13" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Xiaomi 14" in i and baseFix(i):
            isXiaomi14 = True
    if isXiaomi14 is True:
        res.append("")
    for i in a:
        if "Xiaomi 14" in i and baseFix(i):
            res.append(fixName(i))
    
    
    #############       
    for i in a:
        if "Pocophone" in i and baseFix(i):
            isPocophone = True
    if isPocophone is True:
        res.append("")
        res.append("📲 *Pocophone*")
    #######################        
    for i in a:
        if "Pocophone C61" in i and baseFix(i):
            isPocoC61 = True
    for i in a:
        if "Pocophone C61" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Pocophone C65" in i and baseFix(i):
            isPocoC65 = True
    if isPocoC65 is True and isPocoC61 is True:
        res.append("")
    for i in a:
        if "Pocophone C65" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Pocophone C75" in i and baseFix(i):
            isPocoC75 = True
    if isPocoC75 is True and (isPocoC65 is True or isPocoC61 is True):
        res.append("")
    for i in a:
        if "Pocophone C75" in i and baseFix(i):
            res.append(fixName(i))
            
            
    #######################        
    for i in a:
        if "Pocophone F6" in i and baseFix(i):
            isPocoF6 = True
    if isPocoF6 is True and (isPocoC75 is True or isPocoC65 is True or isPocoC61 is True):
        res.append("")
    for i in a:
        if "Pocophone F6" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Pocophone M5" in i and baseFix(i):
            isPocoM5 = True
    if isPocoM5 is True and (isPocoF6 is True or isPocoC75 is True or isPocoC65 is True or isPocoC61 is True):
        res.append("")
    for i in a:
        if "Pocophone M5" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Pocophone M6" in i and baseFix(i):
            isPocoM6 = True
    if isPocoM6 is True and (isPocoM5 is True or isPocoF6 is True or isPocoC75 is True or isPocoC65 is True or isPocoC61 is True):
        res.append("")
    for i in a:
        if "Pocophone M6" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Pocophone X5" in i and baseFix(i):
            isPocoX5 = True
    if (isPocoX5 is True and (isPocoM6 is True or isPocoM5 is True or isPocoF6 is True or isPocoC75 is True 
                              or isPocoC65 is True or isPocoC61 is True)):
        res.append("")
    for i in a:
        if "Pocophone X5" in i and baseFix(i):
            res.append(fixName(i))
    #######################        
    for i in a:
        if "Pocophone X6" in i and baseFix(i):
            isPocoX6 = True
    if (isPocoX6 is True and (isPocoX5 is True or isPocoM6 is True or isPocoM5 is True or isPocoF6 is True or isPocoC75 is True 
                              or isPocoC65 is True or isPocoC61 is True)):
        res.append("")
    for i in a:
        if "Pocophone X6" in i and baseFix(i):
            res.append(fixName(i))
            
    #######################
    for i in a:
        if "Яндекс" in i and baseFix(i):
            isYandex = True
    if isYandex is True:
        res.append('')
        res.append("🔊 *Яндекс Станция*")
    for i in a:
        if 'Яндекс' in i and baseFix(i):
            res.append(i)
    #######################
    for i in a:
        if "JBL" in i and baseFix(i):
            isJBL = True
    if isJBL is True:
        res.append('')
        res.append("🔊 *JBL*")
    for i in a:
        if 'JBL' in i and baseFix(i):
            res.append(i)
    #######################
    for i in a:
        if "Shokz" in i and baseFix(i):
            isShokz = True
    if isShokz is True:
        res.append('')
        res.append("👓 *Shokz*")
    for i in a:
        if 'Shokz' in i and baseFix(i):
            res.append(i)
    
    return '\n'.join([str(i) for i in res])

def getUsed(a):
    def checkUsed(name):
        return (
        '"A-"' in name  or
        '"A"' in name or
        '"A+"' in name  or
        '"B-"' in name  or
        '"B"' in name or
        '"B+"' in name  or
        '"C-"' in name  or
        '"C"' in name or
        '"C+"' in name 
    )
    
    def fixName(name):
        replaceAW = name.replace("Apple Watch ", '')
        replaceCoros = replaceAW.replace("Coros ", '')
        replaceApple = replaceCoros.replace("Apple ", '')
        replaceiPhone = replaceApple.replace("iPhone ", '')
        replaceMacBook = replaceiPhone.replace("MacBook ", '')
        replaceXiaomi = replaceMacBook.replace("Xiaomi Redmi", 'Redmi')
        replacePoco = replaceXiaomi.replace("Pocophone", 'Poco')
        if "Пломбa" not in replacePoco:
            return replacePoco.replace("Samsung ", '')
        else:
            return replacePoco
    
    isDemo = False
    isAWSE = False
    isAWS8 = False
    isAWS9 = False    
    isiPad = False
    isMacBook = False
    isiMac = False
    
    isiPhone = False
    isiPhone7 = False
    isiPhone8 = False
    isiPhoneSE = False
    isiPhoneX = False    
    isiPhone11 = False
    isiPhone12 = False
    isiPhone13 = False
    isiPhone14 = False
    isiPhone15 = False
    isiPhone16 = False
    
    isSams = False
    isXiaomi = False
    isOther = False
    #################
    res = []
    res.append('👇 *Идеальное БУ*')
    res.append('')
       
    res.append("🍏 *Apple*")
    for i in a:
        if ("AirPods" in i or 'Apple Magic' in i or 'Apple Battery' in i or 'Apple TV' in i or 'Apple HomePod' in i or 'Apple AirTag' in i or 'Pencil' in i)  and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone" in i and checkUsed(i):
            isiPhone = True
    if isiPhone is True:
        res.append('')
        res.append("📱 *Apple iPhone*")
            
    #######################
    for i in a:
        if "iPhone 7" in i and checkUsed(i):
            isiPhone7 = True
    for i in a:
        if 'iPhone 7' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone 8" in i and checkUsed(i):
            isiPhone8 = True
    if isiPhone8 is True and isiPhone7 is True:
        res.append('')
    for i in a:
        if 'iPhone 8' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone SE" in i and checkUsed(i):
            isiPhoneSE = True
    if isiPhoneSE is True and (isiPhone7 is True or isiPhone8 is True):
        res.append('')
    for i in a:
        if 'iPhone SE' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone X" in i and checkUsed(i):
            isiPhoneX = True
    if isiPhoneX is True and (isiPhoneSE is True or isiPhone7 is True or isiPhone8 is True):
        res.append('')
    for i in a:
        if 'iPhone X' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone 11" in i and checkUsed(i):
            isiPhone11 = True
    if isiPhone11 is True and (isiPhoneX is True or isiPhoneSE is True or isiPhone7 is True or isiPhone8 is True):
        res.append('')
    for i in a:
        if 'iPhone 11' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone 12" in i and checkUsed(i):
            isiPhone12 = True
    if isiPhone12 is True and (isiPhone11 is True or isiPhoneX is True or isiPhoneSE is True 
                               or isiPhone7 is True or isiPhone8 is True):
        res.append('')
    for i in a:
        if 'iPhone 12' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone 13" in i and checkUsed(i):
            isiPhone13 = True
    if isiPhone13 is True and (isiPhone12 is True or isiPhone11 is True or isiPhoneX is True or isiPhoneSE is True 
                               or isiPhone7 is True or isiPhone8 is True):
        res.append('')
    for i in a:
        if 'iPhone 13' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone 14" in i and checkUsed(i):
            isiPhone14 = True
    if isiPhone14 is True and (isiPhone13 is True or isiPhone12 is True or isiPhone11 is True or isiPhoneX is True 
                               or isiPhone7 is True or isiPhone8 is True or isiPhoneSE is True):
        res.append('')
    for i in a:
        if 'iPhone 14' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone 15" in i and checkUsed(i):
            isiPhone15 = True
    if isiPhone15 is True and (isiPhone14 is True or isiPhone13 is True or isiPhone12 is True or isiPhone11 is True 
                               or isiPhone7 is True or isiPhone8 is True or isiPhoneSE is True or isiPhoneX is True):
        res.append('')
    for i in a:
        if 'iPhone 15' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPhone 16" in i and checkUsed(i):
            isiPhone16 = True
    if isiPhone16 is True and (isiPhone15 is True or isiPhone14 is True or isiPhone13 is True or isiPhone12 is True or isiPhone11 is True 
                               or isiPhone7 is True or isiPhone8 is True or isiPhoneSE is True or isiPhoneX is True):
        res.append('')
    for i in a:
        if 'iPhone 16' in i and checkUsed(i):
            res.append(fixName(i))
            
    #######################
    for i in a:
        if "Watch SE" in i and checkUsed(i):
            isAWSE = True
    if isAWSE is True:
        res.append('')
        res.append("⌚️ *Apple Watch SE 2023*")
    for i in a:
        if 'Watch SE' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Watch S8" in i and checkUsed(i):
            isAWS8 = True
    if isAWS8 is True:
        res.append('')
        res.append("⌚️ *Apple Watch S8*")
    for i in a:
        if 'Watch S8' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Watch S9" in i and checkUsed(i):
            isAWS9 = True
    if isAWS9 is True:
        res.append('')
        res.append("⌚️ *Apple Watch S9*")
    for i in a:
        if 'Watch S9' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iPad" in i and checkUsed(i):
            isiPad = True
    if isiPad is True:
        res.append('')
        res.append("📟 *Apple iPad*")
    for i in a:
        if 'iPad' in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "MacBook" in i and checkUsed(i):
            isMacBook = True
    if isMacBook is True:
        res.append('')
        res.append("💻 *Apple MacBook*")
    for i in a:
        if "MacBook" in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "iMac" in i and checkUsed(i):
            isiMac = True
    if isiMac is True:
        res.append('')
        res.append("🖥️ *Apple iMac*")
    for i in a:
        if "iMac" in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung" in i and checkUsed(i):
            isSams = True
    if isSams is True:
        res.append('')
        res.append("📱 *Samsung*")
    for i in a:
        if "Samsung" in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if ("Xiaomi" in i or "Poco" in i) and checkUsed(i):
            isXiaomi = True
    if isXiaomi is True:
        res.append('')
        res.append("📱 *Xiaomi*")
    for i in a:
        if ("Xiaomi" in i or "Poco" in i) and checkUsed(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Xiaomi" not in i and "Poco" not in i and "Samsung" not in i and "Apple" not in i and checkUsed(i):
            isOther = True
    if isOther is True:
        res.append('')
        res.append("📱 *Остальные бренды*")
    for i in a:
        if "Xiaomi" not in i and "Poco" not in i and "Samsung" not in i and "Apple" not in i and checkUsed(i):
            res.append(fixName(i))
    #######################
    res.append('')
    res.append('──── ୨୧ ────')
    res.append('')
    res.append("🏷 *Пломбы*")
    for i in a:
        if "Пломба" in i or "Пломбa" in i:
            res.append(fixName(i))
    #######################
    for i in a:
        if ("Обменка" in i or "обменка" in i or "Демо" in i):
            isDemo = True
    if isDemo is True:
        res.append('')
        res.append('──── ୨୧ ────')
        res.append('')
        res.append("🔥 *Обменки / Демо*")
    for i in a:
        if ("Обменка" in i or "обменка" in i or "Демо" in i):
            res.append(fixName(i))
    
    return '\n'.join([str(i) for i in res])

@dp.message()
async def echo_message(message: types.Message):
    btn = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton(text='base')]
    ], resize_keyboard=True)
    
    if message.text == '/start':
        await message.answer(returnHeader(), parse_mode='Markdown', reply_markup=btn)
        await message.answer(getApple(removeDouble), parse_mode='Markdown', reply_markup=btn)
        await message.answer(getSamsung(removeDouble), parse_mode='Markdown', reply_markup=btn)
        await message.answer(getCoros(removeDouble), parse_mode='Markdown', reply_markup=btn)
        await message.answer(getXiaomiYandexJBL(removeDouble), parse_mode='Markdown', reply_markup=btn)
        await message.answer(getUsed(removeDouble), parse_mode='Markdown', reply_markup=btn)
    
    if message.text == 'base':
        await message.answer(returnHeader(), parse_mode='Markdown', reply_markup=btn)
        await message.answer(getApple(removeDouble), parse_mode='Markdown', reply_markup=btn)
        await message.answer(getSamsung(removeDouble), parse_mode='Markdown', reply_markup=btn)
        await message.answer(getCoros(removeDouble), parse_mode='Markdown', reply_markup=btn)
        await message.answer(getXiaomiYandexJBL(removeDouble), parse_mode='Markdown', reply_markup=btn)
        await message.answer(getUsed(removeDouble), parse_mode='Markdown', reply_markup=btn)
        await bot.send_message(
            chat_id=CHANNEL_ID,
            parse_mode='Markdown',
            text=returnHeader())
        await bot.send_message(
            chat_id=CHANNEL_ID,
            parse_mode='Markdown',
            text=getApple(removeDouble))
        await bot.send_message(
            chat_id=CHANNEL_ID,
            parse_mode='Markdown',
            text=getSamsung(removeDouble))
        await bot.send_message(
            chat_id=CHANNEL_ID,
            parse_mode='Markdown',
            text=getCoros(removeDouble))
        await bot.send_message(
            chat_id=CHANNEL_ID,
            parse_mode='Markdown',
            text=getXiaomiYandexJBL(removeDouble))
        await bot.send_message(
            chat_id=CHANNEL_ID,
            parse_mode='Markdown',
            text=getUsed(removeDouble))
        
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