import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import health_factor
from tracker import get_prices
import tracker

telegram_bot_token = constants.telegram_bot_token

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"

    # message2 = 'AAVE Health Factor:\n{health_factor}'
    context.bot.send_message(chat_id=chat_id, text=message)
    # context.bot.send_message(chat_id=chat_id, text=message2)

def health(update, context):
    chat_id = update.effective_chat.id
    message = ""

    message += f"AAVE HEALTH FACTOR: \n\n {health_factor()}"

    context.bot.send_message(chat_id=chat_id, text=message)

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("health", health))
updater.start_polling()



