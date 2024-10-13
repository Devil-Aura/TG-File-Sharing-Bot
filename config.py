#https://t.me/abidabdullah199

import os
import logging
from logging.handlers import RotatingFileHandler


#Bot Variables
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "22768311"))
API_HASH = os.environ.get("API_HASH", "702d8884f48b42e865425391432b3794")
OWNER_ID = int(os.environ.get("OWNER_ID", "6040503076"))

#Database Variables
DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://gamerspyer2023:HpcyTyfkjBYvLGi4@cluster0.dogml.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#your channel id where the file will be stored as log format
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002436399053")

#Force Sub Channel id [Your Telegram Channels id] 
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1001999825163"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002059068082"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", ""))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", ""))
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Whatt!You haven't join worlds best channel ever create in human existence, Join Now! All of Them, Smash them")


#Extra
#if you what you are doing then you can change port also
PORT = os.environ.get("PORT", "8080") 
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
#if you set protect content to true no one can forward messages from your bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False


START_MSG = os.environ.get("START_MESSAGE", "Hello {first} I Am A File Sharing Bot Of @CrunchyRollOfficialChannel")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5296584067").split()): #your owner id paste here also, if you have more then add in split
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None) # if you want to add custom caption copy this > "Your Caption" as replace of None

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True' #keep if none thats better but if you know what to do then as you wish

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "You can't send me Direct Message, I'm Only File Share Bot of @CrunchyRollOfficialChannel."

ADMINS.append(OWNER_ID)
ADMINS.append(6040503076) #put owner id here also 

LOG_FILE_NAME = "tg-file-sharing-bot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
