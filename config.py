# ©️ DKBOTZ or https://t.me/DKBOTZ
# Coded By https://t.me/DKBOTZHELP 
# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", '18076374')) #API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", '17d273ec3475c2c171d9122fd079774c') #API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN", '6710510477:AAE3YFDMHWT3d6prygYFzlc285OmpQPpZB0') # Bot token from @BotFather
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split(",")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", 'cluster0')
DATABASE_URL = os.environ.get("DATABASE_URL", 'mongodb+srv://aaroha:aaroha@cluster0.b73vc2y.mongodb.net/?retryWrites=true&w=majority') # mongodb uri from https://www.mongodb.com/
OWNER_ID =  int(os.environ.get("OWNER_ID", '6588740534')) # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(6588740534)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002050926827")) # log channel for information about users
UPDATE_CHANNEL = int(os.environ.get("UPDATE_CHANNEL", "-1002131551627")) # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "True" 


# SHORTNER

SHORTNER_LINK = os.environ.get("SHORTNER_LINK", 'ez4short.xyz')
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", 'https://t.me/ez4short_official')
