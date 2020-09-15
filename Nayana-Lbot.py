
!pip3 install adafruit-io
from Adafruit_IO import RequestError, Client, Feed
from Adafruit_IO import Data
username = 'nreddy'
code = 'aio_APSH68qM59Xnmtcl2XfGNuWXCTfF'
aio = Client(username,code)

!pip install python-telegram-bot
from telegram.ext import Updater,CommandHandler
import requests

def get_url():
    contents = requests.get('https://rb.gy/momsaj').json()
    url = contents['url']
    return url

def on(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'light is turning on'
    pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Green_sphere.svg/1024px-Green_sphere.svg.png'
    bot.send_message(chat_id,txt)
    bot.send_photo(chat_id,pic)
    value = Data(value=1)
    value_send = aio.create_data('lit',value)

def off(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'light is turning off'
    pic = 'https://upload.wikimedia.org/Wikipedia/commons/thumb/d/de/Red_sphere_shaded_lightsource_top_right.svg/1024p'
    bot.send_message(chat_id,txt)
    bot.send_photo(chat_id,pic)
    value = Data(value=0)
    value_send = aio.create_data('lit',value)

u = Updater('1350219392:AAGU0EVB55SmJOVHi4S7KuHe0Fe2q2mrL7A')
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()
