import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27072582")

API_HASH = os.environ.get("API_HASH", "effc97551618eaf4d3bf7bfcdea40abb")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7485548967:AAHoA4V8k9yu-cLUGPia7kub3Xmt09PWPKs") 

FORCE_SUB = os.environ.get("FORCE_SUB", "THE_REBEL_SQUAD") 

DB_NAME = os.environ.get("DB_NAME","arifmagi42")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://arifmagi42:uCJN7ZVrchTeTD1I@rebel-bot.auuyp12.mongodb.net/?retryWrites=true&w=majority&appName=rebel-bot")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6126538092').split()]

PORT = os.environ.get("PORT", "8080")
