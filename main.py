import telebot
import dataBase
from telebot import types
from telegram import ParseMode
#token connect.
bad=('token bot in telegram. api')
bot=telebot.TeleBot(bad)
db = dataBase.DataBase()
db.createEventsTable()
users = {}
#start code.
@bot.message_handler(commands=['start'])
def start(message):
    start_handler = f"<b>Hello {message.from_user.first_name}, in Airdrop $DBG </b>"
    print(start_handler)
    bot.send_message(message.chat.id,start_handler,parse_mode='html',reply_markup=kb1)
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text=='NEXT ✅':
        bot.send_message(message.chat.id,DT,reply_markup=kb2)
    if message.text=='DONE ✅':
        bot.send_message(message.chat.id,TX,parse_mode='HTML', reply_markup=kb3)
    if message.text=='Submit Details ✍':
        bot.send_message(message.chat.id,TT,parse_mode='html')
        bot.register_next_step_handler(message, get_name_Instagram)
#data storage function.
def get_name_Instagram(message):
    global  users;
    users[message.from_user.id] ={}
    users[message.from_user.id]['Instagram'] = message.text
    bot.send_message(message.from_user.id,TTG,parse_mode='html')
    bot.register_next_step_handler(message, get_name_Telegram)

def get_name_Telegram(message):
    global users;
    users[message.from_user.id]['Telegram'] = message.text
    bot.send_message(message.from_user.id,TW)
    bot.register_next_step_handler(message, get_address_wallet)

def get_address_wallet(message):
    global users;
    users[message.from_user.id]['DGB'] = message.text
    bot.send_message(message.from_user.id,TY,parse_mode='html')
    bot.register_next_step_handler(message, get_verification_code)

def get_verification_code(message):
    global users;
    try:
        datestr = message.text;
        datestrcpy = datestr
        datestr = datestr.replace(".", "")
        datestr = datestr.replace("-", "")
        datestr = datestr.replace(":", "")
        users[message.from_user.id]['code'] = int(datestr)
        db.addEvent(message.from_user.id,  users[message.from_user.id]['Instagram'],users[message.from_user.id]['Telegram']
                    , users[message.from_user.id]['DGB'], users[message.from_user.id]['code'])
        bot.send_message(message.from_user.id,
                         "\nYour registration details 📝\n \n1-Your username Instagram: 🔗\n " +
                         users[message.from_user.id]['Instagram'] + "\n2-Your username Telegram: 🔗 ️\n " +
                         users[message.from_user.id]['Telegram'] + "\n3-Your wallet DGB:🛄 \n " +
                         users[message.from_user.id]['DGB'] + "\n4-Your code: 🔥️ \n " + datestrcpy)
        bot.send_message(message.from_user.id,text_end)
    except Exception:
        bot.send_message(message.from_user.id,T_R)
        bot.register_next_step_handler(message, get_verification_code)
#Buttons.
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
#check Run Code.

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
T_R='Enter the number you want to claim the prize'
#Help contact Support
@bot.message_handler(commands=['/help'])
def send_message(message):
    bot.send_message(message.chat.id,'If you encounter any problem with the registration, contact the bot developer @KimoKF9')
bot.polling()    
