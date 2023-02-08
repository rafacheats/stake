import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from cfg import Minas, Horas, list

bot = Bot(token='5746821052:AAFnUoylB8xD8j6VO7WCANU7xcFo4FJG8Ck')
dp = Dispatcher(bot)

#==================================== TEXTOS ========================================

msginicio = "🔥 Olá, tudo bem? este é o menu principal \n \n 🤖 Nosso robô faz analise das minas na casa de aposta Stake e envia os sinais quando você desejar aqui no telegram \n \n 🚀 Para começar a ganhar, você  só precisa clicar em configurações, ajustar os parametros e apertar em jogar! \n \n 💻 Basta seguir os sinais do robô e começar a lucrar"
msgfim = "⭐️ Robô parado, esperamos que tenha um bom resultado\n🤖 Quando quiser voltar basta selecionar alguma opção abaixo"
msgcfg = "1"

#==================================== BOTOES ========================================

btnjogar = KeyboardButton('▶️ Jogar')
btnconfig = KeyboardButton('⚙️ Configurações')
btnjogardnv = KeyboardButton('▶️ Próxima rodada')
btnvoltar = KeyboardButton('🚫 Parar')

menuinicio = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnjogar).add(btnconfig)
menujogo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnjogardnv).add(btnvoltar)
menuvoltar = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnvoltar)

#====================================================================================

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
   await message.reply(msginicio, reply_markup=menuinicio)


@dp.message_handler()
async def kb_answer(message: types.Message):
   if message.text == '▶️ Jogar':
      await message.answer("⭐️ Entrada Confirmada \n💣 Minas: " + Minas + " \n😎 N° Máx de bets: 3 \n⏱ Válido até : " + Horas +" \n \n"+ random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" +random.choice(list) + "" + random.choice(list) +"\n" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "\n" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "\n" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "\n" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "\n", reply_markup=menujogo)
   elif message.text == '⚙️ Configurações':
      await message.answer(msgcfg, reply_markup=menuvoltar)
   elif message.text == '🚫 Parar':
      await message.answer(msgfim, reply_markup=menuinicio)
   elif message.text == '▶️ Próxima rodada':
      await message.answer("⭐️ Entrada Confirmada \n💣 Minas: " + Minas + " \n😎 N° Máx de bets: 3 \n⏱ Válido até : " + Horas +" \n \n"+ random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" +random.choice(list) + "" + random.choice(list) +"\n" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "\n" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "\n" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "\n" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "" + random.choice(list) + "\n", reply_markup=menujogo)


executor.start_polling(dp)
