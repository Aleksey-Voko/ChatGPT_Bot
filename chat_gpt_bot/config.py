import os


BOT_TOKEN = os.getenv('BOT_TOKEN')

DOMAIN = os.getenv('DOMAIN')
WEBHOOK_HOST = f'https://{DOMAIN}'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

WORKS_CHATS = [
    os.getenv('CHAT_ID'),
    os.getenv('ACHAT_ID'),
    os.getenv('VCHAT_ID'),
    os.getenv('SCHAT_ID'),
]

# AI
AI_KEY = os.getenv('AI_KEY')
MODEL = 'gpt-3.5-turbo'
