import telebot
from telebot import types
import time
import oper as opp
import op_kom as opp_km

TOKEN = "6147276946:AAG8Mo0UR9rredpOvGF4NIIFHN-JmmfyAcU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Рациональный"), types.KeyboardButton("Комплексный"))
    bot.send_message(message.chat.id, f"Привет🤝, {message.from_user.first_name}!\nВыбери режим работы калькулятора", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def keyboard_op(message):
    if message.text == "Рациональный":
        keyboard_op = types.ReplyKeyboardMarkup(resize_keyboard=True , one_time_keyboard=True)
        keyboard_op.add(types.KeyboardButton("+"),
                        types.KeyboardButton("-"), 
                        types.KeyboardButton("/"),
                        types.KeyboardButton("*"),
                        types.KeyboardButton("//"),
                        types.KeyboardButton("%")
                        )
        bot.send_message(message.chat.id, "Выберете опперацию", reply_markup=keyboard_op)
        bot.register_next_step_handler(message, operait_raz)
    elif message.text == "Комплексный":
        keyboard_op = types.ReplyKeyboardMarkup(resize_keyboard=True , one_time_keyboard=True)
        keyboard_op.add(types.KeyboardButton("+"),
                        types.KeyboardButton("-"), 
                        types.KeyboardButton("/"),
                        types.KeyboardButton("*"),
                        )
        bot.send_message(message.chat.id, "Выберете опперацию", reply_markup=keyboard_op)
        bot.register_next_step_handler(message, operait_kom)


def operait_raz(message):
    if message.text == "+":
        bot.send_message(message.from_user.id, 'Введите два числа чеерз пробел')
        bot.register_next_step_handler(message, opp.sumcalc)
    elif message.text == "-":
        bot.send_message(message.from_user.id, 'Введите два числа чеерз пробел')
        bot.register_next_step_handler(message, opp.minus)
    elif message.text == "*":
        bot.send_message(message.from_user.id, 'Введите два числа чеерз пробел')
        bot.register_next_step_handler(message, opp.multiply)
    elif message.text == "/":
        bot.send_message(message.from_user.id, 'Введите два числа чеерз пробел')
        bot.register_next_step_handler(message, opp.degree)
    elif message.text == "//":
        bot.send_message(message.from_user.id, 'Введите два числа чеерз пробел')
        bot.register_next_step_handler(message, opp.degree_integer)
    elif message.text == "%":
        bot.send_message(message.from_user.id, 'Введите два числа чеерз пробел')
        bot.register_next_step_handler(message, opp.degree_remainder)
    else:
        bot.send_message(message.from_user.id, 'Недоступная операция!')
        time.sleep(2)
        bot.register_next_step_handler(message, keyboard_op)

def operait_kom(message):
    if message.text == "+":
        bot.send_message(message.from_user.id, 'Введите два числа чеерз пробел')
        bot.register_next_step_handler(message, opp_km.sumcalc_kom)
    elif message.text == "-":
        bot.send_message(message.from_user.id, 'Введите два числа чеерз пробел')
        bot.register_next_step_handler(message, opp_km.minus_kom)
    elif message.text == "*":
        bot.send_message(message.from_user.id, 'Введите два числа чеерз пробел')
        bot.register_next_step_handler(message, opp_km.multiply_kom)
    elif message.text == "/":
        bot.send_message(message.from_user.id, 'Введите два числа чеерз пробел')
        bot.register_next_step_handler(message, opp_km.degree_kom)
    else:
        bot.send_message(message.from_user.id, 'Недоступная операция!')
        time.sleep(2)
        bot.register_next_step_handler(message, keyboard_op)





bot.polling(none_stop=True)