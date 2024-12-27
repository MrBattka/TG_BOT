import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
# from aiogram import types


BOT_TOKEN = '7797795450:AAGS2CY8V0D6lhK9FHfU8afMbWx40PEOctY'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# @dp.message()
# async def echo_message(message: types.Message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton("First BTN")
#     btn2 = types.KeyboardButton("Second BTN")
#     markup.row(btn1, btn2)
#     await bot.send_message(
#         chat_id=message.chat.id,
#         text="Start processing..."
#     )
#     await bot.send_message(
#         chat_id=message.chat.id,
#         text="Detected message...",
#         reply_to_message_id=message.message_id
#     )
#     await message.answer(text="Wait a second...")
#     await message.reply(text=message.text)


# async def main():
#     logging.basicConfig(level=logging.INFO)
#     await dp.start_polling(bot)



# if __name__ == "__main__":
#     asyncio.run(main())


from aiogram import types

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   kb = [
       [
           types.KeyboardButton(text="Сможешь повторить это?"),
           types.KeyboardButton(text="А это?")
       ],
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
 
   await message.reply("Привет!\nЯ Эхобот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.", reply_markup=keyboard)