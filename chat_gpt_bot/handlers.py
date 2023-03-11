import openai
from aiogram import types

from chat_gpt_bot.config import (WORKS_CHATS, MODEL, TEMPERATURE, MAX_TOKENS,
                                 TOP_P, FREQUENCY_PENALTY, PRESENCE_PENALTY,
                                 AI_KEY)
from chat_gpt_bot.dispatcher import dp


openai.api_key = AI_KEY


def get_ai_answer(question):
    response = openai.Completion.create(
        model=MODEL,
        prompt=question,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY,
    )

    return response['choices'][0]['text']


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def text_reply(message: types.Message):
    if str(message.chat.id) in WORKS_CHATS:
        if message.text.startswith('+'):
            await message.answer(get_ai_answer(message.text))
    else:
        await message.answer('Invalid chat ID')
