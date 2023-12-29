

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "2646548"))
API_HASH = os.environ.get("API_HASH", "72e5b96d9aa943df98ec71241b11c7ac")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6829233649:AAHq1q0_XJtoRO5IFNL1QixvYNuGv_YAx1w")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("872623545")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Jayraj8833")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Jayraj8833:Jayraj8833@jayraj8833.9hhl5sa.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "872623545")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(your_owner_id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-4077701785")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-4077701785") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSz6U4M8sK2h8P6pYH9e_HBG5cDvBzZ1zAe5Q&usqp=CAU') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
