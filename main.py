import logging 
import requests
import datetime
from aiogram import Bot, Dispatcher, executor, types


weather_token = "6e8d79779a0c362f14c60a1c7f363e29"

API_TOKEN = '1868753962:AAEa_dnh_Bz_5G2n4_YjJDwvX3ZkyntsoVk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


# @dp.message_handler(regexp='(^cat[s]?$|puss)')
# async def cats(message: types.Message):
#     with open('data/cats.jpg', 'rb') as photo:
#         '''
#         # Old fashioned way:
#         await bot.send_photo(
#             message.chat.id,
#             photo,
#             caption='Cats are here 😺',
#             reply_to_message_id=message.message_id,
#         )
#         '''

#         await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler(lambda message: message.text != "music")
async def echo(message: types.Message):
    r1 = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric")
    data = r1.json()
    city = data["name"]
    temperature = round(data["main"]["temp"])
    humidity = round(data["main"]["humidity"])
    wind = round(data["wind"]["speed"])
    await message.reply(f"***{datetime.datetime.now().strftime('%b %d %Y %H:%M')}***\n"
                        f"Погода в місті: {city}\n\U0001F321Температура: {temperature} C°\n"
                        f"\U0001F4A7Вологість повітря: {humidity} %\n"
                        f"\U0001F32AВітер: {wind} м/с\n ")

 
@dp.message_handler(regexp='music|музыка')
async def music(message: types.Message):
    await message.reply('https://www.youtube.com/watch?v=2i2khp_npdE')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)