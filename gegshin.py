import telebot
from telebot import types
import random, time

electro = ['Куки Синобу', 'Фишль', 'Яэ Мико', 'Сёгун Райден', 'Кэ Цин', 'Лиза', 'Сайно', 'Сара', 'Бэй Доу', 'Дори',
           'Путешественик(-ница) электро ']  # 11
anemo = ['Путешественик(-ница) анемо ', 'Сяо-дед инсайд', 'Саю', 'Сахароза', 'Кадзуха', 'Алкаш-Венти', 'Джин']  # 7
gidro = ['Кокоми', 'Канадакия', 'Е Лань', 'Барбара', 'Барбара', 'Мона', 'Нилу', 'Син Цю', 'Тарталья']  # 9
piro = ['Ёимия', 'Беннет', 'Дэхья', 'Кли', 'Синь Янь', 'Сян Лин', 'Тома', 'Ху Тао', 'Эмбер',
        'Янь Фэй']  # 9+/ 1 без не вышедших
krio = ['Аяка', 'Гань Юй', 'Диона', 'Кэйа', 'Лайла', 'Мика', 'Розария', 'Чича', 'Чун Юнь', 'Шэнь Хэ', 'Элой',
        'Эола']  # 10 персонажей без не вышедших +/ 2
geo = ['Альбедо', 'Горо', 'Итто', 'Нин Гуан', 'Ноэлль', 'Путешественик(-ница) гео', 'Чжун Ли', 'Юнь Цзинь']  # 8 персонажей
dendro = ['Нахида', 'Коллеи', 'Путешественик(-ница) дендро', 'Тигнари']

random_elements = random.randint(1, 7)

bot = telebot.TeleBot('5646476235:AAGyxY-6BCvDTdjtOUw1V7DHVdO781SvDKE')


@bot.message_handler(commands=["start"])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=4)  # кол-во кнопок в строку
    but_1 = types.InlineKeyboardButton('да', callback_data='да')  # второе это id кнопки
    but_2 = types.InlineKeyboardButton('нет', callback_data='нет')
    markup.add(but_1, but_2)  # добавление кнопок
    bot.send_message(message.chat.id, 'Хотите узнать какой вы персонаж из геншина?',
                     reply_markup=markup)  # reply_markup=markup нужен для привязки сообщения к клавиатуре


@bot.callback_query_handler(func=lambda call: True)
def callback(call, i=5, g=1, k='.'):
    if call.message:
        if call.data == 'да':
            while (i >= 1):
                if (g) <= 5:
                    time.sleep(2)
                    bot.send_message(call.message.chat.id, "Происходит вычесление, подождите : " + (str(i) + (k * g)))
                    g += 1
                    i -= 1
            if random_elements == 1:
                bot.send_message(call.message.chat.id, "Вы персонаж из геншина " + random.choice(electro))
            if random_elements == 2:
                bot.send_message(call.message.chat.id, "Вы персонаж из геншина " + random.choice(anemo))
            if random_elements == 3:
                bot.send_message(call.message.chat.id, "Вы персонаж из геншина " + random.choice(gidro))
            if random_elements == 4:
                bot.send_message(call.message.chat.id, "Вы персонаж из геншина " + random.choice(piro))
            if random_elements == 5:
                bot.send_message(call.message.chat.id, "Вы персонаж из геншина " + random.choice(krio))
            if random_elements == 6:
                bot.send_message(call.message.chat.id, "Вы персонаж из геншина " + random.choice(geo))
            if random_elements == 7:
                bot.send_message(call.message.chat.id, "Вы персонаж из геншина " + random.choice(dendro))
        elif call.data == 'нет':
            bot.send_sticker(call.message.chat.id,  'CAACAgIAAxkBAAEGMRFjV5mRBecV-19WzQMGr6fBfuuywwAC3woAAiUM8Uvy73XODFUXuSoE')


bot.infinity_polling()
