import  telebot
import sqlite3
import datetime
import time

import CONFIG


from ENGLISH_BUTTONS import English_Buttons
from INLINE_BUTTONS import Inline_Buttons

bot = telebot.TeleBot(CONFIG.TOKEN)





# DAYS

monday = "🗓  Monday"
tuesday = "🗓  Tuesday"
wednesday = "🗓  Wednesday"
thursday = "🗓  Thursday"
friday = "🗓  Friday"
saturday = "🗓  Saturday"

#  TEACHERS


#  2 YEAR  #

Sathe_M = "👨‍🏫  Sathe M"
Pulatov_S = "👨‍🏫  Pulatov S"
Nurmatov_A = "👨‍🏫  Nurmatov A"
Kumar_A = "👨‍🏫  Kumar A"
Ismoilov_A = "👨‍🏫  Ismoilov A"
Bekov_S = "👨‍🏫  Bekov S"
Liayakath_Ali_Khan_S = "👨‍🏫  Liayakath Ali Khan S"
Raxmanova_I = "👨‍🏫  Raxmanova I"


#  FOUNDATION

Bekmuradova_M = "👨‍🏫  Bekmuradova M"
Gavalyan_N = "👨‍🏫  Gavalyan N"
Yusupov_T = "👨‍🏫  Yusupov T"
Bektasheva_D = "👨‍🏫  Bektasheva D"
Nizamov_A = "👨‍🏫  Nizamov A"
Golestan_Z = "👨‍🏫  Golestan Z"
Sulaymonov_A = "👨‍🏫  Sulaymonov_A"




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

nine = "🕗  09:00 AM  -  10:20 AM"
ten = "🕗  10:30 AM  -  11:50 AM"
twelve = "🕗  12:00 PM  -  13:20 PM"
one = "🕗  13:30 PM  -  14:50 PM"
three = "🕗  15:00 PM  -  16:20 PM"
four = "🕗  16:30 PM  -  17:50 PM"

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
    def __init__(self, reg_course):
        self.reg_course = reg_course
        self.reg_class = None








@bot.message_handler(commands=['start'])
def Reg_Start(message):


    sql.execute(f'''SELECT ID FROM user_registration WHERE ID = {message.chat.id}''')
    user_id = sql.fetchone()


    if user_id is None:

        user_course = bot.send_message(message.chat.id, "<b> Please, select your year of study: </b>", parse_mode='html', reply_markup=English_Buttons.EnglishRegCourseButtons)
        bot.register_next_step_handler(user_course, Reg_Class)

    else:

        bot.send_message(message.chat.id, '<b> You have already registered ❗ </b>', parse_mode='html')



