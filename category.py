from aiogram.utils.markdown import hlink


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
    isDemo = False
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
        if "iPhone 15" in i and "iPhone 15 Pro" not in i and baseFix(i):
            res.append(fixName(i))
            
    #######################
    for i in a:
        if "iPhone 15 Pro" in i and "iPhone 15 Pro Max" not in i and baseFix(i):
            isiPhone15Pro = True
    if (isiPhone15Pro is True and (isiPhone15 is True or isiPhone14 is True or isiPhone13 is True or 
        isiPhone12 is True or isiPhone11 is True)):
        res.append("")
    for i in a:
        if "iPhone 15 Pro" in i and "iPhone 15 Pro Max" not in i and baseFix(i):
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
        if ("SE 2024 Gen" in i or "Watch SE 2024" in i or "Watch SE (2024)" in i) and baseFix(i):
            isAppleWatchSE2024 = True   
    if isAppleWatchSE2024 is True:
        res.append("")
        res.append("⌚️ *Apple Watch SE 2024*")
    for i in a:
        if ("SE 2024 Gen" in i or "Watch SE 2024" in i or "Watch SE (2024)" in i) and baseFix(i):
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
    
    isGalaxyWatch = False
    
    isGalaxyBuds = False
    #################
    res = []
    
    for i in a:
        if "Galaxy Watch" in i and baseFix(i):
            isGalaxyWatch = True
    if isGalaxyWatch is True:
        res.append('')
        res.append("⌚️ *Galaxy Watch*")
    for i in a:
        if ('Galaxy Watch' in i) and baseFix(i):
            res.append(i)
            
    #######################

    for i in a:
        if "Galaxy Buds" in i and baseFix(i):
            isGalaxyBuds = True
    if isGalaxyBuds is True:
        res.append('')
        res.append("🎧 *Galaxy Buds*")
    for i in a:
        if ('Galaxy Buds' in i) and baseFix(i):
            res.append(i)
    
    for i in a:
        if "Samsung Galaxy" in i and 'Galaxy Tab' not in i and baseFix(i):
            isGalaxyPhone = True
    if isGalaxyPhone is True and (isGalaxyBuds is True or isGalaxyWatch is True):
        res.append("")
    if isGalaxyPhone is True:
        res.append("📲 *Galaxy Phone*")
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
        if "Samsung Galaxy S25" in i and "Samsung Galaxy S25 Ultra" not in i and "Samsung Galaxy S25 FE" not in i and "Samsung Galaxy S25+" not in i and baseFix(i):
            isGalaxyS24 = True
    if isGalaxyS24 is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S25" in i and "Samsung Galaxy S25 Ultra" not in i and "Samsung Galaxy S25 FE" not in i and "Samsung Galaxy S25+" not in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy S25 FE" in i and baseFix(i):
            isGalaxyS24FE = True
    if isGalaxyS24FE is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S25 FE" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy S25+" in i and baseFix(i):
            isGalaxyS24Plus = True
    if isGalaxyS24Plus is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S25+" in i and baseFix(i):
            res.append(fixName(i))
    #######################
    for i in a:
        if "Samsung Galaxy S25 Ultra" in i and baseFix(i):
            isGalaxyS24Ultra = True
    if isGalaxyS24Ultra is True:
        res.append("")
    for i in a:
        if "Samsung Galaxy S25 Ultra" in i and baseFix(i):
            res.append(fixName(i))
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

