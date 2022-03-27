import logging
import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "5252256067:AAFk5FrzjCKI2fgMsR5uD7xcZwA4EgkMN8w"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["помощь", "help"])
async def command_start(message: types.Message):
    markup = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton("Погода", callback_data="but_1")
    markup.add(but_1)
    but_2 = InlineKeyboardButton("Курс доллара", callback_data="but_2")
    markup.add(but_2)
    but_3 = InlineKeyboardButton("Курс евро", callback_data="but_3")
    markup.add(but_3)
    if message.from_user.first_name == 'Nukzar':
        await bot.send_message(message.chat.id, 'Как я могу вам помочь, Сэр?',
                               reply_markup=markup)
    else:
        await bot.send_message(message.chat.id, 'Как я могу вам помочь, ' + message.from_user.first_name + '?',
                               reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "but_1")
async def button_react(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    weather = "https://www.gismeteo.ru/weather-kazan-4364/now/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
    full_page = requests.get(weather, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "unit unit_temperature_c"})
    await bot.send_message(call.message.chat.id, "Погода в Казани в данный момент составляет: " + convert[0].text)


@dp.callback_query_handler(lambda c: c.data == "but_2")
async def button_react(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    dollar_rub = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&newwindow=1&sxsrf=APq-WBtX-jj9qj6wzbPnCM7S5JK9rH2bjA%3A1648062948319&ei=5HE7YvOPE5GfgQbgkYmgAQ&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+r&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQsQIQJzIHCCMQsQIQJzIECAAQQzIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIHCAAQyQMQCjIECAAQCjoHCCMQsAMQJzoHCAAQRxCwAzoKCAAQRxCwAxDJA0oECEEYAEoECEYYAFC1AViUAmD7BmgBcAF4AYABgwWIAY4GkgEHMC4xLjUtMZgBAKABAcgBCsABAQ&sclient=gws-wiz"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
    full_page = requests.get(dollar_rub, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
    await bot.send_message(call.message.chat.id,
                           "Официальный курс доллара на бирже в данный момент составляет: " + convert[0].text)


@dp.callback_query_handler(lambda c: c.data == "but_3")
async def button_react(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    euro_rub = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+&aqs=chrome.0.0i20i263i512j0i512l5j69i57j69i61.6463j1j7&sourceid=chrome&ie=UTF-8"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
    full_page = requests.get(euro_rub, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
    await bot.send_message(call.message.chat.id,
                           "Официальный курс евро на бирже в данный момент составляет: " + convert[0].text)


@dp.message_handler()
async def hello(msg: types.Message):
    if "Hello" in msg.text or "HELLO" in msg.text or "Hi" in msg.text or "Привет" in msg.text or "привет" in msg.text or "ПРИВЕТ" in msg.text:
        if msg.from_user.first_name == "Nukzar":
            await msg.reply('Добрый день, Сэр!')
        else:
            await msg.reply("Здравствуйте, " + msg.from_user.first_name + "! " +
                            "Я ассистент мистера Нукзара. Чем я могу вам помочь?")
    elif 'Спасибо' in msg.text or 'Thanks' in msg.text or 'Thnx' in msg.text or 'Пасиб' in msg.text or "Пасибо" in msg.text or "Спс" in msg.text or 'спасибо' in msg.text:
        if msg.from_user.first_name == 'Nukzar':
            await msg.reply('Всегда к вашим услугам, Сэр!')
        else:
            await msg.reply('Всегда к вашим услугам, ' + msg.from_user.first_name + "!")
    elif "Jarvis" in msg.text or "JARVIS" in msg.text or "Джарвис" in msg.text or "джарвис" in msg.text \
            or "ДЖАРВИС" in msg.text or "jarvis" in msg.text:
        if msg.from_user.first_name == "Nukzar":
            await msg.reply('Слушаю вас, Сэр')
        else:
            await msg.reply('Слушаю вас, ' + msg.from_user.first_name)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