def Reg_Class(message):

    chat_id = message.chat.id
    reg_course = message.text
    user = User(reg_course)
    user_dict[chat_id] = user


    if message.text == "Foundation":
        user_class = bot.send_message(message.chat.id, "<b> Please, select your group: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationRegGroupButtons)
        bot.register_next_step_handler(user_class, End_Registration)

    elif message.text == "Year 2":
        user_class = bot.send_message(message.chat.id, "<b> Please, select your group: </b>", parse_mode='html', reply_markup=English_Buttons.SecondCourseRegGroupButtons)
        bot.register_next_step_handler(user_class, End_Registration)



    elif message.text == "/start":
        reg_type = bot.send_message(message.chat.id, f"<b> Please, select your year of study: </b>", parse_mode='html', reply_markup=English_Buttons.EnglishRegCourseButtons)
        bot.register_next_step_handler(reg_type, Reg_Class)


    else:

        bot.send_message(message.chat.id, '<b> Unknown year of study ❗ </b>', parse_mode='html', reply_markup=English_Buttons.EnglishRegCourseButtons)

        user_course= bot.send_message(message.chat.id, '<b> Please, select your year of study: </b>', parse_mode='html', reply_markup=English_Buttons.EnglishRegCourseButtons)
        bot.register_next_step_handler(user_course, Reg_Class)


def End_Registration(message):

    chat_id = message.chat.id
    reg_class = message.text
    user = user_dict[chat_id]
    user.reg_class = reg_class



                                                            #  101  -  112  #

    if message.text == "101":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "102":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "103":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "104":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "105":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "106":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "107":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "108":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "109":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "110":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "111":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "112":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "113":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "114":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "201":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "202":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "203":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "204":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "205":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "206":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "207":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "208":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()
        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "209":
        bot.send_message(message.chat.id, f"<b> {message.from_user.full_name}, Welcome ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)

        sql.execute('''INSERT INTO user_registration (ID, Username, First_Name, Last_Name, Course, Class, Date_Time) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (str(message.chat.id), str(message.from_user.username), str(message.from_user.first_name), str(message.from_user.last_name), str(user.reg_course), str(message.text), DateTime))
        db.commit()

        bot.send_message('@fghjjuytye',   f"User ID:  " + str(message.chat.id) +
                                          f"\nUsername:  @" + str(message.from_user.username) +
                                          f"\nFirst Name:  " + str(message.from_user.first_name) +
                                          f"\nLast Name:  " + str(message.from_user.last_name) +
                                          f"\nCourse:  " + str(user.reg_course) +
                                          f"\nGroup:  " + str(message.text))


    elif message.text == "/start":
        reg_type = bot.send_message(message.chat.id, f"<b> Please, select your year of study: </b>", parse_mode='html', reply_markup=English_Buttons.EnglishRegCourseButtons)
        bot.register_next_step_handler(reg_type, Reg_Class)

    else:

        bot.send_message(message.chat.id, '<b> Unknown group ❗ </b>', parse_mode='html', reply_markup=English_Buttons.EnglishRegCourseButtons)

        user_course = bot.send_message(message.chat.id, '<b> Please, select your year of study: </b>', parse_mode='html', reply_markup=English_Buttons.EnglishRegCourseButtons)
        bot.register_next_step_handler(user_course, Reg_Class)


                                                            #  TEXT  #

@bot.message_handler(content_types=['text'])
def Menu(message):


    sql.execute(f'''SELECT Course FROM user_registration WHERE ID = "{message.chat.id}"''')
    user_course = sql.fetchone()[0]

    sql.execute(f'''SELECT Class FROM user_registration WHERE ID = "{message.chat.id}"''')
    user_class = sql.fetchone()[0]









                                                            #  TIMETABLE  #



    if message.text == "Deadlines ❗":
        bot.send_message(message.chat.id, "<b> Choose the category: </b>", parse_mode='html', reply_markup=English_Buttons.DeadlinesButton)


    if message.text == "Dates  🗓":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html')

    if message.text == "Assignment Materials  📑":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html')





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





    if message.text == "Clubs  🎲":
        with open("PHOTOS/English Hub.jpg", "rb") as SpeakingClubPhoto:
            bot.send_photo(message.chat.id, SpeakingClubPhoto, "<b> Choose the club: </b>", parse_mode='html', reply_markup=Inline_Buttons.ClubsButton)


    if message.text == "Speaking club":

        with open("PHOTOS/English Hub.jpg", "rb") as SpeakingClubPhoto:

            bot.send_photo(message.chat.id, SpeakingClubPhoto, "<b> </b>", parse_mode='html', reply_markup=Inline_Buttons.SpeakingClubButton)


    if message.text == "Club 2":

        with open("PHOTOS/Empty.png", "rb") as EmptyPhoto:
            bot.send_photo(message.chat.id, EmptyPhoto, "<b> </b>", parse_mode='html', reply_markup=Inline_Buttons.CreateTheClubButton)

    if message.text == "Club 3":

        with open("PHOTOS/Empty.png", "rb") as EmptyPhoto:
            bot.send_photo(message.chat.id, EmptyPhoto, "<b> </b>", parse_mode='html', reply_markup=Inline_Buttons.CreateTheClubButton)

    if message.text == "Club 4":

        with open("PHOTOS/Empty.png", "rb") as EmptyPhoto:
            bot.send_photo(message.chat.id, EmptyPhoto, "<b> </b>", parse_mode='html', reply_markup=Inline_Buttons.CreateTheClubButton)

    if message.text == "Club 5":

        with open("PHOTOS/Empty.png", "rb") as EmptyPhoto:
            bot.send_photo(message.chat.id, EmptyPhoto, "<b> </b>", parse_mode='html', reply_markup=Inline_Buttons.CreateTheClubButton)

    if message.text == "Club 6":

        with open("PHOTOS/Empty.png", "rb") as EmptyPhoto:
            bot.send_photo(message.chat.id, EmptyPhoto, "<b> </b>", parse_mode='html', reply_markup=Inline_Buttons.CreateTheClubButton)





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



    if message.text == "Files  📁":


        if user_class == "101":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "102":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "103":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "104":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "105":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "106":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "107":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "108":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "109":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "110":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "111":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "112":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "113":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "114":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

        if user_class == "201":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.AccountingFilesButton)

        if user_class == "202":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.BusinessFilesButton)

        if user_class == "203":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.BusinessFilesButton)

        if user_class == "204":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.BusinessFilesButton)

        if user_class == "205":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.LogisticsFilesButton)

        if user_class == "206":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.ITFilesButton)

        if user_class == "207":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.ITFilesButton)

        if user_class == "208":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.ITFilesButton)

        if user_class == "209":
            bot.send_message(message.chat.id, "<b> Select a subject: </b>", parse_mode='html', reply_markup=English_Buttons.TourismFilesButton)


    #  FOUNDATION  #

    if message.text == "Communication  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

    if message.text == "Introduction to Information Technology  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

    if message.text == "Introduction to Study Skills  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

    if message.text == "Introduction To Social And Digital Media  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)

    if message.text == "Psychology Applied To Work  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.FoundationSubjectsButton)



    #  IT  #

    if message.text == "Project Management  📁":
        bot.send_message(message.chat.id, "<b> Select a session: </b>", parse_mode='html', reply_markup=Inline_Buttons.ProjectManagement_1)

    if message.text == "Application Programming with Java  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.ITFilesButton)

    if message.text == "Database Systems  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.ITFilesButton)



    #  ACCOUNTING, BUSINESS, LOGISTICS  #

    if message.text == "Business Communication and ICT  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.BusinessFilesButton)

    if message.text == "Introduction to Management  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.BusinessFilesButton)

    if message.text == "Marketing for Managers  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.BusinessFilesButton)



    #  TOURISM  #

    if message.text == "ICT in the Hospitality and Leisure Industry  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.TourismFilesButton)

    if message.text == "International Hotel and Resort Management  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.TourismFilesButton)

    if message.text == "Marketing for Hospitality and Leisure  📁":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html', reply_markup=English_Buttons.TourismFilesButton)





    if message.text == "Contact Us  🆘":

        with open("PHOTOS/Contact Us.jpg", "rb") as ContactUsPhoto:
            bot.send_photo(message.chat.id, ContactUsPhoto, "<b>"
                                                            "<u> Developers: </u>"
                                                            "\n\n🧑‍💻  <a href='https://t.me/ShaHriXMusic'>Shahrizod Ilxomov</a>"
                                                            "\n🧑‍💻  <a href='https://t.me/theulugbekhon'>Ulugbek Shofayziev</a>"
                                                            "\n\n<u>Chief Advisor: </u>"
                                                            "\n\n🤵  <a href='https://t.me/A6r0rKM'>Abror Karimov</a>"
                                                            "</b>", parse_mode='html', reply_markup=Inline_Buttons.SupportButton)





    if message.text == "Profile  👤":
        with open("PHOTOS/Profile.png", "rb") as ProfilePhoto:
            bot.send_photo(message.chat.id, ProfilePhoto, "<b>"
                                                          f'❌  First Name:'
                                                          f'\n❌  Last Name:'
                                                          f'\n\n✅  Year:   "{user_course}"'
                                                          f'\n✅  Group:   "{user_class}"'
                                                          f'\n\n❌  Student ID:'
                                                          f'\n❌  Phone Number:'
                                                          f'\n❌  Email:'
                                                          "</b>", parse_mode='html', reply_markup=English_Buttons.VerificationButtons)

    if message.text == "Verification  ✅":
        bot.send_message(message.chat.id, "<b> Soon . . . </b>", parse_mode='html')





    if message.text == "Main Menu  🏠":
        bot.send_message(message.chat.id, "<b> Main menu: </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)





    if message.text == "Grape":
        bot.send_message(message.chat.id, "<b> Choose a button: </b>", parse_mode='html', reply_markup=English_Buttons.AdminButtons)


    if message.text == "CHANGE THE GROUP":
        bot.send_message(message.chat.id, "<b> Choose the course: </b>", parse_mode='html', reply_markup=English_Buttons.EnglishRegCourseButtons)


    if message.text == "Foundation":
        msg = bot.send_message(message.chat.id, "<b> Choose the group: </b>", parse_mode='html', reply_markup=English_Buttons.FoundationRegGroupButtons)
        bot.register_next_step_handler(msg, new_group)

    if message.text == "Year 2":
        msg = bot.send_message(message.chat.id, "<b> Choose the group: </b>", parse_mode='html', reply_markup=English_Buttons.SecondCourseRegGroupButtons)
        bot.register_next_step_handler(msg, new_group)


def new_group(message):

    sql.execute(f'''SELECT Class FROM user_registration WHERE ID = "{message.chat.id}"''')
    user_class = sql.fetchone()[0]

    sql.execute(f'''UPDATE user_registration SET Class = {message.text}  WHERE ID = "{message.chat.id}"''')
    db.commit()


    bot.send_message(message.chat.id, "<b> Your group is updated ❗ </b>", parse_mode='html', reply_markup=English_Buttons.MenuButtons)





                                                                        #  TIMETABLE  #


    if message.text == "Timetable  🗓":
        bot.send_message(message.chat.id, "<b> Choose the day: </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)





    if message.text == "Monday":

        if user_class == "101":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, f"<b> {monday}"
                                              f"\n\n{ten}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id,f"<b>{monday}"
                                              f"\n\n{ten}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{twelve}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{one}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{one}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{one}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{nine}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



        if user_class == "113":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{three}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "114":
            bot.send_message(message.chat.id, f"<b>{monday}"
                                              f"\n\n{three}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



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
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{nine}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Golestan_Z}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{twelve}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{twelve}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{twelve}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{twelve}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{twelve}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{twelve}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)


        if user_class == "113":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{one}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "114":
            bot.send_message(message.chat.id, f"<b>{tuesday}"
                                              f"\n\n{one}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{four}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



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
                                              f"\n{room_404}"
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
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{ten}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{ten}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{ten}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{nine}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{nine}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Golestan_Z}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{nine}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{twelve}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{twelve}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{twelve}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{one}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{four}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{one}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{four}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{one}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{four}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)


        if user_class == "113":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{one}"
                                              f"\n{Sulaymonov_A}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_206}"
                                              f"\n{tutorial}"
                                              f"\n\n{three}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{four}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "114":
            bot.send_message(message.chat.id, f"<b>{wednesday}"
                                              f"\n\n{three}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{four}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



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
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{ten}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Golestan_Z}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{ten}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{Sulaymonov_A}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"\n\n{ten}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{ten}"
                                              f"\n{Golestan_Z}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"\n\n{twelve}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Sulaymonov_A}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{nine}"
                                              f"\n{Golestan_Z}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"\n\n{twelve}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{twelve}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{ten}"
                                              f"\n{Sulaymonov_A}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{twelve}"
                                              f"\n{Sulaymonov_A}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "113":
            bot.send_message(message.chat.id, f"<b>{thursday}"
                                              f"\n\n{four}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "114":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



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
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{nine}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{one}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{nine}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{three}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_201}"
                                              f"\n{tutorial}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{nine}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_404}"
                                              f"\n{lecture}"
                                              f"\n\n{four}"
                                              f"\n{Bekmuradova_M}"
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
                                              f"\n{Sulaymonov_A}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{one}"
                                              f"\n{Sulaymonov_A}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{ten}"
                                              f"\n{Sulaymonov_A}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, f"<b>{friday}"
                                              f"\n\n{twelve}"
                                              f"\n{Golestan_Z}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "113":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "114":
            bot.send_message(message.chat.id, f"<b> {not_scheduled} </b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



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
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{Bektasheva_D}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"\n\n{twelve}"
                                              f"\n{Nizamov_A}"
                                              f"\n{communication}"
                                              f"\n{room_307}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "102":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{one}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"\n\n{three}"
                                              f"\n{Bektasheva_D}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              "</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "103":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{three}"
                                              f"\n{Nizamov_A}"
                                              f"\n{communication}"
                                              f"\n{room_307}"
                                              f"\n{tutorial}"
                                              f"\n\n{four}"
                                              f"\n{Bektasheva_D}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "104":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{Bektasheva_D}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"\n\n{ten}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "105":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{Nizamov_A}"
                                              f"\n{communication}"
                                              f"\n{room_307}"
                                              f"\n{tutorial}"
                                              f"\n\n{ten}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "106":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{three}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "107":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{ten}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{four}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_307}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "108":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "109":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Bektasheva_D}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "110":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Nizamov_A}"
                                              f"\n{communication}"
                                              f"\n{room_307}"
                                              f"\n{tutorial}"
                                              f"\n\n{one}"
                                              f"\n{Bektasheva_D}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "111":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{ten}"
                                              f"\n{Bektasheva_D}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_209}"
                                              f"\n{tutorial}"
                                              f"\n\n{one}"
                                              f"\n{Nizamov_A}"
                                              f"\n{communication}"
                                              f"\n{room_307}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "112":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{nine}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_204}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Gavalyan_N}"
                                              f"\n{communication}"
                                              f"\n{room_308}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "113":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{ten}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_207}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)

        if user_class == "114":
            bot.send_message(message.chat.id, f"<b>{saturday}"
                                              f"\n\n{ten}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{conference_hall}"
                                              f"\n{lecture}"
                                              f"\n\n{twelve}"
                                              f"\n{Bekmuradova_M}"
                                              f"\n{intro_to_study}"
                                              f"\n{room_202}"
                                              f"\n{tutorial}"
                                              f"\n\n{one}"
                                              f"\n{Yusupov_T}"
                                              f"\n{intro_to_it}"
                                              f"\n{room_207}"
                                              f"\n{tutorial}"
                                              f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)



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



@bot.callback_query_handler(func = lambda call: True)
def answer(call):

    if call.data == "club_1":
        with open("PHOTOS/English Hub.jpg", "rb") as SpeakingClubPhoto:
            bot.send_photo(call.message.chat.id, SpeakingClubPhoto, "<b> </b>", parse_mode='html', reply_markup=Inline_Buttons.SpeakingClubButton)

    if call.data == "club_2":
        with open("PHOTOS/Empty.png", "rb") as EmptyPhoto:
            bot.send_photo(call.message.chat.id, EmptyPhoto, "<b> </b>", parse_mode='html', reply_markup=Inline_Buttons.CreateTheClubButton)

    if call.data == "club_3":
        with open("PHOTOS/Empty.png", "rb") as EmptyPhoto:
            bot.send_photo(call.message.chat.id, EmptyPhoto, "<b> </b>", parse_mode='html', reply_markup=Inline_Buttons.CreateTheClubButton)

    if call.data == "club_4":
        with open("PHOTOS/Empty.png", "rb") as EmptyPhoto:
            bot.send_photo(call.message.chat.id, EmptyPhoto, "<b> </b>", parse_mode='html', reply_markup=Inline_Buttons.CreateTheClubButton)

    if call.data == "club_5":
        with open("PHOTOS/Empty.png", "rb") as EmptyPhoto:
            bot.send_photo(call.message.chat.id, EmptyPhoto, "<b> </b>", parse_mode='html', reply_markup=Inline_Buttons.CreateTheClubButton)

    if call.data == "club_6":
        with open("PHOTOS/Empty.png", "rb") as EmptyPhoto:
            bot.send_photo(call.message.chat.id, EmptyPhoto, "<b> </b>", parse_mode='html', reply_markup=Inline_Buttons.CreateTheClubButton)






    if call.data == "P_M_Session_1":
        with open("FILES/Lectures/Year 2/IT/Project Management/Project Scope Management.pptx", "rb") as P_M_File_1:
            bot.send_document(call.message.chat.id, P_M_File_1, caption="<b> Project Scope Management </b>", parse_mode='html')

    if call.data == "P_M_Session_2":
        with open("FILES/Lectures/Year 2/IT/Project Management/Project Management Methodologies.pptx", "rb") as P_M_File_2:
            bot.send_document(call.message.chat.id, P_M_File_2, caption="<b> Project Management Methodologies </b>", parse_mode='html')

    if call.data == "P_M_Session_3":
        with open("FILES/Lectures/Year 2/IT/Project Management/Introduction to Project Management.pptx", "rb") as P_M_File_3:
            bot.send_document(call.message.chat.id, P_M_File_3, caption="<b> Introduction to Project Management </b>", parse_mode='html')



    if call.data == "P_M_Next":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b> Select a session: </b>", parse_mode="html", reply_markup=Inline_Buttons.ProjectManagement_2)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="You selected the next page:")

    if call.data == "P_M_Back":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b> Select a session: </b>", parse_mode="html", reply_markup=Inline_Buttons.ProjectManagement_1)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="You selected the previous page:")



if __name__=='__main__':

    while True:

        try:

            bot.polling(non_stop=True, interval=0)

        except Exception as e:

            print(e)
            time.sleep(5)
            continue