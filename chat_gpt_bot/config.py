import os


BOT_TOKEN = os.getenv('BOT_TOKEN')

RAILWAY_APP_NAME = os.getenv('RAILWAY_APP_NAME')

WEBHOOK_HOST = f'https://{RAILWAY_APP_NAME}.railway.app'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

WORKS_CHATS = [
    os.getenv('ACHAT_ID'),
    os.getenv('VCHAT_ID'),
    os.getenv('SCHAT_ID'),
    os.getenv('MCHAT_ID'),
]

# AI
AI_KEY = os.getenv('AI_KEY')
MODEL = 'text-davinci-003'
TEMPERATURE = 0.5
MAX_TOKENS = 1000
TOP_P = 1.0
FREQUENCY_PENALTY = 0.5
PRESENCE_PENALTY = 0.0
