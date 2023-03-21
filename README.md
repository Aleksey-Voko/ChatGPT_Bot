# ChatGPT Bot  

[![wakatime](https://wakatime.com/badge/github/Aleksey-Voko/ChatGPT_Bot.svg)](https://wakatime.com/badge/github/Aleksey-Voko/ChatGPT_Bot)

Telegram-bot (Python, [aiogram](https://aiogram.dev/), [OpenAI API](https://platform.openai.com/docs/api-reference/))

The simplest telegram bot for dialogue with ChatGPT.  
Most capable GPT-3.5 model ([gpt-3.5-turbo](https://platform.openai.com/docs/models/gpt-3-5)) and optimized for chat.  
Requires OpenAI API token for authorization.  
Prepared for deployment on [Railway](https://railway.app/)  

### [Rapid deployment on Railway](https://railway.app/template/-S3lVz?referralCode=jUyx2Z)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/-S3lVz?referralCode=jUyx2Z)

#### Variables

- `BOT_TOKEN` - Telegram Bot Token
- `CHAT_ID` - ID of the telegram chat where the bot is allowed to work.
- `AI_KEY` - OpenAI API Token
- `DOMAIN` - URL with the name of the application. After deployment, go to the `Settings` of the project and copy the domain from the `Domains` section. It should be like `worker-production-XXXX.up.railway.app`. This will be a value for your `DOMAIN` variable.
