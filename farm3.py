

import random

from pyrogram import Client, filters

from pyrogram.errors import *

from time import time
import asyncio
from asyncio import sleep
import pickle



yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
red = "\033[91m"
purple = "\033[35m"
orange = "\033[33m"
bots_id = ("gram_piarbot","pr_mitcoin_bot","Whale_Piar_bot")
log_group = "FGLogGroupSL23_Hello"
api_id = 24976468
api_hash = '6e498035dcf4d32e270ff3f90cf61c58'


with open("sessions.bin","rb") as f:
    phones = pickle.load(f)

print(clear)

bots = []

for i,phone in enumerate(phones):
    bots.append(Client(name=phone,
api_id=api_id,
api_hash=api_hash,
phone_number=phone))



class BotWPMode:
    def __init__(self):
        pass
    async def run(self,bot):
        if not bot.phone_number in [phones[0]]:
            return
        await bot.send_message(log_group, "BotWBMode")
        await bot.send_message(bots_id[2], "/start 6470140273")
        await sleep(3)
        await bot.send_message(bots_id[2], "💵 Заработать")
        await sleep(20)
        print("BWPMbot", bot.phone_number)
        for i_ in range(20):
            async for msg in bot.get_chat_history(bots_id[2], limit=1):
                split = msg.text.split()
                if msg.reply_markup:

                    if ''.join(split[0:3]) == "🚀КакВы":
                        await msg.click(0, 2)
                    elif ''.join(split[0:3]) == "🚀Длязаработка":
                        pass
                    elif split[0] == "❗️Ошибка❗️️":
                        await sleep(0.7)
                    elif ''.join(split[0:3]) == "📝Перейдитев":
                        if msg.reply_markup.inline_keyboard:
                            for r in msg.reply_markup.inline_keyboard:
                                if r[0].url:
                                    try:
                                        name = r[0].url.removeprefix("https://t.me/")
                                        try:
                                            name = name[0:name.index("?")]
                                        except:
                                            pass
                                        try:
                                            await bot.send_message(name, "/start")
                                            await sleep(10)
                                            await bot.send_message(name, "/start")
                                            await sleep(3)
                                            async for msg in bot.get_chat_history(name, limit=1):
                                                await bot.forward_messages(bots_id[2],msg.chat.id,[msg.id])
                                                await msg.chat.mute()
                                                await sleep(0.1)
                                                await msg.chat.archive()
                                                await bot.send_message(log_group, f"BWPM: @{name}")
                                        except:
                                            pass
                                    except:
                                        pass
                    elif ''.join(split[0:2]) == "💰Начислено":
                        await msg.click(0,0)
            await sleep(3.7)

class BotMode:
    def __init__(self):
        pass
    async def run(self,bot):
        await bot.send_message(log_group, "BotMode")
        await bot.send_message(bots_id[0], "👨‍💻 Заработать")
        await sleep(20)
        print("BMbot", bot.phone_number)
        for i_ in range(20):
            async for msg in bot.get_chat_history(bots_id[0], limit=1):
                split = msg.text.split()
                if msg.reply_markup:

                    if ''.join(split[0:3]) == "💰Выможете":
                        await msg.click(0, 3)
                    elif ''.join(split[0:3]) == "⚠️Запрещеноблокировать":
                        await msg.click(0, 0)

                    elif ''.join(split[0:2]) == "Заданиена":
                        if msg.reply_markup.inline_keyboard:
                            for r in msg.reply_markup.inline_keyboard:
                                if r[0].url:
                                    try:
                                        await msg.click(0,0)
                                        name = r[0].url.removeprefix("https://t.me/")
                                        try:
                                            name = name[0:name.index("?")]
                                        except:
                                            pass



                                        for i in range(2):
                                            try:
                                                await bot.send_message(name, "/start")
                                                await sleep(0.7)
                                                async for msg in bot.get_chat_history(name, limit=1):
                                                    await bot.forward_messages(bots_id[0],msg.chat.id,[msg.id])
                                                    await msg.chat.mute()
                                                    await sleep(0.1)
                                                    await msg.chat.archive()
                                                    await bot.send_message(log_group, f"BM: @{name}")
                                            except:
                                                pass
                                    except:
                                        pass
                    elif ''.join(split[0:3])  == "✅Заданиевыполнено!":
                        await msg.click(0,0)
            await sleep(3.7)

class ViewMode:
    def __init__(self):
        pass
    async def run(self,bot):
        await bot.send_message(log_group, "ViewMode")
        await bot.send_message(bots_id[0], "👨‍💻 Заработать")
        await sleep(60)
        print("VMbot", bot.phone_number)
        for i_ in range(70):
            async for msg in bot.get_chat_history(bots_id[0],limit=1):
                split = msg.text.split()
                if msg.reply_markup:

                    if ''.join(split[0:3]) == "💰Выможете":
                        await sleep(0.5)
                        await msg.click(0,2)
                    elif ''.join(split[0:3]) == "Чтобыполучатьграмм,":
                        await sleep(0.5)
                        await msg.click(0,0)
                    elif ''.join(split[0:3]) == "💰Вамначислено":
                        await sleep(0.5)
                        await msg.click(0, 0)
                        await bot.send_message(log_group,f"VM: {' '.join(split[0:5])}")
                if "❌ Больше нет постов для просмотра." == msg.text or "❌ Нету доступных заданий" == msg.text or ''.join(split[0:3]) == "⏳Ошибка:Слишком":
                    f"VM: {msg.text}"
                    return -2
                await sleep(1)
        return 0

