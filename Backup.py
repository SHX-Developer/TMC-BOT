from telebot import types, telebot
import sqlite3
import datetime
import time

import CONFIG

from BUTTONS import Buttons

from ENGLISH_BUTTONS import English_Buttons
from RUSSIAN_BUTTONS import Russian_Buttons


bot = telebot.TeleBot(CONFIG.TOKEN)



# DAYS

monday = "🗓  Monday"
tuesday = "🗓  Tuesday"
wednesday = "🗓  Wednesday"
thursday = "🗓  Thursday"
friday = "🗓  Friday"
saturday = "🗓  Saturday"

#  TEACHERS



Sathe_M = "👨‍🏫  Sathe M"
Pulatov_S = "👨‍🏫  Pulatov S"
Nurmatov_A = "👨‍🏫  Nurmatov A"
Kumar_A = "👨‍🏫  Kumar A"
Ismoilov_A = "👨‍🏫  Ismoilov A"
Bekov_S = "👨‍🏫  Bekov S"
Liayakath_Ali_Khan_S = "👨‍🏫  Liayakath Ali Khan S"
Raxmanova_I = "👨‍🏫  Raxmanova I"

# SUBJECTS

intro_to_study = "📚  Introduction to Study Skills"
communication = "📚  Communication"
intro_to_it = "📚  Introduction to IT"

project_management = "📚  Project Management"
java = "📚  Application Programming with Java"
database = "📚  Database Systems"

bus_communication_ict = "📚  Business Communication and ICT"
intro_to_management = "📚  Introduction to Management"
marketing_for_managers = "📚  Marketing for Managers"

hospitality_leisure = "📚  Marketing for Hospitality and Leisure"
ict_hospitality = "📚  ICT in the Hospitality and Leisure Industrial"
hotel_resort = "📚  International Hotel and Resort Management"

# TIMING

nine = "🕗  09:00 AM - 10:20 AM"
ten = "🕗  10:30 AM - 11:50 AM"
twelve = "🕗  12:00 PM - 13:20 PM"
one = "🕗  13:30 PM - 14:50 PM"
three = "🕗  15:00 PM - 16:20 PM"
four = "🕗  16:30 PM - 17:50 PM"

# ROOM

conference_hall = "🏫  Conference hall"

room_201 = "🏫  Room  -  201"
room_202 = "🏫  Room  -  202"
room_203 = "🏫  Room  -  203"
room_204 = "🏫  Room  -  204"
room_205 = "🏫  Room  -  205"
room_206 = "🏫  Room  -  206"
room_207 = "🏫  Room  -  207"
room_208 = "🏫  Room  -  208"
room_209 = "🏫  Room  -  209"

room_301 = "🏫  Room  -  301"
room_302 = "🏫  Room  -  302"
room_303 = "🏫  Room  -  303"
room_304 = "🏫  Room  -  304"
room_305 = "🏫  Room  -  305"
room_306 = "🏫  Room  -  306"
room_307 = "🏫  Room  -  307"
room_308 = "🏫  Room  -  308"
room_309 = "🏫  Room  -  309"

room_401 = "🏫  Room  -  401"
room_402 = "🏫  Room  -  402"
room_403 = "🏫  Room  -  403"
room_404 = "🏫  Room  -  404"
room_405 = "🏫  Room  -  405"
room_406 = "🏫  Room  -  406"
room_407 = "🏫  Room  -  407"
room_408 = "🏫  Room  -  408"
room_409 = "🏫  Room  -  409"

room_501 = "🏫  Room  -  501"
room_502 = "🏫  Room  -  502"
room_503 = "🏫  Room  -  503"
room_504 = "🏫  Room  -  504"
room_505 = "🏫  Room  -  505"
room_506 = "🏫  Room  -  506"
room_507 = "🏫  Room  -  507"
room_508 = "🏫  Room  -  508"
room_509 = "🏫  Room  -  509"

# TYPE

lecture = "📖  Lecture"
tutorial = "📖  Tutorial"

# NOT SCHEDULED

not_scheduled = "Not scheduled  ❌"





db = sqlite3.connect('DATA BASE.db', check_same_thread=False)
sql = db.cursor()


DateTime = datetime.datetime.now()




user_dict = {}

class User:
    def __init__(self, reg_language):
        self.reg_language = reg_language
        self.reg_type = None
        self.reg_course = None
        self.reg_class = None












@bot.message_handler(commands=['start'])
def Reg_Language(message):


    sql.execute(f'''SELECT ID FROM user_registration WHERE ID = {message.chat.id}''')
    user_id = sql.fetchone()


    if user_id is None:

        user_reg_language = bot.send_message(message.chat.id, '<b> 🇺🇸  Please, choose the language  🇺🇸'
                                                         '\n\n🇷🇺  Пожалуйста, выберите язык  🇷🇺'
                                                         '</b>', parse_mode='html', reply_markup=Buttons.RegistrationLanguageButtons)
        bot.register_next_step_handler(user_reg_language, Reg_Type)

    else:

        bot.send_message(message.chat.id, '<b> You have already registered ! '
                                          '\n\nВы уже зарегестрированы !'
                                          '</b>', parse_mode='html')



