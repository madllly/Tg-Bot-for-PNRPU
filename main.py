# - *- coding: utf- 8 - *-

import telebot
from datetime import datetime, timedelta
from telebot import types
import sqlite3
from config import BOT_TOKEN




def tg_bot(token):
    bot = telebot.TeleBot(token)
    conn = sqlite3.connect('Users.db', check_same_thread=False)
    cursor = conn.cursor()

    def db_insert(id, join_group):
        cursor.execute('INSERT INTO users (id, join_group) VALUES (?, ?)',
                       (id, join_group))
        conn.commit()

    def dell_message(call):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    @bot.message_handler(commands=['start'])
    def get_text_messages(message):
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton('АСУ-21', callback_data='ASY-21')
        item2 = types.InlineKeyboardButton('АТПП-21', callback_data='ATPP-21')
        item3 = types.InlineKeyboardButton('ПГС-21', callback_data='PGS-21')
        item4 = types.InlineKeyboardButton('АСУ-20', callback_data='ASY-20')
        item5 = types.InlineKeyboardButton('ПГС-20', callback_data='PGS-20')
        item6 = types.InlineKeyboardButton('АТПП-20', callback_data='ATPP-20')
        item7 = types.InlineKeyboardButton('ЭС-20', callback_data='ES-20')
        item8 = types.InlineKeyboardButton('АСУ-19', callback_data='ASY-19')
        item9 = types.InlineKeyboardButton('АТПП-19', callback_data='ATPP-19')
        item10 = types.InlineKeyboardButton('ЭС-19', callback_data='ES-19')
        item11 = types.InlineKeyboardButton('АСУ-18', callback_data='ASY-18')
        item12 = types.InlineKeyboardButton('АТПП-18', callback_data='ATPP-18')
        item13 = types.InlineKeyboardButton('ЭС-18', callback_data='ES-18')
        markup.add(item1, item2, item3).add(item4, item5, item6).add(item7, item8, item9).add(item10, item11,
                                                                                              item12).add(item13)
        bot.send_message(message.from_user.id,
                         'Привет! Я бот, который напомнит тебе расписание занятий!\nИз какой ты группы?',
                         reply_markup=markup)

    def get_ras(call, i=0, word='Сегодня'):
        offset = datetime.today().weekday() + i

        if offset == 0:
            d = datetime.now() + timedelta(days=i)
            bot.send_message(call.message.chat.id, f" {word} {d.strftime('%d-%m-%Y')}")
            with sqlite3.connect('Users.db') as con:
                cur = con.cursor()
                id = call.from_user.id
                cur.execute(f"SELECT * FROM users WHERE id = {id}")
                group = cur.fetchone()
                group = group[1]

            with sqlite3.connect('Rasp.db') as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM '{group}' WHERE day = 'Понедельник' AND disc IS NOT NULL")
                result = cur.fetchall()
                if len(result) < 1:
                    bot.send_message(call.message.chat.id, 'Пар нет!')
                else:
                    for res in result:
                        bot.send_message(call.message.chat.id, res[1] + ') ' + res[2] + '\n' + res[3])

        if offset == 1:
            d = datetime.now() + timedelta(days=i)
            bot.send_message(call.message.chat.id, f"{word} {d.strftime('%d-%m-%Y')}")
            with sqlite3.connect('Users.db') as con:
                cur = con.cursor()
                id = call.from_user.id
                cur.execute(f"SELECT * FROM users WHERE id = {id}")
                group = cur.fetchone()
                group = group[1]

            with sqlite3.connect('Rasp.db') as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM '{group}' WHERE day = 'Вторник' AND disc IS NOT NULL")
                result = cur.fetchall()

                if len(result) < 1:
                    bot.send_message(call.message.chat.id, 'Пар нет!')
                else:
                    for res in result:
                        bot.send_message(call.message.chat.id, res[1] + ') ' + res[2] + '\n' + res[3])

        if offset == 2:
            d = datetime.now() + timedelta(days=i)
            bot.send_message(call.message.chat.id, f"{word} {d.strftime('%d-%m-%Y %H:%M')}")
            with sqlite3.connect('Users.db') as con:
                cur = con.cursor()
                id = call.from_user.id
                cur.execute(f"SELECT * FROM users WHERE id = {id}")
                group = cur.fetchone()
                group = group[1]

            with sqlite3.connect('Rasp.db') as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM '{group}' WHERE day = 'Среда' AND disc IS NOT NULL")
                result = cur.fetchall()
                if len(result) < 1:
                    bot.send_message(call.message.chat.id, 'Пар нет!')
                else:
                    for res in result:
                        bot.send_message(call.message.chat.id, res[1] + ') ' + res[2] + '\n' + res[3])

        if offset == 3:
            d = datetime.now() + timedelta(days=i)
            bot.send_message(call.message.chat.id, f"{word} {d.strftime('%d-%m-%Y')}")
            with sqlite3.connect('Users.db') as con:
                cur = con.cursor()
                id = call.from_user.id
                cur.execute(f"SELECT * FROM users WHERE id = {id}")
                group = cur.fetchone()
                group = group[1]

            with sqlite3.connect('Rasp.db') as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM '{group}' WHERE day = 'Четверг' AND disc IS NOT NULL")
                result = cur.fetchall()
                if len(result) < 1:
                    bot.send_message(call.message.chat.id, 'Пар нет!')
                else:
                    for res in result:
                        bot.send_message(call.message.chat.id, res[1] + ') ' + res[2] + '\n' + res[3])

        if offset == 4:
            d = datetime.now() + timedelta(days=i)
            bot.send_message(call.message.chat.id, f"{word} {d.strftime('%d-%m-%Y')}")
            with sqlite3.connect('Users.db') as con:
                cur = con.cursor()
                id = call.from_user.id
                cur.execute(f"SELECT * FROM users WHERE id = {id}")
                group = cur.fetchone()
                group = group[1]

            with sqlite3.connect('Rasp.db') as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM '{group}' WHERE day = 'Пятница' AND disc IS NOT NULL")
                result = cur.fetchall()
                if len(result) < 1:
                    bot.send_message(call.message.chat.id, 'Пар нет!')
                else:
                    for res in result:
                        bot.send_message(call.message.chat.id, res[1] + ') ' + res[2] + '\n' + res[3])

        if offset == 5:
            d = datetime.now() + timedelta(days=i)
            bot.send_message(call.message.chat.id, f"{word} {d.strftime('%d-%m-%Y')}")
            with sqlite3.connect('Users.db') as con:
                cur = con.cursor()
                id = call.from_user.id
                cur.execute(f"SELECT * FROM users WHERE id = {id}")
                group = cur.fetchone()
                group = group[1]

            with sqlite3.connect('Rasp.db') as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM '{group}' WHERE day = 'Суббота' AND disc IS NOT NULL")
                result = cur.fetchall()
                if len(result) < 1:
                    bot.send_message(call.message.chat.id, 'Пар нет!')
                else:
                    for res in result:
                        bot.send_message(call.message.chat.id, res[1] + ') ' + res[2] + '\n' + res[3])

    @bot.message_handler(commands=['delete'])
    def delete(message):
        us_id = message.from_user.id
        cursor.execute(f"DELETE FROM users WHERE id = {us_id}")
        conn.commit()

    @bot.callback_query_handler(func=lambda call: True)
    def answer(call):
        if call.data == 'ASY-21' or call.data == 'ASY-21' or call.data == 'ASY-20' or call.data == 'ASY-19' or call.data == 'ASY-18' or call.data == 'ATPP-21' or call.data == 'ATPP-20' or call.data == 'ATPP-19' or call.data == 'ATPP-18' or call.data == 'ES-20' or call.data == 'ES-19' or call.data == 'ES-18' or call.data == 'PGS-20' or call.data == 'PGS-21':
            us_id = call.from_user.id
            us_join = call.data

            cursor.execute(f"SELECT id FROM users WHERE id = '{us_id}'")
            data = cursor.fetchone()
            if data is None:
                db_insert(id=us_id, join_group=us_join)
            else:
                cursor.execute(f"UPDATE users SET join_group = '{us_join}' WHERE id = '{us_id}'")
                conn.commit()

            bot.send_message(call.message.chat.id,
                             f'Я запомнил, что ты в группе: {us_join}.')
            dell_message(call)

            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton('Сегодня', callback_data='today')
            item2 = types.InlineKeyboardButton('Завтра', callback_data='tomorrow')
            item3 = types.InlineKeyboardButton('Смена группы', callback_data='change')
            markup.add(item1).add(item2).add(item3)
            bot.send_message(call.message.chat.id, 'На всю неделю я расписание не выдам, иначе ты больше не вернешься',
                             reply_markup=markup)
        elif call.data == 'today':
            dell_message(call)
            get_ras(call)
            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton('Сегодня', callback_data='today')
            item2 = types.InlineKeyboardButton('Завтра', callback_data='tomorrow')
            item3 = types.InlineKeyboardButton('Смена группы', callback_data='change')
            markup.add(item1).add(item2).add(item3)
            bot.send_message(call.message.chat.id, 'На всю неделю я расписание не выдам, иначе ты больше не вернешься',
                             reply_markup=markup)

        elif call.data == 'tomorrow':
            dell_message(call)
            get_ras(call, i=1, word='Завтра')
            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton('Сегодня', callback_data='today')
            item2 = types.InlineKeyboardButton('Завтра', callback_data='tomorrow')
            item3 = types.InlineKeyboardButton('Смена группы', callback_data='change')
            markup.add(item1).add(item2).add(item3)
            bot.send_message(call.message.chat.id, 'На всю неделю я расписание не выдам, иначе ты больше не вернешься',
                             reply_markup=markup)
        elif call.data == 'change':
            dell_message(call)
            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton('АСУ-21', callback_data='ASY-21')
            item2 = types.InlineKeyboardButton('АТПП-21', callback_data='ATPP-21')
            item3 = types.InlineKeyboardButton('ПГС-21', callback_data='PGS-21')
            item4 = types.InlineKeyboardButton('АСУ-20', callback_data='ASY-20')
            item5 = types.InlineKeyboardButton('ПГС-20', callback_data='PGS-20')
            item6 = types.InlineKeyboardButton('АТПП-20', callback_data='ATPP-20')
            item7 = types.InlineKeyboardButton('ЭС-20', callback_data='ES-20')
            item8 = types.InlineKeyboardButton('АСУ-19', callback_data='ASY-19')
            item9 = types.InlineKeyboardButton('АТПП-19', callback_data='ATPP-19')
            item10 = types.InlineKeyboardButton('ЭС-19', callback_data='ES-19')
            item11 = types.InlineKeyboardButton('АСУ-18', callback_data='ASY-18')
            item12 = types.InlineKeyboardButton('АТПП-18', callback_data='ATPP-18')
            item13 = types.InlineKeyboardButton('ЭС-18', callback_data='ES-18')
            markup.add(item1, item2, item3).add(item4, item5, item6).add(item7, item8, item9).add(item10, item11,
                                                                                                  item12).add(item13)
            bot.send_message(call.from_user.id,
                             'Привет! Я бот, который напомнит тебе расписание занятий!\nИз какой ты группы?',
                             reply_markup=markup)

    bot.skip_pending = True
    bot.polling(none_stop=True)


if __name__ == "__main__":
    tg_bot(BOT_TOKEN)
