# ChatGPT Bot  

[![wakatime](https://wakatime.com/badge/github/Aleksey-Voko/ChatGPT_Bot.svg)](https://wakatime.com/badge/github/Aleksey-Voko/ChatGPT_Bot)

Telegram-bot (Python, [aiogram](https://aiogram.dev/), [OpenAI API](https://platform.openai.com/docs/api-reference/))

The simplest telegram bot for dialogue with ChatGPT.  
Requires OpenAI API token for authorization.  
Prepared for deployment on [Railway](https://railway.app/)  

### [Deploy on Railway](https://railway.app/template/U-zkJQ?referralCode=jUyx2Z)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/U-zkJQ?referralCode=jUyx2Z)

#### Variables

`BOT_TOKEN` - Telegram Bot Token  
`RAILWAY_APP_NAME` - Part of the URL with the name of the application (you can get it when you deploy)  
`CHAT_ID` - ID of the telegram chat where the bot is allowed to work. Must be added to the list `WORKS_CHATS` in the file [`config.py`](chat_gpt_bot/config.py). You can add several.  
`AI_KEY` - OpenAI API Token