def Reg_Type(message):

    chat_id = message.chat.id
    reg_language = message.text
    user = User(reg_language)
    user_dict[chat_id] = user


    if message.text == "🇺🇸  English  🇺🇸":
        user_type = bot.send_message(message.chat.id, '<b> Please, select your group type: </b>', parse_mode='html', reply_markup=Buttons.EnglishRegTypeButtons)
        bot.register_next_step_handler(user_type, Reg_Course)

        sql.execute('''INSERT INTO user_language (ID, Language) VALUES (?, ?)''',
        (str(message.chat.id), 1))
        db.commit()


    if message.text == "🇷🇺  Русский  🇷🇺":
        user_type = bot.send_message(message.chat.id, '<b> Пожалуйста, выберите свой тип группы: </b>', parse_mode='html', reply_markup=Buttons.RussianRegTypeButtons)
        bot.register_next_step_handler(user_type, Reg_Course)

        sql.execute('''INSERT INTO user_language (ID, Language) VALUES (?, ?)''',
        (str(message.chat.id), 2))
        db.commit()


    if message.text == "/start":
        user_reg_language = bot.send_message(message.chat.id, '<b> 🇺🇸  Please, choose the language  🇺🇸'
                                                              '\n\n🇷🇺  Пожалуйста, выберите язык  🇷🇺'
                                                              '</b>', parse_mode='html', reply_markup=Buttons.RegistrationLanguageButtons)
        bot.register_next_step_handler(user_reg_language, Reg_Language)


def Reg_Course(message):

    chat_id = message.chat.id
    reg_type = message.text
    user = user_dict[chat_id]
    user.reg_type = reg_type


    if message.text == "International Group":
        user_course = bot.send_message(message.chat.id, "<b> Please, choose your course of study: </b>", parse_mode='html', reply_markup=Buttons.EnglishRegCourseButtons)
        bot.register_next_step_handler(user_course, Reg_Class)

    if message.text == "Uzbek Group":
        user_course = bot.send_message(message.chat.id, "<b> Please, choose your course of study: </b>", parse_mode='html', reply_markup=Buttons.EnglishRegCourseButtons)
        bot.register_next_step_handler(user_course, Reg_Class)


    if message.text == "Международная Группа":
        user_course = bot.send_message(message.chat.id, "<b> Пожалуйста, выберите свой курс обучения: </b>", parse_mode='html', reply_markup=Buttons.RussianRegCourseButtons)
        bot.register_next_step_handler(user_course, Reg_Class)

    if message.text == "Узбекская Группа":
        user_course = bot.send_message(message.chat.id, "<b> Пожалуйста, выберите свой курс обучения: </b>", parse_mode='html', reply_markup=Buttons.RussianRegCourseButtons)
        bot.register_next_step_handler(user_course, Reg_Class)


    if message.text == "/start":
        user_reg_language = bot.send_message(message.chat.id, '<b> 🇺🇸  Please, choose the language  🇺🇸'
                                                              '\n\n🇷🇺  Пожалуйста, выберите язык  🇷🇺'
                                                              '</b>', parse_mode='html', reply_markup=Buttons.RegistrationLanguageButtons)
        bot.register_next_step_handler(user_reg_language, Reg_Type)

def Reg_Class(message):

    chat_id = message.chat.id
    reg_course = message.text
    user = user_dict[chat_id]
    user.reg_course = reg_course


    if message.text == "Foundation":
        user_class = bot.send_message(message.chat.id, "<b> Choose your group: </b>", parse_mode='html', reply_markup=Buttons.FoundationRegGroupButtons)
        bot.register_next_step_handler(user_class, End_Registration)

    if message.text == "2  -  Year":
        user_class = bot.send_message(message.chat.id, "<b> Choose your group: </b>", parse_mode='html', reply_markup=Buttons.SecondCourseRegGroupButtons)
        bot.register_next_step_handler(user_class, End_Registration)


    if message.text == "Первый Курс":
        user_class = bot.send_message(message.chat.id, "<b> Выберите свою группу: </b>", parse_mode='html', reply_markup=Buttons.FoundationRegGroupButtons)
        bot.register_next_step_handler(user_class, End_Registration)

    if message.text == "Второй Курс":
        user_class = bot.send_message(message.chat.id, "<b> Выберите свою группу: </b>", parse_mode='html', reply_markup=Buttons.SecondCourseRegGroupButtons)
        bot.register_next_step_handler(user_class, End_Registration)

    if message.text == "/start":
        user_reg_language = bot.send_message(message.chat.id, '<b> 🇺🇸  Please, choose the language  🇺🇸'
                                                              '\n\n🇷🇺  Пожалуйста, выберите язык  🇷🇺'
                                                              '</b>', parse_mode='html', reply_markup=Buttons.RegistrationLanguageButtons)
        bot.register_next_step_handler(user_reg_language, Reg_Type)

