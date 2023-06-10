import telebot
import sqlite3
from telebot import types
from telegram import ParseMode
#token connect
kf9=('5505740829:AAGUcPX7mo4MxV9riN9JzYwQVRQARAntPss')
bot=telebot.TeleBot(kf9)
x=1
#start code
@bot.message_handler(commands=['start'])
def start(message):
    start_handler = f"<b>Hello {message.from_user.first_name}, in Airdrop $DBG </b>"
    bot.send_message(message.chat.id,start_handler,reply_markup=kb1,parse_mode='html')
#    sql.execute("INSERT INTO users VALUES(?,?);",x, message.from_user.username)
#    db.commit()
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text=='help':
        bot.send_message(message.chat.id,T_R)
    if message.text=='NEXT ✅':
        bot.send_message(message.chat.id,DT,reply_markup=kb2)
    if message.text=='DONE ✅':
        bot.send_message(message.chat.id,TX,parse_mode='HTML', reply_markup=kb3)
    if message.text=='Submit Details ✍':
        bot.send_message(message.chat.id,TT,parse_mode='html')
        #bot.register_next_step_handler(message, get_name_Instagram)
#Buttons
kb1=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
k1 = types.KeyboardButton('NEXT ✅')
kb1.add(k1)
kb2=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
k2=types.KeyboardButton('DONE ✅')
kb2.add(k2)
kb3=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
k3=types.KeyboardButton('Submit Details ✍')
kb3.add(k3)
#kb3=types.ReplyKeyboardRemove(one_time_keyboard=True)
#check Run Code 
print('KimoKF9™ ©')
#hyperlink
t="<a href='https://www.instagram.com/kimo.kf9/'>Instagram</a>"
o="<a href='https://t.me/airdrops_DGB/'>Telegram Group</a>"
c="<a href='https://t.me/ItechnicalworldT/'>Channel</a>"
y="<a href='https://youtube.com/channel/UCpqxgVU3lB9WmCxixpUYAcQ/'>Youtube</a>"
nue=' f"<b>wow{message.from_user.first_name}wow</b>"'
#tasks
TX='Complete the tasks below! \n\nAll the tasks are mandatory \n🔰Join our 'f'{o}'' and 'f'{c}'' \n🔰Follow our 'f'{t}'' page.  \n🔰Follow 'f'{y}' ' channel. \n\n \nClick "Submit Details"'
#Definition texts for this bot
DT="💰 Airdrop Reward: $DGB.\n🥇 Winners: For the first 500 follower. \n 🎉The rest is 200 random distribution."
TW="🔰Submit Your DGB Address (DigiByte) \n You can create an address at Trust wallet."
TT='🔰Follow our 'f'{t} page & retweet the pinned post\nSubmit your Instagram profile username (Ex:@KimoKF9)'
TTG='🔰Joined our 'f'{o}'' and 'f'{c}''.\n Submit your Telegram username (Ex:@KimoKF9)'
TY='🔰Follow our 'f'{y}'' Channel. \nSubmit your YouTube channel username (Ex @KimoKF9)'
text_end='🌟🌟 Congratulations  🌟🌟\n \nThank you for joining the airdrop DGB, it will be distributed every week. \n\n⚠️ Note: If you submited any wrong information please click /start to resubmit correctly.'
Err='Wrong entry❎, re-enter'
T_R='If you encounter any problem with the registration, contact the bot developer @KimoKF9'

bot.polling()    
