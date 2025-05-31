#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ
8
API_ID = int(environ.get("API_ID", "29813238"))
API_HASH = environ.get("API_HASH", "51178112667e5c4df22421000d62e9fc")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "6335130816"))
CREDIT = "𝄟⃝‌🐬chetan𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '6335130816').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
