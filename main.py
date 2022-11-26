import telebot
import requests
from telebot import types
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
config_dict['language'] = 'ru'

url = 'http://api.openweathermap.org/data/2.5/weather'
api_weather = 'd182349a37cfd1427c8d6240607a3353'

bot = telebot.TeleBot('5901828532:AAGQ0LUgxceXeGcmFeGE3AVLFdVpGRRhAJ0')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить website", url="http://127.0.0.1:8000/"))
    bot.send_message(message.chat.id, 'Чтобы узнать мой весь функционал, введите команду: /help')


@bot.message_handler(commands=['help'])
def get_user_help(message):
    help_text = '''<b>Вот мой весь функционал:
/start - Запуск бота.
/help - Команда для запроса помощи.
/website - Получить ссылку на сайт (RubiLom'a)
/weather - Получить погоду на сегодня
/schedule - Получить расписание
/debt - Получить информацию о долгах по учебе</b>
    '''
    bot.send_message(message.chat.id, help_text, parse_mode='html')


@bot.message_handler(commands=['website'])
def get_user_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить website", url="http://127.0.0.1:8000/"))
    bot.send_message(message.chat.id, 'Для перехода на сайт, нажмите на кнопку!', reply_markup=markup)


@bot.message_handler(commands=['debt'])
def get_user_debt(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Долги по учебе", url="https://classroom.google.com/u/1/w/MTQyNjcxNjk1NDg3/t/all"))
    bot.send_message(message.chat.id, 'Чтобы узнать свои долги по учебе --> Нажмите на кнопку!', reply_markup=markup)


@bot.message_handler(commands=['weather'])
def weather_send(message):
    s_city = 'Днепр'
    try:
        params = {'APPID': api_weather, 'q': s_city, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()

        bot.send_message(message.chat.id,
                        "🏙️ В городе " + str(weather["name"]) + " температура - " + str(float(weather["main"]['temp'])) + "\n" +
                        "🌡️ Максимальная температура - " + str(float(weather['main']['temp_max'])) + "\n" +
                        "🌡️ Минимальная температура - " + str(float(weather['main']['temp_min'])) + "\n" +
                        "💨 Скорость ветра - " + str(float(weather['wind']['speed'])) + "\n" +
                        "🗜 Давление - " + str(float(weather['main']['pressure'])) + "\n" +
                        "💧 Влажность - " + str(float(weather['main']['humidity'])) + "\n" +
                        "🌫 Видимость - " + str(weather['visibility']) + "\n" +
                        "❓ Описание - " + str(weather['weather'][0]["description"]) + "\n")

        if weather["main"]['temp'] < 0:
            bot.send_message(message.chat.id, "🧊 А тебе точно нужно куда-то идти?" + "\n" + "Дома не так уж и плохо.")
        elif weather["main"]['temp'] < 10:
            bot.send_message(message.chat.id, "🥶 Сейчас холодно!")
        elif weather["main"]['temp'] < 20:
            bot.send_message(message.chat.id, "😑 Сейчас прохладно!")
        elif weather["main"]['temp'] > 38:
            bot.send_message(message.chat.id, "🥵 Сейчас жарко!")
        else:
            bot.send_message(message.chat.id, "😁 Сейчас отличная температура!")

    except:
        bot.send_message(message.chat.id, "🌁 Город " + s_city + " не найден")


@bot.message_handler(commands=['schedule'])
def schedule(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Понедельник", callback_data="monday"),
               types.InlineKeyboardButton("Вторник", callback_data="tuesday"),
               types.InlineKeyboardButton("Среда", callback_data="wednesday"),
               types.InlineKeyboardButton("Четверг", callback_data="thursday"),
               types.InlineKeyboardButton("Пятница", callback_data="friday"))
    bot.send_message(message.chat.id, 'Выберете расписание на какой день.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
     if call.message:
        if call.data == "monday":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="""
Понедельник
1 - 8:30 - Геометрия
2 - 9:25 - Защита Украины
3 - 10:25 - Немецкий 
4 - 11:30 - География/Химия 
5 - 12:25 - Информатика 
6 - 13:20 - Физика 
7 - 14:15 - Английский
""")

     if call.message:
        if call.data == "tuesday":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="""
Вторник
1 - 8:30 - Биология
2 - 9:25 - Гражданская обучение
3 - 10:25 - География
4 - 11:30 - Физра 
5 - 12:25 - Физика 
6 - 13:20 - Зарубежка 
7 - 14:15 - История/Защита Украины
""")
     if call.message:
        if call.data == "wednesday":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="""
Среда
1 - 8:30 - Рисование
2 - 9:25 - Албебра
3 - 10:25 - Немецкий
4 - 11:30 - Физра 
5 - 12:25 - Украинский язык
6 - 13:20 - Химия
7 - 14:15 - Английский
""")
     if call.message:
        if call.data == "thursday":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="""
Четверг
1 - 8:30 - Украинская литература
2 - 9:25 - Физика
3 - 10:25 - Немецкий
4 - 11:30 - Информатика
5 - 12:25 - Физра
6 - 13:20 - Украинский язык
7 - 14:15 - История
""")
     if call.message:
        if call.data == "friday":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="""
Пятница
1 - 8:30 - Украинский язык
2 - 9:25 - Геометрия
3 - 10:25 - Немецкий
4 - 11:30 - История 
5 - 12:25 - Биология 
6 - 13:20 - Английский
7 - 14:15 - Немецкий
""")


bot.polling(none_stop=True)