def End_Registration(message):

    chat_id = message.chat.id
    reg_class = message.text
    user = user_dict[chat_id]
    user.reg_class = reg_class

    sql.execute(f'''SELECT Language FROM user_language WHERE ID = "{message.chat.id}"''')
    user_language = sql.fetchone()[0]



                                                            #  101  -  112  #

    if message.text == "101":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()



    if message.text == "102":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "103":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "104":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "105":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()




    if message.text == "106":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "107":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "108":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "109":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()




    if message.text == "110":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "111":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "112":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()






                                                            #  201  -  212  #


    if message.text == "201":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()



    if message.text == "202":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "203":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "204":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "205":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()




    if message.text == "206":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "207":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "208":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "209":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()




    if message.text == "210":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "211":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()


    if message.text == "212":

        if user_language == 1:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ! </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()

        if user_language == 2:
            bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Добро Пожаловать ! </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)

            sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Language, Type, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_language), str(user.reg_type), str(user.reg_course), str(message.text), DateTime))
            db.commit()



        if message.text == "/start":
            user_reg_language = bot.send_message(message.chat.id, '<b> 🇺🇸  Please, choose the language  🇺🇸'
                                                                  '\n\n🇷🇺  Пожалуйста, выберите язык  🇷🇺'
                                                                  '</b>', parse_mode='html', reply_markup=Buttons.RegistrationLanguageButtons)
            bot.register_next_step_handler(user_reg_language, Reg_Type)






                                                            #  TEXT  #