class ViewMCMode:
    def __init__(self):
        pass
    async def run(self,bot):
        try:
            await bot.send_message(log_group, "ViewMode MC")
            print(f"VM MC: {bot.phone_number}")
            await bot.send_message(bots_id[1],"/start 6470140273")
            await sleep(20)
            for i in range(70):
                async for msg in bot.get_chat_history(bots_id[1], limit=1):
                    split = msg.text.split()
                    if msg.reply_markup:
                        if ''.join(split[0:3]) == "💎PRMIT":
                            await msg.click(0, 0)
                            await sleep(1)
                        elif ''.join(split[0:3]) == "💰Выможете":
                            await msg.click(0, 5)
                            await sleep(7)
                        elif ''.join(split[0:3]) == "👀Просмотрелипост?":
                            await msg.click(1, 0)
                        elif ''.join(split[0:3]) == "Наданныймомент":
                            return -3
                await sleep(7)
        except:
            pass
class SubMode:
    def __init__(self):
        self.logs = open("subs.log", "a")
        self.num = 0
        self.sleep = True


    async def run(self,bot):
        await bot.get_chat(log_group)
        await bot.send_message(log_group, "SubMode")
        if bot.phone_number == phones[0]:
            await bot.send_message("sanpiar",'''📈 Накрутка подписчеков на тг канал:

100 - 30 руб 💸
250 - 75 руб 💸
500 - 150 руб 💸
1000 - 300 руб 💸
    
Писать в лс, постояным клиентам скидки🤑''')
            await sleep(60)
        if True:
            self.num = 0
            print("SMbot", bot.phone_number)
            for i_ in range(4):
                await bot.send_message(bots_id[0], "👨‍💻 Заработать")
                await sleep(20)
                async for msg in bot.get_chat_history(bots_id[0],limit=1):
                    try:
                        split = msg.text.split()
                        if ''.join(split[0:3]) == "💰Выможете":
                            try:
                                await sleep(0.5)
                                await msg.click(0,min(1,max(0,random.randint(0,1))))
                            except:
                                pass
                        elif ''.join(split[0:3]) == "Нажмитенакнопки,":
                            await sleep(0.5)
                            if msg.reply_markup:
                                if msg.reply_markup.inline_keyboard:
                                    i = 0
                                    for r in msg.reply_markup.inline_keyboard:
                                        if r[0].url and i <= 4:
                                            try:
                                                await sleep(4)
                                                i +=1
                                                jchat = await bot.join_chat(r[0].url)
                                                print(lgreen,f"Подписался на канал",clear)
                                                try:
                                                    await sleep(3)
                                                    await jchat.mute()
                                                    await sleep(1)
                                                    await jchat.archive()
                                                    await bot.send_message(log_group,f"SM: {r[0].url}")
                                                except:
                                                    pass
                                                try:
                                                    self.logs.write(f"{bot.phone_number}, {jchat.id}, {time()}, {jchat.title}\n")
                                                    self.logs.flush()
                                                except:
                                                    pass
                                                try:
                                                    await bot.request_callback_answer(msg.chat.id,msg.id,r[1].callback_data)
                                                except:
                                                    try:
                                                        await msg.click(0,i)
                                                    except:
                                                        pass
                                                await sleep(3)
                                                await bot.send_message(log_group,f"sub {i}")
                                                print("sleep 60s")
                                                await sleep(60)
                                            except FloodWait as e:
                                                await bot.request_callback_answer(msg.chat.id, msg.id, r[1].callback_data)
                                                print(red,"FloodWait",e.value//70,"m",clear)
                                                await bot.send_message(log_group,f"FloodWait {e.value//60} m")
                                                return -1
                                            except:
                                                await bot.request_callback_answer(msg.chat.id, msg.id, r[1].callback_data)
                                                self.sleep = False
                    except:
                        passd
            if self.sleep:
                await sleep(5)
            self.sleep = True
async def main(bot):
    print(bot.phone_number)
    await bot.send_message(log_group, "START FARM")
    while True:

        modes = [SubMode(), ViewMode()]
        mode = random.randint(0, 1)

        await sleep(3)
        for i_ in range(3):
            ret = await modes[mode].run(bot)
            if ret == -1:
                mode = random.randint(1,1)
            elif ret == -2:
                    mode = 0
            elif ret == -3:
                mode = random.choice([0,1])
            else:
                mode = random.randint(0, 1)
        st = random.randint(20,50)
async def mainRun():
    tasks = []
    for bot in bots:
        await bot.start()
        tasks.append(asyncio.create_task(main(bot)))
    for t in tasks:
        await t
    #await main(bots[0])


asyncio.run(mainRun())