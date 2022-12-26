import logging
from telegram.ext import Updater, CommandHandler
import telegram
import logging

# Configure Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

# Solicitar TOKEN
TOKEN = "5783949221:AAFbJD3VPpObDKZsuJMTfSGmyoYDJhSaEPo"

def daily_commands(update,context):
  chat_id = update.effective_chat['id']
  title = update.effective_chat['title']
  name = update.effective_user['first_name']
  logger.info(
        f"El usuario {name}, ha puesto una solicitud de daily Tasks en el chat {title} (id = {chat_id} )")
  context.bot.sendMessage(
        chat_id="-819161372", parse_mode="HTML", text="Starting Daily Tasks Spreads OSL")
  context.bot.sendMessage(
        chat_id="-819161372", parse_mode="HTML", text="/rfq_spreads@Spreads_rfq_bot")
  context.bot.sendMessage(
        chat_id="-819161372", parse_mode="HTML", text="/exch_spreads@Spreads_exch_bot")
  context.bot.sendMessage(
        chat_id="-819161372", parse_mode="HTML", text="/exch_spread_tracker_all_coins@spread_all_coins_exch_bot")
  context.bot.sendMessage(
        chat_id="-819161372", parse_mode="HTML", text="/rfq_spread_tracker_all_coins@spread_all_coins_rfq_bot")
  
if __name__ == "__main__":
    # Obtenemos la informacion del Bot
    my_bot = telegram.Bot(token=TOKEN)

# Enlazamos nuestro updater con nuestro bot
updater = Updater(my_bot.token, use_context=True)

# Creamos un despachador
dp = updater.dispatcher
                         
 
dp.add_handler(CommandHandler("daily_tasks", daily_commands ))
# Pregunta al bot si hay nuevos msjs
updater.start_polling()
                           
print("BOT CARGADO")
                           
updater.idle()  # finalizar el bot ctrl+c