@bot.message_handler(content_types=['text'])
def Menu(message):


    sql.execute(f'''SELECT Type FROM user_registration WHERE ID = "{message.chat.id}"''')
    user_group_type = sql.fetchone()[0]

    sql.execute(f'''SELECT Course FROM user_registration WHERE ID = "{message.chat.id}"''')
    user_course = sql.fetchone()[0]

    sql.execute(f'''SELECT Class FROM user_registration WHERE ID = "{message.chat.id}"''')
    user_class = sql.fetchone()[0]










                                                            #  TIMETABLE  #


    if message.text == "Timetable  🗓":
        bot.send_message(message.chat.id, "<b> Choose the day: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)




    if message.text == "Monday":

        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Monday timetable - 101 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, f"<b> {monday}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



        if user_class == "103":
            bot.send_message(message.chat.id,f"<b> {monday}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{twelve}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{one}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{one}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{one}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Monday timetable - 112 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



        if user_class == "113":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{four}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "114":
            bot.send_message(message.chat.id, "<b> Monday timetable - 114 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



        if user_class == "201":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{one}"
                                              f"\n{Sathe_M}"
                                              f"\n{bus_communication_ict}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{Pulatov_S}"
                                              f"\n{bus_communication_ict}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "202":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{ten}"
                                              f"\n{Sathe_M}"
                                              f"\n{bus_communication_ict}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Sathe_M}"
                                              f"\n{bus_communication_ict}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Pulatov_S}"
                                              f"\n{bus_communication_ict}"
                                              f"\n{room_201}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "203":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{ten}"
                                              f"\n{Sathe_M}"
                                              f"\n{bus_communication_ict}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Sathe_M}"
                                              f"\n{bus_communication_ict}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "204":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{ten}"
                                              f"\n{Sathe_M}"
                                              f"\n{bus_communication_ict}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Sathe_M}"
                                              f"\n{bus_communication_ict}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "205":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                      f"\n\n{one}"
                                      f"\n{Sathe_M}"
                                      f"\n{bus_communication_ict}"
                                      f"\n{conference_hall}"
                                      f"\n{lecture}"
                                      f"\n\n{four}"
                                      f"\n{Pulatov_S}"
                                      f"\n{bus_communication_ict}"
                                      f"\n{room_201}"
                                      f"\n{lecture}"
                                      f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "206":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{Bekov_S}"
                                              f"\n{project_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Bekov_S}"
                                              f"\n{project_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "207":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{Bekov_S}"
                                              f"\n{project_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Bekov_S}"
                                              f"\n{project_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Bekov_S}"
                                              f"\n{project_management}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)




        if user_class == "208":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{Bekov_S}"
                                              f"\n{project_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Bekov_S}"
                                              f"\n{project_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "209":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{hospitality_leisure}"
                                              f"\n{room_201}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{hospitality_leisure}"
                                              f"\n{room_201}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{hospitality_leisure}"
                                              f"\n{room_201}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)





    if message.text == "Tuesday":

        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Tuesday timetable - 101 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{communication}"
                                              f"\n{communication}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{twelve}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{twelve}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{twelve}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{twelve}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{twelve}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Tuesday timetable - 112 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)


        if user_class == "113":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{one}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{communication}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "114":
            bot.send_message(message.chat.id, "<b> Tuesday timetable - 114 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



        if user_class == "201":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{twelve}"
                                              f"\n{Nurmatov_A}"
                                              f"\n{intro_to_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Nurmatov_A}"
                                              f"\n{intro_to_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{Sathe_M}"
                                              f"\n{bus_communication_ict}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "202":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{Nurmatov_A}"
                                              f"\n{intro_to_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Nurmatov_A}"
                                              f"\n{intro_to_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}" 
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "203":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{Nurmatov_A}"
                                              f"\n{intro_to_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Nurmatov_A}"
                                              f"\n{intro_to_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"         
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "204":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{Nurmatov_A}"
                                              f"\n{intro_to_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Nurmatov_A}"
                                              f"\n{intro_to_management}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "205":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                      f"\n\n{twelve}"
                                      f"\n{Nurmatov_A}"
                                      f"\n{intro_to_management}"
                                      f"\n{room_404}"
                                      f"\n{lecture}"
                                      f"\n\n{one}"
                                      f"\n{Nurmatov_A}"
                                      f"\n{intro_to_management}"
                                      f"\n{room_404}"
                                      f"\n{lecture}"
                                      f"\n\n{three}"
                                      f"\n{Sathe_M}"
                                      f"\n{bus_communication_ict}"
                                      f"\n{room_204}"
                                      f"\n{lecture}"
                                      f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "206":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "207":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "208":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "209":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{ten}"
                                              f"\n{Raxmanova_I}"
                                              f"\n{ict_hospitality}"
                                              f"\n{room_201}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Raxmanova_I}"
                                              f"\n{ict_hospitality}"
                                              f"\n{room_201}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Raxmanova_I}"
                                              f"\n{ict_hospitality}"
                                              f"\n{room_201}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)





    if message.text == "Wednesday":

        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Wednesday timetable - 101 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{twelve}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{twelve}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_304}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{twelve}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n\n{three}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{one}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{four}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{one}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{four}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Wednesday timetable - 112 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)


        if user_class == "113":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{one}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_206}"
                                              f"\n{tutorial}"
                                              f"\n\n{three}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "114":
            bot.send_message(message.chat.id, "<b> Wednesday timetable - 114 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



        if user_class == "201":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "202":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "203":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "204":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "205":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "206":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{nine}"
                                              f"\n{Liayakath_Ali_Khan_S}"
                                              f"\n{java}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Liayakath_Ali_Khan_S}"
                                              f"\n{java}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Liayakath_Ali_Khan_S}"
                                              f"\n{java}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "207":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{nine}"
                                              f"\n{Liayakath_Ali_Khan_S}"
                                              f"\n{java}"
                                              f"\n{room_204}"
                                              f"\n\n{ten}"
                                              f"\n{Liayakath_Ali_Khan_S}"
                                              f"\n{java}"
                                              f"\n{room_204}"
                                              f"\n\n{three}"
                                              f"\n{Liayakath_Ali_Khan_S}"
                                              f"\n{java}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "208":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{nine}"
                                              f"\n{Liayakath_Ali_Khan_S}"
                                              f"\n{java}"
                                              f"\n{room_204}"
                                              f"\n\n{ten}"
                                              f"\n{Liayakath_Ali_Khan_S}"
                                              f"\n{java}"
                                              f"\n{room_204}"
                                              f"\n\n{four}"
                                              f"\n{Liayakath_Ali_Khan_S}"
                                              f"\n{java}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "209":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)





    if message.text == "Thursday":

        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Thursday timetable - 101 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{ten}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{ten}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"\n\n{one}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"\n\n{twelve}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"\n\n{twelve}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{communication}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{twelve}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{communication}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Thursday timetable - 112 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "113":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{twelve}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "114":
            bot.send_message(message.chat.id, "<b> Thursday timetable - 114 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



        if user_class == "201":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{Kumar_A}"
                                              f"\n{intro_to_management}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"\n\n{twelve}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "202":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Kumar_A}"
                                              f"\n{intro_to_management}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "203":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_307}"
                                              f"\n{tutorial}"
                                              f"\n\n{twelve}"
                                              f"\n{Kumar_A}"  
                                              f"\n{intro_to_management}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "204":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Kumar_A}"
                                              f"\n{intro_to_management}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "205":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{twelve}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{Kumar_A}"
                                              f"\n{intro_to_management}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "206":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{Sathe_M}"
                                              f"\n{database}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Sathe_M}"
                                              f"\n{database}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Sathe_M}"
                                              f"\n{database}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "207":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{Sathe_M}"
                                              f"\n{database}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Sathe_M}"
                                              f"\n{database}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "208":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{Sathe_M}"
                                              f"\n{database}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Sathe_M}"
                                              f"\n{database}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "209":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{twelve}"
                                              f"\n{Raxmanova_I}"
                                              f"\n{hotel_resort}"
                                              f"\n{room_206}"
                                              f"\n{tutorial}"
                                              f"\n\n{one}"
                                              f"\n{Raxmanova_I}"
                                              f"\n{hotel_resort}"
                                              f"\n{room_206}"
                                              f"\n{tutorial}"
                                              f"\n\n{three}"
                                              f"\n{Raxmanova_I}"
                                              f"\n{hotel_resort}"
                                              f"\n{room_206}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)





    if message.text == "Friday":

        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Friday timetable - 101 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n\n{three}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{four}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{intro_to_study}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Friday timetable - 112 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "113":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{twelve}"
                                              f"\n{intro_to_study}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "114":
            bot.send_message(message.chat.id, "<b> Friday timetable - 114 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



        if user_class == "201":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "202":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{nine}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "203":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                      f"\n\n{nine}"
                                      f"\n{Ismoilov_A}"
                                      f"\n{marketing_for_managers}"
                                      f"\n{room_204}"
                                      f"\n{lecture}"
                                      f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "204":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{nine}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "205":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "206":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "207":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "208":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "209":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)





    if message.text == "Saturday":

        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Saturday timetable - 101 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{one}"
                                              f"\n{communication}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"\n\n{three}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{three}"
                                              f"\n{communication}"
                                              f"\n{room_307}"
                                              f"\n{tutorial}"
                                              f"\n\n{four}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"\n\n{ten}"
                                              f"\n{communication}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{communication}"
                                              f"\n{room_307}"
                                              f"\n{tutorial}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{three}"
                                              f"\n{communication}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{four}"
                                              f"\n{communication}"
                                              f"\n{room_307}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{communication}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{communication}"
                                              f"\n{room_307}"
                                              f"\n{tutorial}"
                                              f"\n\n{one}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{communication}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"\n\n{twelve}"
                                              f"\n{communication}"
                                              f"\n{room_307}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Saturday timetable - 112 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "113":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{ten}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_207}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "114":
            bot.send_message(message.chat.id, "<b> Saturday timetable - 114 group: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



        if user_class == "201":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "202":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "203":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{twelve}"
                                              f"\n{Pulatov_S}"
                                              f"\n{bus_communication_ict}"
                                              f"\n{room_205}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "204":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{ten}"
                                              f"\n{Pulatov_S}"
                                              f"\n{bus_communication_ict}"
                                              f"\n{room_205}"
                                              f"\n{tutorial}"
                                              f"\n\n{twelve}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "205":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{ten}"
                                              f"\n{Ismoilov_A}"
                                              f"\n{marketing_for_managers}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "206":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{Bekov_S}"
                                              f"\n{project_management}"
                                              f"\n{room_207}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "207":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{ten}"
                                              f"\n{Sathe_M}"
                                              f"\n{database}"
                                              f"\n{room_208}"
                                              f"\n{tutorial}" 
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "208":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{Sathe_M}"
                                              f"\n{database}"
                                              f"\n{room_208}"
                                              f"\n{tutorial}"
                                              f"\n\n{ten}"
                                              f"\n{Bekov_S}"
                                              f"\n{project_management}"
                                              f"\n{room_207}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "209":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{ten}"
                                              f"\n{Raxmanova_I}"
                                              f"\n{ict_hospitality}"
                                              f"\n{room_402}"
                                              f"\n{tutorial}"
                                              f"\n\n{twelve}"
                                              f"\n{Raxmanova_I}"
                                              f"\n{ict_hospitality}"
                                              f"\n{room_402}"
                                              f"\n{tutorial}"
                                              f"\n\n{one}"
                                              f"\n{Raxmanova_I}"
                                              f"\n{ict_hospitality}"
                                              f"\n{room_402}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)









                                                            #  RUSSIAN TIMETABLE  #


    if message.text == "Расписание  🗓":
        bot.send_message(message.chat.id, "<b> Выберите день: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)



    if message.text == "Понедельник":

        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 101  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 102  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 103  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 104  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 105  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 106  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 107  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 108  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 109  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 110  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 111  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 112  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)



        if user_class == "201":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 201  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "202":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 202  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "203":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 203  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "204":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 204  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "205":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 205  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "206":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 206  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "207":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 207  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "208":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 208  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "209":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 209  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "210":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 210  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "211":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 211  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "212":
            bot.send_message(message.chat.id, "<b> Расписание понедельника 212  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)



    if message.text == "Вторник":

        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Расписание вторника 101  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, "<b> Расписание вторника 102  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, "<b> Расписание вторника 103  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, "<b> Расписание вторника 104  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, "<b> Расписание вторника 105  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, "<b> Расписание вторника 106  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, "<b> Расписание вторника 107  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, "<b> Расписание вторника 108  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, "<b> Расписание вторника 109  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, "<b> Расписание вторника 110  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, "<b> Расписание вторника 111  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Расписание вторника 112  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)



        if user_class == "201":
            bot.send_message(message.chat.id, "<b> Расписание вторника 201  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "202":
            bot.send_message(message.chat.id, "<b> Расписание вторника 202  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "203":
            bot.send_message(message.chat.id, "<b> Расписание вторника 203  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "204":
            bot.send_message(message.chat.id, "<b> Расписание вторника 204  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "205":
            bot.send_message(message.chat.id, "<b> Расписание вторника 205  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "206":
            bot.send_message(message.chat.id, "<b> Расписание вторника 206  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "207":
            bot.send_message(message.chat.id, "<b> Расписание вторника 207  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "208":
            bot.send_message(message.chat.id, "<b> Расписание вторника 208  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "209":
            bot.send_message(message.chat.id, "<b> Расписание вторника 209  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "210":
            bot.send_message(message.chat.id, "<b> Расписание вторника 210  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "211":
            bot.send_message(message.chat.id, "<b> Расписание вторника 211  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "212":
            bot.send_message(message.chat.id, "<b> Расписание вторника 212  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)


    if message.text == "Среда":

        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Расписание среды 101  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, "<b> Расписание среды 102  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, "<b> Расписание среды 103  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, "<b> Расписание среды 104  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, "<b> Расписание среды 105  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, "<b> Расписание среды 106  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, "<b> Расписание среды 107  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, "<b> Расписание среды 108  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, "<b> Расписание среды 109  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, "<b> Расписание среды 110  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, "<b> Расписание среды 111  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Расписание среды 112  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)



        if user_class == "201":
            bot.send_message(message.chat.id, "<b> Расписание среды 201  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "202":
            bot.send_message(message.chat.id, "<b> Расписание среды 202  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "203":
            bot.send_message(message.chat.id, "<b> Расписание среды 203  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "204":
            bot.send_message(message.chat.id, "<b> Расписание среды 204  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "205":
            bot.send_message(message.chat.id, "<b> Расписание среды 205  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "206":
            bot.send_message(message.chat.id, "<b> Расписание среды 206  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "207":
            bot.send_message(message.chat.id, "<b> Расписание среды 207  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "208":
            bot.send_message(message.chat.id, "<b> Расписание среды 208  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "209":
            bot.send_message(message.chat.id, "<b> Расписание среды 209  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "210":
            bot.send_message(message.chat.id, "<b> Расписание среды 210  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "211":
            bot.send_message(message.chat.id, "<b> Расписание среды 211  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "212":
            bot.send_message(message.chat.id, "<b> Расписание среды 212  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)





    if message.text == "Четверг":

        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Расписание четверга 101  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, "<b> Расписание четверга 102  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, "<b> Расписание четверга 103  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, "<b> Расписание четверга 104  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, "<b> Расписание четверга 105  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, "<b> Расписание четверга 106  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, "<b> Расписание четверга 107  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, "<b> Расписание четверга 108  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, "<b> Расписание четверга 109  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, "<b> Расписание четверга 110  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, "<b> Расписание четверга 111  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Расписание четверга 112  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)



        if user_class == "201":
            bot.send_message(message.chat.id, "<b> Расписание четверга 201  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "202":
            bot.send_message(message.chat.id, "<b> Расписание четверга 202  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "203":
            bot.send_message(message.chat.id, "<b> Расписание четверга 203  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "204":
            bot.send_message(message.chat.id, "<b> Расписание четверга 204  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "205":
            bot.send_message(message.chat.id, "<b> Расписание четверга 205  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "206":
            bot.send_message(message.chat.id, "<b> Расписание четверга 206  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "207":
            bot.send_message(message.chat.id, "<b> Расписание четверга 207  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "208":
            bot.send_message(message.chat.id, "<b> Расписание четверга 208  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "209":
            bot.send_message(message.chat.id, "<b> Расписание четверга 209  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "210":
            bot.send_message(message.chat.id, "<b> Расписание четверга 210  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "211":
            bot.send_message(message.chat.id, "<b> Расписание четверга 211  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "212":
            bot.send_message(message.chat.id, "<b> Расписание четверга 212  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)




    if message.text == "Пятница":

        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 101  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 102  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 103  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 104  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 105  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 106  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 107  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 108  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 109  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 110  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 111  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 112  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)



        if user_class == "201":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 201  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "202":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 202  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "203":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 203  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "204":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 204  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "205":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 205  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "206":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 206  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "207":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 207  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "208":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 208  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "209":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 209  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "210":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 210  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "211":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 211  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "212":
            bot.send_message(message.chat.id, "<b> Расписание пятницы 212  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)




    if message.text == "Суббота":

        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Расписание субботы 101  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, "<b> Расписание субботы 102  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, "<b> Расписание субботы 103  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, "<b> Расписание субботы 104  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, "<b> Расписание субботы 105  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, "<b> Расписание субботы 106  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, "<b> Расписание субботы 107  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, "<b> Расписание субботы 108  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, "<b> Расписание субботы 109  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, "<b> Расписание субботы 110  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, "<b> Расписание субботы 111  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Расписание субботы 112  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)



        if user_class == "201":
            bot.send_message(message.chat.id, "<b> Расписание субботы 201  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "202":
            bot.send_message(message.chat.id, "<b> Расписание субботы 202  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "203":
            bot.send_message(message.chat.id, "<b> Расписание субботы 203  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "204":
            bot.send_message(message.chat.id, "<b> Расписание субботы 204  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "205":
            bot.send_message(message.chat.id, "<b> Расписание субботы 205  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "206":
            bot.send_message(message.chat.id, "<b> Расписание субботы 206  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "207":
            bot.send_message(message.chat.id, "<b> Расписание субботы 207  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "208":
            bot.send_message(message.chat.id, "<b> Расписание субботы 208  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "209":
            bot.send_message(message.chat.id, "<b> Расписание субботы 209  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "210":
            bot.send_message(message.chat.id, "<b> Расписание субботы 210  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "211":
            bot.send_message(message.chat.id, "<b> Расписание субботы 211  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)

        if user_class == "212":
            bot.send_message(message.chat.id, "<b> Расписание субботы 212  -  группы: </b>", parse_mode='html', reply_markup=Russian_Buttons.WeekDaysButtons)










    if message.text == "Deadlines ❗":
        bot.send_message(message.chat.id, "<b> Choose the category: </b>", parse_mode='html', reply_markup=English_Buttons.DeadlinesButton)


    if message.text == "Dates  🗓":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html')

    if message.text == "Assignment Materials  📑":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html')





    if message.text == "Дэдлайны ❗":
        bot.send_message(message.chat.id, "<b> Выберите категорию: </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)


    if message.text == "Даты  🗓":
        bot.send_message(message.chat.id, "<b> Скоро . . . </b>", parse_mode='html')

    if message.text == "Материалы для задания  📑":
        bot.send_message(message.chat.id, "<b> Скоро . . . </b>", parse_mode='html')





    if message.text == "Events  🎉":
        with open("PHOTOS/Night Vision Party.jpg", "rb") as PartyPhoto:
            bot.send_photo(message.chat.id, PartyPhoto,"<b> Dear TMCI Students!"
                                                         "\nAre you ready for the Freshman Party?!"
                                                         "\n\n💥  TMCI in Tashkent presents a long expected Freshman Party!"
                                                         "\n\nTheme of the Party is “The Night Vision Party"      
                                                         "\n\nOur invited guest is DJ King Macarella"
                                                         "\n\nWe offer:"
                                                         "\n📸  Photozone"
                                                         "\n⚡  Light effects"
                                                         "\n🌯  Food"
                                                         "\n🥤  Drinks"
                                                         "\n\n❗️Dress code : White cloth and Sneakers"
                                                         "\n\n📆  Date: 12.11.2022"
                                                         "\n🕕  Time: 18:00-21:00"
                                                         "\n🏫  Venue: TMCi Atrium (New Campus)"
                                                         "\n💳  Price of the ticket: 200.000 sum"
                                                         "\n\nPlease approach room 210 for ticket purchase."
                                                         "\n\nDeadline to buy tickets is November 10th!"
                                                         "\n\nTickets are limited!"
                                                         "</b>", parse_mode='html')

    if message.text == "События  🎉":
        with open("PHOTOS/Night Vision Party.jpg", "rb") as PartyPhoto:
            bot.send_photo(message.chat.id, PartyPhoto, "<b> Уважаемые студенты TMCI!"
                                                        "\nВы готовы к вечеринке первокурсников?!"
                                                        "\n\n💥  TMCI представляет долгожданную вечеринку для первокурсников!"
                                                        "\n\nТема вечеринки - “Вечеринка ночного видения“"
                                                        "\n\nНаш приглашенный гость - DJ King Macarella"
                                                        "\n\nМы предлагаем:"
                                                        "\n📸  Фотозона"
                                                        "\n⚡  Световые эффекты"
                                                        "\n🌯  Еда"
                                                        "\n🥤  Напитки"
                                                        "\n\n❗️Дресс-код: Белая ткань и кроссовки"
                                                        "\n\n📆  Дата: 12.11.2022"
                                                        "\n🕕  Время: 18:00-21:00"
                                                        "\n🏫  Место проведения: TMCi Atrium (Новый кампус)"
                                                        "\n💳  Стоимость билета: 200.000 сум"
                                                        "\n\nПожалуйста, подойдите в комнату 210 для покупки билета."
                                                        "\n\nКрайний срок покупки билетов - 10 ноября!"
                                                        "\n\nКоличество билетов ограничено!"
                                                        "</b>", parse_mode='html')





    if message.text == "Clubs  🎲":
        bot.send_message(message.chat.id, "<b> Choose the club: </b>", parse_mode='html', reply_markup=English_Buttons.ClubsButtons)

    if message.text == "Speaking club  ⏳":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.ClubsButtons)



    if message.text == "Клубы  🎲":
        bot.send_message(message.chat.id, "<b> Выберите клуб: </b>", parse_mode='html', reply_markup=Russian_Buttons.ClubsButtons)

    if message.text == "Speaking клуб  ⏳":
        bot.send_message(message.chat.id, "<b> Скоро . . . </b>", parse_mode='html', reply_markup=English_Buttons.ClubsButtons)





    if message.text == "News  📬":
        bot.send_message(message.chat.id, "<b>"
                                          "Important ❗"
                                          "\nPhotoshoot for your Student ID and Face ID "
                                          "</b>"
                                          "\n\nThose who have not been pictured for Student ID cards and Face ID system please visit reception ASAP."
                                          "\nHigher Diploma students who lost Student Id cards must also visit reception desk in order to apply for restoring Student ID card."
                                          "<b><i>"
                                          "\n\nBest Regards,"
                                          "\nStudent Service Unit."
                                          "</i></b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)



    if message.text == "Новости  📬":
        bot.send_message(message.chat.id, "<b>"
                                          "Важно ❗"
                                          "\nФотосессия для вашего студенческой карты и Face ID"
                                          "</b>"
                                          "\n\nТе, кто не был сфотографирован для студенческих билетов и системы идентификации лица, пожалуйста, обратитесь на стойку регистрации как можно скорее."
                                          "\nСтуденты с высшим дипломом, потерявшие студенческие билеты, также должны посетить приемную, чтобы подать заявление на восстановление студенческого билета.."
                                          "<b><i>"
                                          "\n\nС уважением,"
                                          "\nОтдел обслуживания студентов."
                                          "</i></b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)





    if message.text == "Contact Us  🆘":

        SupportButton = types.InlineKeyboardMarkup(row_width=2)
        FounderButton1 = types.InlineKeyboardButton(text="Shahrizod", url="https://t.me/ShaHriXMusic")
        FounderButton2 = types.InlineKeyboardButton(text="Ulugbekhon", url="https://t.me/theulugbekhon")
        SupportButton.add(FounderButton1, FounderButton2)

        with open("PHOTOS/Contact Us.jpg", "rb") as ContactUsPhoto:
            bot.send_photo(message.chat.id, ContactUsPhoto, "<b>"
                                                            "<u> Developers: </u>"
                                                            "\n\n -  <a href='https://t.me/ShaHriXMusic'>Shahrizod Ilxomov</a>"
                                                            "\n -  <a href='https://t.me/theulugbekhon'>Shofayziyev Ulugbek</a>"
                                                            "\n\n<u>Chief Advisor: </u>"
                                                            "\n\n -  <a href='https://t.me/A6r0rKM'>Abror Karimov</a>"
                                                            "</b>", parse_mode='html', reply_markup=SupportButton)



    if message.text == "Поддержка  🆘":

        SupportButton = types.InlineKeyboardMarkup(row_width=2)
        FounderButton1 = types.InlineKeyboardButton(text="Shahrizod", url="https://t.me/ShaHriXMusic")
        FounderButton2 = types.InlineKeyboardButton(text="Ulugbekhon", url="https://t.me/theulugbekhon")
        SupportButton.add(FounderButton1, FounderButton2)

        with open("PHOTOS/Contact Us.jpg", "rb") as ContactUsPhoto:
            bot.send_photo(message.chat.id, ContactUsPhoto, "<b>"
                                                            "<u> Разработчики: </u>"
                                                            "\n\n -  <a href='https://t.me/ShaHriXMusic'>Shahrizod Ilxomov</a>"
                                                            "\n -  <a href='https://t.me/theulugbekhon'>Shofayziyev Ulugbek</a>"
                                                            "\n\n<u>Главный советник: </u>"
                                                            "\n\n -  <a href='https://t.me/A6r0rKM'>Abror Karimov</a>"
                                                            "</b>", parse_mode='html', reply_markup=SupportButton)





    if message.text == "Language  🌐":
        bot.send_message(message.chat.id, "<b> Choose the language: </b>", parse_mode='html', reply_markup=Buttons.LanguageButtons)

    if message.text == "Язык  🌐":
        bot.send_message(message.chat.id, "<b> Выберите язык: </b>", parse_mode='html', reply_markup=Buttons.LanguageButtons)





    if message.text == "🇺🇸  English  🇺🇸":
        bot.send_message(message.chat.id, "<b> Main menu: </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

    if message.text == "🇷🇺  Русский  🇷🇺":
        bot.send_message(message.chat.id, "<b> Главное меню: </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)





    if message.text == "Profile  👤":
        bot.send_message(message.chat.id, "<b>"
                                          f"First Name:   ❌"
                                          f"\nLast Name:   ❌"
                                          f"\n\nType:   {user_group_type}"
                                          f"\nCourse:   {user_course}"
                                          f"\nGroup:   {user_class}"
                                          f"\n\nStudent ID:   ❌"
                                          f"\nPhone Number:   ❌"
                                          f"\nEmail:   ❌"
                                          "</b>", parse_mode='html', reply_markup=English_Buttons.VerificationButtons)

    if message.text == "Профиль  👤":
        bot.send_message(message.chat.id, "<b>"
                                          f"Имя:   ❌"
                                          f"\nФамилия:   ❌"
                                          f"\n\nТип:   {user_group_type}"
                                          f"\nКурс:   {user_course}"
                                          f"\nГруппа:   {user_class}"
                                          f"\n\nСтудент ID:   ❌"
                                          f"\nНомер телефона:   ❌"
                                          f"\nПочта:   ❌"
                                          "</b>", parse_mode='html', reply_markup=Russian_Buttons.VerificationButtons)


    if message.text == "Verification  ✅":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html')

    if message.text == "Верификация  ✅":
        bot.send_message(message.chat.id, "<b> Скоро . . . </b>", parse_mode='html')





    if message.text == "Main Menu  🏠":
        bot.send_message(message.chat.id, "<b> Main menu: </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

    if message.text == "Главное Меню  🏠":
        bot.send_message(message.chat.id, "<b> Главное меню: </b>", parse_mode='html', reply_markup=Russian_Buttons.MenuButtons)





    if message.text == "Grape":
        bot.send_message(message.chat.id, "<b> Choose a button: </b>", parse_mode='html', reply_markup=English_Buttons.AdminButtons)


    if message.text == "CHANGE THE GROUP":
        msg = bot.send_message(message.chat.id, "<b> Choose a new group: </b>", parse_mode='html', reply_markup=Buttons.FoundationRegGroupButtons)
        bot.register_next_step_handler(msg, new_group)

def new_group(message):

    sql.execute(f'''UPDATE user_registration SET Class = {message.text}  WHERE ID = "{message.chat.id}"''')
    db.commit()

    bot.send_message(message.chat.id, "<b> Your group is updated ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)











while True:

    try:

        bot.polling(non_stop=True)

    except Exception as e:
        time.sleep(15)

# if __name__ == '__main__':
#     bot.polling(non_stop=True)