def getUsedSN(a):
    def checkUsed(name):
        return (
        '"A-"' in name  or
        '"A"' in name or
        '"A+"' in name or
        '"B-"' in name or
        '"B"' in name or
        '"B+"' in name  or
        '"C-"' in name  or
        '"C"' in name or
        '"C+"' in name 
    )
    res = []
    res.append('IMEI / SN:')
    for i in a:
        if checkUsed(i):
            res.append(i.split("imei", 1)[1])
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
    res.append('👇 <b>Идеальное БУ</b>')
    res.append('')
    res.append('📸_Описание и фотографии_')
    res.append('🔗https://t.me/+969mFs7AbldkYTQ6')
    res.append('')
       
    res.append("🍏 <b>Apple</b>")
    for i in a:
        if ("AirPods" in i or 'Apple Magic' in i or 'Apple Battery' in i or 'Apple TV' in i or 'Apple HomePod' in i or 'Apple AirTag' in i or 'Pencil' in i)  and checkUsed(i):
            res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "iPhone" in i and checkUsed(i):
            isiPhone = True
    if isiPhone is True:
        res.append('')
        res.append("📱 <b>Apple iPhone</b>")
            
    #######################
    for i in a:
        if "iPhone 7" in i and checkUsed(i):
            isiPhone7 = True
    for i in a:
        if 'iPhone 7' in i and checkUsed(i):
            res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "iPhone 8" in i and checkUsed(i):
            isiPhone8 = True
    if isiPhone8 is True and isiPhone7 is True:
        res.append('')
    for i in a:
        if 'iPhone 8' in i and checkUsed(i):
            res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "iPhone SE" in i and checkUsed(i):
            isiPhoneSE = True
    if isiPhoneSE is True and (isiPhone7 is True or isiPhone8 is True):
        res.append('')
    for i in a:
        if 'iPhone SE' in i and checkUsed(i):
            res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "iPhone X" in i and checkUsed(i):
            isiPhoneX = True
    if isiPhoneX is True and (isiPhoneSE is True or isiPhone7 is True or isiPhone8 is True):
        res.append('')
    for i in a:
        if 'iPhone X' in i and checkUsed(i):
            res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "iPhone 11" in i and checkUsed(i):
            isiPhone11 = True
    if isiPhone11 is True and (isiPhoneX is True or isiPhoneSE is True or isiPhone7 is True or isiPhone8 is True):
        res.append('')
    for i in a:
        if 'iPhone 11' in i and checkUsed(i):
            if ('357879821502784' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('11 128 Red "B"', hlink('11 128 Red "B"', 'https://t.me/c/1545286162/3112')))
            elif ('352928112609686' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('11 128 Red "B"', hlink('11 128 Red "B"', 'https://t.me/c/1545286162/3314')))
            elif ('355125538424959' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('11 128 Purple "B"', hlink('11 128 Purple "B"', 'https://t.me/c/1545286162/3367')))
            elif ('353833100695045' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('11 Pro 64 Gray "B"', hlink('11 Pro 64 Gray "B"', 'https://t.me/c/1545286162/3431')))
            else:
                res.append(fixName(i.split("imei", 1)[0]))
            
            
    #######################
    for i in a:
        if "iPhone 12" in i and checkUsed(i):
            isiPhone12 = True
    if isiPhone12 is True and (isiPhone11 is True or isiPhoneX is True or isiPhoneSE is True 
                               or isiPhone7 is True or isiPhone8 is True):
        res.append('')
    for i in a:
        if 'iPhone 12' in i and checkUsed(i):
            if ('356683116177968' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('12 Pro 128 Blue "A-"', hlink('12 Pro 128 Blue "A-"', 'https://t.me/c/1545286162/3262')))
            elif ('354741663374354' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('12 Pro Max 256 Gold "B+"', hlink('12 Pro Max 256 Gold "B+"', 'https://t.me/c/1545286162/3067')))
            elif ('357095185548020' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('12 Pro Max 256 Blue "A-"', hlink('12 Pro Max 256 Blue "A-"', 'https://t.me/c/1545286162/3436')))
            elif ('357014746875004' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('12 Pro Max 128 Graphite "B"', hlink('12 Pro Max 128 Graphite "B"', 'https://t.me/c/1545286162/3175')))
                
            else:
                res.append(fixName(i.split("imei", 1)[0]))
        
    #######################
    for i in a:
        if "iPhone 13" in i and checkUsed(i):
            isiPhone13 = True
    if isiPhone13 is True and (isiPhone12 is True or isiPhone11 is True or isiPhoneX is True or isiPhoneSE is True 
                               or isiPhone7 is True or isiPhone8 is True):
        res.append('')
    for i in a:
        if 'iPhone 13' in i and checkUsed(i):
            
            if ('358184149822991' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 128 Blue "B"', hlink('13 128 Blue "B"', 'https://t.me/c/1545286162/2833')))
            elif ('356122174586851' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 128 Blue "B"', hlink('13 128 Blue "B"', 'https://t.me/c/1545286162/3053')))
            elif ('354038644827091' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 128 Midnight "B"', hlink('13 128 Midnight "B"', 'https://t.me/c/1545286162/3492')))
            elif ('350196691085130' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 128 Midnight "B-"', hlink('13 128 Midnight "B-"', 'https://t.me/c/1545286162/3493')))
            elif ('357492900363894' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 128 White "B"', hlink('13 128 White "B"', 'https://t.me/c/1545286162/3500')))
            elif ('354038644827091' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 128 Midnight "C"', hlink('13 128 Midnight "C"', 'https://t.me/c/1545286162/3412')))
            elif ('353013830678898' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 128 Red "B"', hlink('13 128 Red "B"', 'https://t.me/c/1545286162/3417')))
            elif ('355402939339932' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 128 Midnight "B"', hlink('13 128 Midnight "B"', 'https://t.me/c/1545286162/2945')))
            elif ('358184140200742' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 256 Pink "A"', hlink('13 256 Pink "A"', 'https://t.me/c/1545286162/3193')))
            elif ('359595813464498' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 256 Blue "B+"', hlink('13 256 Blue "B+"', 'https://t.me/c/1545286162/3442')))
            elif ('359339135664315' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 Pro 128 Blue "A-"', hlink('13 Pro 128 Blue "A-"', 'https://t.me/c/1545286162/3200')))
            elif ('357038541207089' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 Mini 128 Blue "B+"', hlink('13 Mini 128 Blue "B+"', 'https://t.me/c/1545286162/3047')))
            elif ('356942286320166' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 Pro 256 Blue "B"', hlink('13 Pro 256 Blue "B"', 'https://t.me/c/1545286162/3062')))
            elif ('359366640347946' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 Pro 256 Blue "B"', hlink('13 Pro 256 Blue "B"', 'https://t.me/c/1545286162/2893')))
            elif ('351243328068821' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 Pro Max 1Tb Gold "B"', hlink('13 Pro Max 1Tb Gold "B"', 'https://t.me/c/1545286162/2924')))
            elif ('357624693272193' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 Pro Max 256 Blue "B"', hlink('13 Pro Max 256 Blue "B"', 'https://t.me/c/1545286162/3097')))
            elif ('355782151840166' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 Pro Max 256 Blue "C"', hlink('13 Pro Max 256 Blue "C"', 'https://t.me/c/1545286162/2820')))
            elif ('357724820810277' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('13 Pro 512 Blue "A"', hlink('13 Pro 512 Blue "A"', 'https://t.me/c/1545286162/3074')))
            else:
                res.append(fixName(i.split("imei", 1)[0]))
            
    #######################
    for i in a:
        if "iPhone 14" in i and checkUsed(i):
            isiPhone14 = True
    if isiPhone14 is True and (isiPhone13 is True or isiPhone12 is True or isiPhone11 is True or isiPhoneX is True 
                               or isiPhone7 is True or isiPhone8 is True or isiPhoneSE is True):
        res.append('')
    for i in a:
        if 'iPhone 14' in i and checkUsed(i):
            if ('354248582072002' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('14 128 Purple "A"', hlink('14 128 Purple "A"', 'https://t.me/c/1545286162/2957')))
            elif ('351850726307401' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('14 Pro 128 Purple "A"', hlink('14 Pro 128 Purple "A"', 'https://t.me/c/1545286162/3181')))
            elif ('351850727648795' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('14 Pro 128 Purple "B"', hlink('14 Pro 128 Purple "B"', 'https://t.me/c/1545286162/2864')))
            elif ('351643939531192' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('14 Pro Max 128 Black "B"', hlink('14 Pro Max 128 Black "B"', 'https://t.me/c/1545286162/3477')))
            elif ('351643937340166' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('14 Pro Max 128 Purple"B"', hlink('14 Pro Max 128 Purple"B"', 'https://t.me/c/1545286162/3206')))
            elif ('357173347519195' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('14 Pro Max 128 Silver "B"', hlink('14 Pro Max 128 Silver "B"', 'https://t.me/c/1545286162/3107')))
            elif ('351542666082082' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('14 Pro Max 256 Gold "A"', hlink('14 Pro Max 256 Gold "A"', 'https://t.me/c/1545286162/2965')))
            elif ('351344356815453' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('14 Pro Max 256 Black "A-"', hlink('14 Pro Max 256 Black "A-"', 'https://t.me/c/1545286162/3482')))
            elif ('359687306847519' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('14 Pro Max 256 Purple "B"', hlink('14 Pro Max 256 Purple "B"', 'https://t.me/c/1545286162/3186')))
            elif ('353180364328883' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('14 Pro Max 256 Purple "B-"', hlink('14 Pro Max 256 Purple "B-"', 'https://t.me/c/1545286162/3090')))
            elif ('351344350268352' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('14 Pro Max 512 Gold Dual Sim "A"', hlink('14 Pro Max 512 Gold Dual Sim "A"', 'https://t.me/c/1545286162/2875')))
            else:
                res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "iPhone 15" in i and checkUsed(i):
            isiPhone15 = True
    if isiPhone15 is True and (isiPhone14 is True or isiPhone13 is True or isiPhone12 is True or isiPhone11 is True 
                               or isiPhone7 is True or isiPhone8 is True or isiPhoneSE is True or isiPhoneX is True):
        res.append('')
    for i in a:
        if 'iPhone 15' in i and checkUsed(i):
            if ('356876522178238' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('15 Pro Max 256 White "A"', hlink('15 Pro Max 256 White "A"', 'https://t.me/c/1545286162/3079')))
            elif ('357497540876452' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('15 128 Green "A"', hlink('15 128 Green "A"', 'https://t.me/c/1545286162/3058')))
            elif ('356176844150605' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('15 Pro 256 Natural "A"', hlink('15 Pro 256 Natural "A"', 'https://t.me/c/1545286162/3424')))
            elif ('355721794375735' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('15 Pro 128 Black "A', hlink('15 Pro 128 Black "A', 'https://t.me/c/1545286162/3505')))
            else:
                res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "iPhone 16" in i and checkUsed(i):
            isiPhone16 = True
    if isiPhone16 is True and (isiPhone15 is True or isiPhone14 is True or isiPhone13 is True or isiPhone12 is True or isiPhone11 is True 
                               or isiPhone7 is True or isiPhone8 is True or isiPhoneSE is True or isiPhoneX is True):
        res.append('')
    for i in a:
        if 'iPhone 16' in i and checkUsed(i):
            res.append(fixName(i.split("imei", 1)[0]))
            
    #######################
    for i in a:
        if "Watch SE" in i and checkUsed(i):
            isAWSE = True
    if isAWSE is True:
        res.append('')
        res.append("⌚️ <b>Apple Watch SE 2023</b>")
    for i in a:
        if 'Watch SE' in i and checkUsed(i):
            res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "Watch S8" in i and checkUsed(i):
            isAWS8 = True
    if isAWS8 is True:
        res.append('')
        res.append("⌚️ <b>Apple Watch S8</b>")
    for i in a:
        if 'Watch S8' in i and checkUsed(i):
            res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "Watch S9" in i and checkUsed(i):
            isAWS9 = True
    if isAWS9 is True:
        res.append('')
        res.append("⌚️ <b>Apple Watch S9</b>")
    for i in a:
        if 'Watch S9' in i and checkUsed(i):
            res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "iPad" in i and checkUsed(i):
            isiPad = True
    if isiPad is True:
        res.append('')
        res.append("📟 <b>Apple iPad</b>")
    for i in a:
        if 'iPad' in i and checkUsed(i):
            if ('DLXS92H6GMLD' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('iPad Pro 12.9 (2015) 32 Wi-fi Gray "B+"', \
                    hlink('iPad Pro 12.9 (2015) 32 Wi-fi Gray "B+"', 'https://t.me/c/1545286162/2858')))
            else:
                res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "MacBook" in i and checkUsed(i):
            isMacBook = True
    if isMacBook is True:
        res.append('')
        res.append("💻 <b>Apple MacBook</b>")
    for i in a:
        if "MacBook" in i and checkUsed(i):
            if ('C02RX0PJGTHV' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('12 (2016 - MLHC2) 8/512 Silver "B+"', \
                    hlink('12 (2016 - MLHC2) 8/512 Silver "B+"', 'https://t.me/c/1545286162/3164')))
            elif ('FVFWHFU4J1WK' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Air 13 (2017 - MQD32) 8/128 Silver "C"', \
                    hlink('Air 13 (2017 - MQD32) i5 8/128 Silver "C"', 'https://t.me/c/1545286162/2984')))
            elif ('FVFZ2B30LYWJ' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Air 13 (2019 - MVFH2) i5 8/128 Silver "B"', \
                    hlink('Air 13 (2019 - MVFH2) i5 8/128 Silver "B"', 'https://t.me/c/1545286162/3543')))
            elif ('FVFZP6V4J1WK' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Air 13 (2017 - MQD32) i5 8/128 Silver "B+"', \
                    hlink('Air 13 (2017 - MQD32) i5 8/128 Silver "B+"', 'https://t.me/c/1545286162/3037')))
            elif ('FVFDN4WXM6KJ' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Air 13 (2020 - MVH52) i5 8/512 Gold "B"', \
                    hlink('Air 13 (2020 - MVH52) i5 8/512 Gold "B"', 'https://t.me/c/1545286162/2665')))
            elif ('C02F2279Q6L8' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Air 13 M1 (2020 - MGNA3) 8/512 Silver "A-"', \
                    hlink('Air 13 M1 (2020 - MGNA3) 8/512 Silver "A-"', 'https://t.me/c/1545286162/2670')))
            elif ('FVFFW0JSQ6M0' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Air 13 M1 (2020 - Z12A0008Q) 16/256 Gold "A-"', \
                    hlink('Air 13 M1 (2020 - Z12A0008Q) 16/256 Gold "A-"', 'https://t.me/c/1545286162/2711')))
            elif ('FVFZR8CCL40Y' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 13 (2019 - MUHN2) 8/128 T/B "A-"', \
                    hlink('Pro 13 (2019 - MUHN2) 8/128 T/B "A-"', 'https://t.me/c/1545286162/2992')))
            elif ('C02CM175ML7J' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 13 (2020 - MWP52) i5 16/1TB T/Bar "B"', \
                    hlink('Pro 13 (2020 - MWP52) i5 16/1TB T/Bar "B"', 'https://t.me/c/1545286162/2998')))
            elif ('C02JRN00DKQ1' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 15 (2012 - MC975 Retina) i7 8/256 Silver (АКБ 1 цикл) "B"', \
                    hlink('Pro 15 (2012 - MC975 Retina) i7 8/256 Silver (АКБ 1 цикл) "B"', 'https://t.me/c/1545286162/3003')))
            elif ('C02C2H3EMD6M' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 16 (2019 - MVVL2) i7 16/512 Gray "B"', \
                    hlink('Pro 16 (2019 - MVVL2) i7 16/512 Gray "B"', 'https://t.me/c/1545286162/3007')))
            elif ('sc02yh0f0jhc9' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 13 (2018 - MR9R2) i5 8/512 T/Bar "B"', \
                    hlink('Pro 13 (2018 - MR9R2) i5 8/512 T/Bar "B"', 'https://t.me/c/1545286162/3231')))
            elif ('C02SR0S2GTFL' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 15 (2016 - MLH32) i7 16/256 T/Bar "B+"', \
                    hlink('Pro 15 (2016 - MLH32) i7 16/256 T/Bar "B+"', 'https://t.me/c/1545286162/3243')))
            elif ('C02V54QYHTD6' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 15 (2017 - MPTT2) i7 16/512 Gray "B+"', \
                    hlink('Pro 15 (2017 - MPTT2) i7 16/512 Gray "B+"', 'https://t.me/c/1545286162/3388')))
            elif ('C02S72HFFVH7' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 13 (2015 - MF841) 8/512 Silver "B"', \
                    hlink('Pro 13 (2015 - MF841) 8/512 Silver "B"', 'https://t.me/c/1545286162/3392')))
            elif ('HXJMK1BL1WG7' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Air 13 (2020 - MGN63) M1 8/256 "A"', \
                    hlink('Air 13 (2020 - MGN63) M1 8/256 "A"', 'https://t.me/c/1545286162/3398')))
            elif ('C02G80LZMD6T' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 16 (2019 - MVVM2 ) i9 32/1TB T/B  "B+"', \
                    hlink('Pro 16 (2019 - MVVM2 ) i9 32/1TB T/B  "B+"', 'https://t.me/c/1545286162/3342')))
            elif ('C02ZQ714MD6Q' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 16 (2019 - MVVM2) i9 16/1TB T/B "B+"', \
                    hlink('Pro 16 (2019 - MVVM2) i9 16/1TB T/B "B+"', 'https://t.me/c/1545286162/3336')))
            elif ('FCV0XCW7J9' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Air 15 (2022 - MQKT3) M2 8/512 Silver "A"', \
                    hlink('Air 15 (2022 - MQKT3) M2 8/512 Silver "A"', 'https://t.me/c/1545286162/3448')))
            elif ('R91G9711Q9' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 13 (2022 - MNEJ3) M2 8/512 T/B "B+"', \
                    hlink('Pro 13 (2022 - MNEJ3) M2 8/512 T/B "B+"', 'https://t.me/c/1545286162/3455')))
            elif ('DP4JN4RR0Y' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 14 M1 Pro (2021 - Z15G001Q) 16/512 Gray "A"', \
                    hlink('Pro 14 M1 Pro (2021 - Z15G001Q) 16/512 Gray "A"', 'https://t.me/c/1545286162/3463')))
            elif ('X736565MVW' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 16 (2021 - MK183) M1 Pro 16/512 "A"', \
                    hlink('Pro 16 (2021 - MK183) M1 Pro 16/512 "A"', 'https://t.me/c/1545286162/3470')))
            elif ('C02Z55Z5L40Y' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 13 (2019 - MUHN2) i5 8/128 "A-"', \
                    hlink('Pro 13 (2019 - MUHN2) i5 8/128 "A-"', 'https://t.me/c/1545286162/3511')))
            elif ('MQW07GQCL4' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Pro 14 (2021 - MKGQ3) M1 Pro 16/1TB "A"', \
                    hlink('Pro 14 (2021 - MKGQ3) M1 Pro 16/1TB "A"', 'https://t.me/c/1545286162/3517')))
                
            else:
                res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "iMac" in i and checkUsed(i):
            isiMac = True
    if isiMac is True:
        res.append('')
        res.append("🖥️ <b>Apple iMac</b>")
    for i in a:
        if "iMac" in i and checkUsed(i):
            res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "Samsung" in i and checkUsed(i):
            isSams = True
    if isSams is True:
        res.append('')
        res.append("📱 <b>Samsung</b>")
    for i in a:
        if "Samsung" in i and checkUsed(i):
            if ('356663764960923' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Galaxy S23 Ultra 12/256 Black "A-"', \
                    hlink('Galaxy S23 Ultra 12/256 Black "A-"', 'https://t.me/c/1545286162/3536')))
            elif ('350272253363965' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Galaxy S22 Ultra 12/256 Black "B"', \
                    hlink('Galaxy S22 Ultra 12/256 Black "B"', 'https://t.me/c/1545286162/3275')))
            elif ('350683210272307' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Galaxy S24 Ultra 12/256 Black "A"', \
                    hlink('Galaxy S24 Ultra 12/256 Black "A"', 'https://t.me/c/1545286162/3268')))
            elif ('350928506521572' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Galaxy S21 FE 5G 6/128 Olive "B+"', \
                    hlink('Galaxy S21 FE 5G 6/128 Olive "B+"', 'https://t.me/c/1545286162/2917')))
            elif ('358453420322330' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Galaxy S21 FE 5G 256 Black "B-"', \
                    hlink('Galaxy S21 FE 5G 256 Black "B-"', 'https://t.me/c/1545286162/3525')))
                
            else:
                res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if ("Xiaomi" in i or "Poco" in i) and checkUsed(i):
            isXiaomi = True
    if isXiaomi is True:
        res.append('')
        res.append("📱 <b>Xiaomi</b>")
    for i in a:
        if ("Xiaomi" in i or "Poco" in i) and checkUsed(i):
            if ('865513052815756' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Xiaomi 12X 8/256 Purple "A"', \
                    hlink('Xiaomi 12X 8/256 Purple "A"', 'https://t.me/c/1545286162/2805')))
            elif ('865513054138959' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Xiaomi 12X 8/256 Purple "A"', \
                    hlink('Xiaomi 12X 8/256 Purple "A"', 'https://t.me/c/1545286162/3117')))
            elif ('860136069706233' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Xiaomi 14 Ultra 16/512 White "A"', \
                    hlink('Xiaomi 14 Ultra 16/512 White "A"', 'https://t.me/c/1545286162/3358')))
            elif ('866567073825425' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Redmi Note 13 Pro 4G 256 Black "B"', \
                    hlink('Redmi Note 13 Pro 4G 256 Black "B"', 'https://t.me/c/1545286162/3362')))
                
            else:
                res.append(fixName(i.split("imei", 1)[0]))
    #######################
    for i in a:
        if "Xiaomi" not in i and "Poco" not in i and "Samsung" not in i and "Apple" not in i and checkUsed(i):
            isOther = True
    if isOther is True:
        res.append('')
        res.append("📱 <b>Остальные бренды</b>")
    for i in a:
        if "Xiaomi" not in i and "Poco" not in i and "Samsung" not in i and "Apple" not in i and checkUsed(i):
            if ('N1N0CX203100039' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Asus VivoBook i7-1065G7 16/512 Silver "B"', \
                    hlink('Asus VivoBook i7-1065G7 16/512 Silver "B"', 'https://t.me/c/1545286162/3159')))
            elif ('4VCXZK3' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Dell Vostro 3510 i5-1035G1 8/256 Black "B"', \
                    hlink('Dell Vostro 3510 i5-1035G1 8/256 Black "B"', 'https://t.me/c/1545286162/3146')))
            elif ('DTL8RK3' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Dell Vostro 3510 i5-1135G7 16/512 Black "B"', \
                    hlink('Dell Vostro 3510 i5-1135G7 16/512 Black "B"', 'https://t.me/c/1545286162/3141')))
            elif ('1LFRHM3' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('Dell Vostro 3510 i7-1165G7 16/512 Gray "B-"', \
                    hlink('Dell Vostro 3510 i7-1165G7 16/512 Gray "B-"', 'https://t.me/c/1545286162/3152')))
            elif ('CND138123J' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('HP 250 G8 27K00EA i5-1035G1 8/256 Silver "B"', \
                    hlink('HP 250 G8 27K00EA i5-1035G1 8/256 Silver "B"', 'https://t.me/c/1545286162/3136')))
            elif ('CND3081D5Q' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('HP 255 G9 Ryzen 5 5625U 16/512 Silver "B"', \
                    hlink('HP 255 G9 Ryzen 5 5625U 16/512 Silver "B"', 'https://t.me/c/1545286162/3126')))
            elif ('CND2031SXL' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('HP Laptoop 15-dw1208ur i5-10210U 16/512 Silver "B"', \
                    hlink('HP Laptoop 15-dw1208ur i5-10210U 16/512 Silver "B"', 'https://t.me/c/1545286162/3131')))
            elif ('CND1071CK8' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('HP 255 G8 AMD 3050U 8/256 Black "B"', \
                    hlink('HP 255 G8 AMD 3050U 8/256 Black "B"', 'https://t.me/c/1545286162/3292')))
            elif ('CND1071CKL' in i):
                res.append(fixName(i.split("imei", 1)[0]).replace('HP 255 G8 AMD 3050U 8/256 Black "B"', \
                    hlink('HP 255 G8 AMD 3050U 8/256 Black "B"', 'https://t.me/c/1545286162/3292')))
                
            else:
                res.append(fixName(i.split("imei", 1)[0]))
    #######################
    res.append('')
    res.append('──── ୨୧ ────')
    res.append('')
    res.append("🏷 <b>Пломбы</b>")
    for i in a:
        if "Пломба" in i or "Пломбa" in i:
            res.append(fixName(i.split("imei", 1)[0]))
    
    
    return '\n'.join([str(i) for i in res])
