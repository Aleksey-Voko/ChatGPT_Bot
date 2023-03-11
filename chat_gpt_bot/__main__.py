import logging

from aiogram.utils.executor import start_polling

from chat_gpt_bot.handlers import *


def main():
    logging.basicConfig(level=logging.INFO)

    start_polling(dp, skip_updates=True)  # TODO: for debug


if __name__ == '__main__':
    main()
