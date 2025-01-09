import asyncio
import logging
import logging.config

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

import openpyxl
# Define variable to load the wookbook
wookbook = openpyxl.load_workbook("priceFromBase.xlsx")
# Define variable to read the active sheet:
worksheet = wookbook.active
result = []
first_column = worksheet['C']
# Iterate the loop to read the cell values
# for i in range(0, first_column):
#     for col in worksheet.iter_cols(1, worksheet.max_column):
#         result.append(first_column[i].value)

for x in range(len(first_column)): 
    if first_column[x].value:
        result.extend(first_column[x].value) 



BOT_TOKEN = '7797795450:AAGS2CY8V0D6lhK9FHfU8afMbWx40PEOctY'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



str_nums = ["Poco F6 12/512 Black 🇪🇺35400", "Poco F6 12/512 Titanium 🇪🇺35400", "Poco F6 Pro 12/256 White 🇪🇺42700", 
            "Poco M6 Pro 8/256 Purple 🇪🇺17600", "Note 13 Pro 12/512 Forest Green 🇪🇺25800", "Pixel 9 Pro XL 16/256 Hazel 🇨🇦90500", 
            "PS5 DualSense Black - 7200", "MI 12 8/256 Blue 🇪🇺29800", "PlayStation VR2 🇨🇳52000", "Steam Deck 16/1Tb Black OLED 🇯🇵70500"]

def get(a):
    return '\n'.join([str(i) for i in a])



class price:
    default_color = "green"
    def __init__(self, name, price):
        self.name = name
        self.price = price
    

@dp.message()
async def echo_message(message: types.Message):
    btn = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton(text='First11')],
        [types.KeyboardButton(text='Second')]
    ])
    await message.answer(text="Wait a second...")

    def func():
        return get(str_nums)

    
    await message.answer(func(), reply_markup=btn)

    
    

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