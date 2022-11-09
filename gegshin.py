import telebot
from telebot import types
import random, time

electro = ['Kuki Shinobu', 'Fishl', 'Yae Miko', 'Shogun Raiden', 'Keqing', 'Lisa', ' Cyno', 'Sara', 'BeiDou ', 'Dori',
           'Travaler electro ']  
anemo = ['Travaler anemo ', 'Xiao', 'Sayu', 'Sucrose', 'Kazuha', 'Venti', 'Jean']  
gidro = ['Kokomi', 'Candace', 'Yelan', 'Barbara', 'Mona', 'Niloy', 'Sin Tsyu', 'Tartaglia']  
piro = ['Yoimiya', 'Bennett', 'Kli', 'Xinyan', 'Xiangling', 'Тома', 'Hu Tao', 'Amber',
        'Yan Fey']  
krio = ['Ayaka', 'Gan Yu', 'Diona', 'Keya', 'Rosary', 'Qiqi', 'Chongyun', 'Shēnhè', 'Aloy',
        'Eola']  
geo = ['Albedo', 'Gorou', 'Itto', 'Ningguang', 'Noelle ', 'Travler geo', 'Zhongli', 'Yún Jǐn)'] 
dendro = ['Nahida', 'Collei', 'Travaler dendro', 'Tighnary']

random_elements = random.randint(1, 7)

bot = telebot.TeleBot('Your api')#take from https://t.me/BotFather


@bot.message_handler(commands=["start"])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=2)  # number of buttons per line
    but_1 = types.InlineKeyboardButton('yes', callback_data='yes')  # the second is the button id
    but_2 = types.InlineKeyboardButton('no', callback_data='no')
    markup.add(but_1, but_2)  # adding buttons
    bot.send_message(message.chat.id, 'Do you want to know what kind of character you are from genshin?',
                     reply_markup=markup)  


@bot.callback_query_handler(func=lambda call: True)
def callback(call, i=5, g=1, k='.'):
    if call.message:
        if call.data == 'yes':#if the user clicks on 'yes' it will work
            while (i >= 1):
                if (g) <= 5:
                    time.sleep(2)
                    bot.send_message(call.message.chat.id, "Calculation is in progress, wait: " + (str(i) + (k * g)))#creating a loop for a relatively beautiful design
                    g += 1
                    i -= 1
            if random_elements == 1:
                bot.send_message(call.message.chat.id, "Are you a character from Genshin " + random.choice(electro))
            if random_elements == 2:
                bot.send_message(call.message.chat.id, "Are you a character from Genshin " + random.choice(anemo))
            if random_elements == 3:
                bot.send_message(call.message.chat.id, "Are you a character from Genshin " + random.choice(gidro))
            if random_elements == 4:
                bot.send_message(call.message.chat.id, "Are you a character from Genshin " + random.choice(piro))
            if random_elements == 5:
                bot.send_message(call.message.chat.id, "Are you a character from Genshin " + random.choice(krio))
            if random_elements == 6:
                bot.send_message(call.message.chat.id, "Are you a character from Genshin " + random.choice(geo))
            if random_elements == 7:
                bot.send_message(call.message.chat.id, "Are you a character from Genshin " + random.choice(dendro))
        elif call.data == 'no':
            bot.send_sticker(call.message.chat.id,  'your stiker')#take id sticker from https://t.me/idstickerbot


bot.infinity_polling()
