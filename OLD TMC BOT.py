import telebot

bot = telebot.TeleBot('5631144225:AAH7maWRJP4OVmeC5zMU7BEI08Q_9eMt1Bc')

########################################################################################################################

# ADMIN PANEL

@bot.message_handler(commands=['adminmessage1'])
def Main(message):
    if message.chat.id == 284929331:
        for i in open('TMC BOT REAL IDS.txt', 'r').readlines():
            NewCampusPhoto = open('NEW CAMPUS.jpg', 'rb')
            bot.send_photo(i, NewCampusPhoto, '<b>'
            'Новый Кампус будет готов уже в этом году❗'
            '\n\nПодробная Информация - http://shorturl.at/efAMS'
            '</b>', parse_mode = 'html')


@bot.message_handler(commands=['adminpoll1'])
def Poll(message):
    if message.chat.id == 284929331:
        for i in open('REAL IDS.txt', 'r').readlines():
            Answer = bot.send_message(i, "Дайте рейтинг боту 🤗", reply_markup=Stars)
            bot.register_next_step_handler(Answer, AnswerReview)

def AnswerReview(message):

            UserAnswer = message.text
            UserNameText = "Username: @"
            RateUserName = message.from_user.username
            UserID = message.chat.id
            UserIdText = "User ID: "
            AnswerText = "Answer: "

            bot.send_message('@tmcbotratings', UserNameText + str(RateUserName) + '\n' + UserIdText + str(UserID) + '\n\n' + AnswerText + UserAnswer)
            bot.send_message(message.chat.id, 'Спасибо за Ответ 🙏', reply_markup=Menu)

########################################################################################################################





########################################################################################################################

# COMMANDS

@bot.message_handler(commands=['start'])
def Main(message):
    bot.send_message(message.chat.id, '<b> Main Menu 📍 </b>', parse_mode = 'Html', reply_markup = Menu)
    with open('TMC BOT User Names.txt', 'a+') as chatids:
        print(message.from_user.username, file = chatids)
        with open('TMC BOT Users IDs.txt', 'a+') as chatids:
            Comma = ','
            print (str(message.chat.id) + Comma, file=chatids)
            with open('TMC BOT Username & IDs.txt', 'a+') as chatids:
                print(message.chat.id, message.from_user.username, file=chatids)


@bot.message_handler(commands=['help'])
def Main(message):
    bot.send_message(message.chat.id, '<b> /start - Start Bot  \n/help - List of Commands \n\n/menu - Main Menu \n/timetable - Timetable of Lessons \n/deadlines - Dates of DeadLines \n\n/founders - Bot Creators </b>', parse_mode = 'Html')

@bot.message_handler(commands=['timetable'])
def Main(message):
    bot.send_message(message.chat.id, '<b> Regular classes are over! </b>', parse_mode = 'Html', reply_markup = Menu)

@bot.message_handler(commands=['menu'])
def Main(message):
    bot.send_message(message.chat.id, "<b> Main Menu📍 </b>", parse_mode = 'Html', reply_markup = Menu)

@bot.message_handler(commands=['deadlines'])
def Main(message):
    bot.send_message(message.chat.id, '<b> DeadLines❗️ </b>', parse_mode = 'Html', reply_markup = DeadlineButton)

@bot.message_handler(commands=['events'])
def Main(message):
    bot.send_message(message.chat.id, '<b> Empty </b>', parse_mode = 'Html', reply_markup = Menu)


@bot.message_handler(commands=['founders'])
def Main(message):
    bot.send_message(message.chat.id, '<b> @ShaHriXMusic & @theulugbekhon </b>', parse_mode='Html', reply_markup=Menu)


@bot.message_handler(commands=['update'])
def Main(message):
    bot.send_message(message.chat.id, '<b> Main Menu📍 </b>', parse_mode='Html', reply_markup=Menu)




########################################################################################################################

# GROUP COMMANDS

# @bot.message_handler(commands=['101'])
# def Main(message):
#     bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Menu)
#
# @bot.message_handler(commands=['102'])
# def Main(message):
#     bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Menu)
#
# @bot.message_handler(commands=['103'])
# def Main(message):
#     bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Menu)
#
# @bot.message_handler(commands=['104'])
# def Main(message):
#     bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Menu)
#
# @bot.message_handler(commands=['105'])
# def Main(message):
#     bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Menu)
#
# @bot.message_handler(commands=['106'])
# def Main(message):
#     bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Menu)
#
# @bot.message_handler(commands=['107'])
# def Main(message):
#     bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Menu)
#
# @bot.message_handler(commands=['108'])
# def Main(message):
#     bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Menu)
#
# @bot.message_handler(commands=['109'])
# def Main(message):
#     bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Menu)
#
# @bot.message_handler(commands=['110'])
# def Main(message):
#     bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Menu)
#
# @bot.message_handler(commands=['111'])
# def Main(message):
#     bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Menu)





########################################################################################################################

@bot.message_handler(content_types=['text'])
def buttons(message):

# MENU BUTTONS

    if message.text == "Timetable  🗓":
        bot.send_message(message.chat.id, '<b> Regular classes are over! </b>', parse_mode = 'Html', reply_markup = Menu)

    if message.text == "DeadLines❗️":
        bot.send_message(message.chat.id,  '<b> Deadlines❗️ </b>', parse_mode = 'Html', reply_markup = DeadlineButton)

    if message.text == "Events  🎉":
        bot.send_message(message.chat.id, '<b> Culture Day (SOON) </b>', parse_mode = 'Html', reply_markup = Menu)


    if message.text == "Games  🎮":
        bot.send_message(message.chat.id, "Choose The Game 👇", reply_markup=Games)

    if message.text == "Dart  🎯":
        bot.send_dice(message.chat.id, "🎯", reply_markup=Menu)

    if message.text == "Dice  🎲":
        bot.send_dice(message.chat.id, "🎲", reply_markup=Menu)

    if message.text == "Slot Machine  🎰":
        bot.send_dice(message.chat.id, "🎰", reply_markup=Menu)

    if message.text == "Football  ⚽️":
        bot.send_dice(message.chat.id, "⚽️", reply_markup=Menu)

    if message.text == "Basketball  🏀":
        bot.send_dice(message.chat.id, "🏀", reply_markup=Menu)


    if message.text == "News  📢":
        bot.send_message(message.chat.id, "<b> NEWS SOON... </b>", parse_mode = 'html', reply_markup=Menu)


    if message.text == "Contact Us  🆘":
        bot.send_message(message.chat.id, "<b> For All Questions  🔰 \n\n ⚫️  @ShaHriXMusic  ⚫️ \n\n 🟢  @theulugbekhon  🟢 </b>", parse_mode = 'Html', reply_markup=Menu)


    if message.text == "Dates  🗓":
        bot.send_message(message.chat.id, '<b> IT Class Exam (30%) 📚 \n 10.05.2022 🗓\n\n 10:00 morning session 🕗 \n 14:00 afternoon session 🕗 </b>', parse_mode='Html', reply_markup=Menu)
        bot.send_message(message.chat.id, '<b> Psychology Class Exam (50%) 📚 \n 11.05.2022 🗓\n\n 10:00 morning session 🕗 \n 14:00 afternoon session 🕗 </b>', parse_mode='Html', reply_markup=Menu)
        bot.send_message(message.chat.id,'<b> Media Class Exam (50%) 📚  \n 12.05.2022 🗓\n\n 10:00 morning session 🕗 \n 14:00 afternoon session 🕗 </b>',parse_mode='Html', reply_markup=Menu)

    if message.text == "Assignment Materials  📑":
        bot.send_message(message.chat.id, '<b> What kind of material do you need? 🔍 </b>', parse_mode = 'Html', reply_markup = FilesButton)

    if message.text == "Task Descriptions  📝":
        bot.send_message(message.chat.id, '<b> Nothing Found ! </b>', parse_mode = 'Html', reply_markup = Menu)

    if message.text == "Lectures & Tutorials (PPTs)  📁":
        bot.send_message(message.chat.id, '<b> Select The Subject 👇 </b>', parse_mode = 'Html', reply_markup = SubjectsButton)

    if message.text == "Psychology Applied To Work  📚":
        bot.send_message(message.chat.id, '<b> Psychology Applied To Work Files 👇 </b>', parse_mode='Html', reply_markup=Menu)
        File1 = open ('File 1.pptx', 'rb')
        bot.send_document(message.chat.id, File1, caption = '<i> Introduction to Psychology at Workplace </i>', parse_mode='html')
        File2 = open('File 2.pptx', 'rb')
        bot.send_document(message.chat.id, File2, caption = '<i> Intro to I/O Psychology. Part 2 </i>', parse_mode='html')
        File3 = open('File 3.pptx', 'rb')
        bot.send_document(message.chat.id, File3, caption = '<i> Work Attitudes and Values </i>', parse_mode='html')
        File4 = open('File 4.docx', 'rb')
        bot.send_document(message.chat.id, File4, caption = '<i> Psychology Tutorial #1 </i>', parse_mode='html')
        File5 = open('File 5.pptx', 'rb')
        bot.send_document(message.chat.id, File5, caption = '<i> Psychology - 16.02.2022 \n\n Motivation </i>', parse_mode='html')
        File6 = open('File 6.docx', 'rb')
        bot.send_document(message.chat.id, File6, caption = '<i> Psychology Tutorial #2  </i>', parse_mode='html')
        File7 = open('File 7.pptx', 'rb')
        bot.send_document(message.chat.id, File7, caption = '<i> Psychology 21.02.2022 \n\n Motivation. Part 2. </i>', parse_mode='html')
        File8 = open('File 8.pptx', 'rb')
        bot.send_document(message.chat.id, File8, caption = '<i> Psychology - 28.02.2022 \n\n Leadership </i>', parse_mode='html')
        File9 = open('File 9.pptx', 'rb')
        bot.send_document(message.chat.id, File9, caption = '<i> Psychology - 02.03.2022 \n\n Leadership Theories (Part 2) </i>', parse_mode='html')
        File10 = open('File 10.pptx', 'rb')
        bot.send_document(message.chat.id, File10, caption = '<i> Psychology Tutorial - 05.03.2022 </i>', parse_mode='html')
        File11= open('File 11.pptx', 'rb')
        bot.send_document(message.chat.id, File11, caption = '<i> Psychology - 16.03.2022 \n\n Emotional Intelligence </i>', parse_mode='html')
        File12= open('File 12.pptx', 'rb')
        bot.send_document(message.chat.id, File12, caption = '<i> Psychology - 28.03.2022 \n\n Groups </i>', parse_mode='html')
        File13= open('File 13.pptx', 'rb')
        bot.send_document(message.chat.id, File13, caption = '<i> Psychology - 30.03.2022 \n\n Teams </i>', parse_mode='html')
        File14= open('File 14.pptx', 'rb')
        bot.send_document(message.chat.id, File14, caption = '<i> Psychology Tutorial - 02.04.2022 \n\n Lost at Sea </i>', parse_mode='html')
        File15= open('File 15.pptx', 'rb')
        bot.send_document(message.chat.id, File15, caption = '<i> Psychology - 04.04.2022 \n\n Conflict </i>', parse_mode='html')
        File16 = open('File 16.pptx', 'rb')
        bot.send_document(message.chat.id, File16, caption='<i> Psychology - 06.04.2022 \n\n Negotiations </i>', parse_mode='html')
        File17 = open('File 17.pptx', 'rb')
        bot.send_document(message.chat.id, File17,caption='<i> Psychology - 09.04.2022 \n\n Negotiations Tutorial </i>', parse_mode='html')
        File18 = open('File 18.ppt', 'rb')
        bot.send_document(message.chat.id, File18, caption='<i> Psychology - 11.04.2022 \n\n Occupational Health </i>',parse_mode='html')
        File19 = open('File 19.pptx', 'rb')
        bot.send_document(message.chat.id, File19,caption='<i> Psychology - 13.04.2022 \n\n Diversity and Culture </i>', parse_mode='html')
        File20 = open('File 20.pptx', 'rb')
        bot.send_document(message.chat.id, File20,caption="<i> Psychology - 16.04.2022 \n\n Hofstede's Model </i>", parse_mode='html')
        File21 = open('File 21.pptx', 'rb')
        bot.send_document(message.chat.id, File21,caption='<i> Psychology - 18.04.2022 \n\n Organizational Development </i>', parse_mode='html')
        File22 = open('File 22.pptx', 'rb')
        bot.send_document(message.chat.id, File22, caption='<i> Psychology - 20.04.2022 \n\n Organizational structure and design </i>', parse_mode='html')


    if message.text == "Introduction To Information Technology  📚":
        bot.send_message(message.chat.id, '<b> Introduction To Information Technology Files 👇 </b>', parse_mode='Html', reply_markup=Menu)
        ITFile1 = open('IT File 1.pdf', 'rb')
        bot.send_document(message.chat.id, ITFile1, caption='<i> IT - 09.02.2022 \n\n Intro </i>', parse_mode='html')
        ITFile2 = open('IT File 2.pptx', 'rb')
        bot.send_document(message.chat.id, ITFile2, caption='<i> IT - 09.02.2022 & 10.02.2022 \n\n Intro + MS Word </i>', parse_mode='html')
        ITFile3 = open('IT File 3.pptx', 'rb')
        bot.send_document(message.chat.id, ITFile3, caption='<i> IT - 16.02.2022 \n\n Computer Security Risks </i>', parse_mode='html')
        ITFile4 = open('IT File 4.pptx', 'rb')
        bot.send_document(message.chat.id, ITFile4, caption='<i> IT - 17.02.2022 \n\n Safety, Ethics, and Privacy </i>', parse_mode='html')
        ITFile5 = open('IT File 5.pptx', 'rb')
        bot.send_document(message.chat.id, ITFile5, caption='<i> IT - 23.02.2022 \n\n Milestones in Computer History </i>', parse_mode='html')
        ITFile6 = open('IT File 6.ppt', 'rb')
        bot.send_document(message.chat.id, ITFile6, caption='<i> IT - Introduction to IT </i>', parse_mode='html')
        ITFile7 = open('IT File 7.pptx', 'rb')
        bot.send_document(message.chat.id, ITFile7, caption='<i> IT - Overview of IT, Microsoft Windows, Microsoft Word </i>', parse_mode='html')
        ITFile8 = open('IT File 8.pptx', 'rb')
        bot.send_document(message.chat.id, ITFile8, caption='<i> IT - Introduction to Microsoft Excel </i>', parse_mode='html')
        ITFile9 = open('IT File 9.pptx', 'rb')
        bot.send_document(message.chat.id, ITFile9, caption='<i> IT - Microsoft PowerPoint </i>', parse_mode='html')
        ITFile10 = open('IT File 10.pptx', 'rb')
        bot.send_document(message.chat.id, ITFile10, caption='<i> IT - Microsoft Excel Functions </i>', parse_mode='html')
        ITFile11 = open('IT File 11.pptx', 'rb')
        bot.send_document(message.chat.id, ITFile11, caption='<i> IT - Microsoft Excel Functions Advanced </i>', parse_mode='html')



    if message.text == "Introduction To Social And Digital Media  📚":
        bot.send_message(message.chat.id, '<b> Introduction To Social And Digital Media Files 👇 </b>', parse_mode='Html', reply_markup=Menu)
        MediaFile1 = open('Media File 1.pptx', 'rb')
        bot.send_document(message.chat.id, MediaFile1, caption='<i> Media - Introduction to Social and Digital Media </i>', parse_mode='html')
        MediaFile2 = open('Media File 2.pptx', 'rb')
        bot.send_document(message.chat.id, MediaFile2, caption='<i> Media - SOCIAL MEDIA AND SOCIETY </i>', parse_mode='html')
        MediaFile3 = open('Media File 3.pptx', 'rb')
        bot.send_document(message.chat.id, MediaFile3, caption='<i> Media - Social Media and Us </i>', parse_mode='html')
        MediaFile4 = open('Media File 4.pptx', 'rb')
        bot.send_document(message.chat.id, MediaFile4, caption='<i> Media - VIRTUAL COMMUNITY AND PARTICIPATORY CULTURE </i>', parse_mode='html')


########################################################################################################################

# # 101
#
#     if message.text == "101":
#         bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Days101)
#
#     if message.text == "Monday (101)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Tuesday (101)":
#         bot.send_message(message.chat.id, '<b> Tuesday 🗓 \n\n Introduction To Social And Digital Media 📚 \n 9:00 AM - 10:20 AM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup = Menu)
#     if message.text == "Wednesday (101)":
#         bot.send_message(message.chat.id, '<b> Wednesday 🗓 \n\n Psychology Applied To Work 📚 \n 9:00 AM - 10:20 AM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup = Menu)
#     if message.text == "Thursday (101)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Friday (101)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Saturday (101)":
#         bot.send_message(message.chat.id, '<b> Saturday 🗓 \n\n Psychology Applied To Work 📚 \n 10:30 AM - 11:50 AM 🕗 \n 302 🔺 </b>', parse_mode='Html', reply_markup = Menu)
#
# # 102
#
#     if message.text == "102":
#         bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Days102)
#
#     if message.text == "Monday (102)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Tuesday (102)":
#         bot.send_message(message.chat.id, '<b> Tuesday 🗓 \n\n Introduction To Social And Digital Media 📚 \n 10:30 AM - 11:50 AM 🕗 \n LR 🔻 </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Wednesday (102)":
#         bot.send_message(message.chat.id, '<b> Wednesday 🗓 \n\n Psychology Applied To Work 📚 \n 9:00 AM - 10:20 AM 🕗 \n LR 🔻 </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Thursday (102)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Friday (102)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Saturday (102)":
#         bot.send_message(message.chat.id, '<b> Saturday 🗓 \n\n Psychology Applied To Work 📚 \n 9:00 AM - 10:20 AM 🕗 \n 402 🔺 </b>', parse_mode = 'Html', reply_markup = Menu)
# # 103
#
#     if message.text == "103":
#         bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Days103)
#
#     if message.text == "Monday (103)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Tuesday (103)":
#         bot.send_message(message.chat.id, '<b> Tuesday 🗓 \n\n Introduction To Social And Digital Media 📚 \n 13:30 PM - 14:50 PM 🕗 \n LR 🔻 </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Wednesday (103)":
#         bot.send_message(message.chat.id, '<b> Wednesday 🗓 \n\n Psychology Applied To Work 📚 \n 10:30 AM - 11:50 AM 🕗 \n LR 🔻 </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Thursday (103)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Friday (103)":
#         bot.send_message(message.chat.id, '<b> Friday 🗓 \n\n Psychology Applied To Work 📚 \n 9:00 AM - 10:20 AM 🕗 \n 302 🔺 </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Saturday (103)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode = 'Html', reply_markup = Menu)
#
# # 104
#
#     if message.text == "104":
#         bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Days104)
#
#     if message.text == "Monday (104)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup = Menu)
#     if message.text == "Tuesday (104)":
#         bot.send_message(message.chat.id, '<b> Tuesday 🗓 \n\n Introduction To Social And Digital Media 📚 \n 12:00 PM - 13:20 PM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup = Menu)
#     if message.text == "Wednesday (104)":
#         bot.send_message(message.chat.id, '<b> Wednesday 🗓 \n\n Psychology Applied To Work 📚 \n 10:30 PM - 11:50 AM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup = Menu)
#     if message.text == "Thursday (104)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Friday (104)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Saturday (104)":
#         bot.send_message(message.chat.id, '<b> Saturday 🗓 \n\n Psychology Applied To Work 📚 \n 10:30 AM - 11:50 AM 🕗 \n 402 🔺 </b>', parse_mode='Html', reply_markup = Menu)
#
# # 105
#
#     if message.text == "105":
#         bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Days105)
#
#     if message.text == "Monday (105)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Tuesday (105)":
#         bot.send_message(message.chat.id, '<b> Tuesday 🗓 \n\n Introduction To Social And Digital Media 📚 \n 13:30 PM - 14:50 PM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Wednesday (105)":
#         bot.send_message(message.chat.id, '<b> Wednesday 🗓 \n\n Psychology Applied To Work 📚 \n 9:00 AM - 10:20 AM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Thursday (105)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Friday (105)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Saturday (105)":
#         bot.send_message(message.chat.id, '<b> Saturday 🗓 \n\n Psychology Applied To Work 📚 \n 12:00 PM - 13:20 PM 🕗 \n 302 🔺 </b>', parse_mode='Html', reply_markup=Menu)
#
# # 106
#
#     if message.text == "106":
#         bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Days106)
#
#     if message.text == "Monday (106)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Tuesday (106)":
#         bot.send_message(message.chat.id, '<b> Tuesday 🗓 \n\n Introduction To Social And Digital Media 📚 \n 12:00 PM - 13:20 PM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Wednesday (106)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Thursday (106)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Friday (106)":
#         bot.send_message(message.chat.id, '<b> Friday 🗓 \n\n Psychology Applied To Work 📚 \n 13:30 PM - 14:50 PM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Saturday (106)":
#         bot.send_message(message.chat.id, '<b> Saturday 🗓 \n\n Psychology Applied To Work 📚 \n 15:00 PM - 16:20 PM 🕗 \n 402 🔺 </b>', parse_mode='Html', reply_markup=Menu)
#
# # 107
#
#     if message.text == "107":
#         bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Days107)
#
#     if message.text == "Monday (107)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌  </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Tuesday (107)":
#         bot.send_message(message.chat.id, '<b> Tuesday 🗓 \n\n Introduction To Social And Digital Media 📚 \n 15:00 PM - 16:20 PM 🕗 \n LR 🔻  </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Wednesday (107)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌  </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Thursday (107)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Friday (107)":
#         bot.send_message(message.chat.id, '<b> Friday 🗓 \n\n Psychology Applied To Work 📚 \n 15:00 PM - 16:20 PM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Saturday (107)":
#         bot.send_message(message.chat.id, '<b> Saturday 🗓 \n\n Psychology Applied To Work 📚 \n 13:30 PM - 14:50 PM 🕗 \n 402 🔺 </b>', parse_mode='Html', reply_markup=Menu)
#
# # 108
#
#     if message.text == "108":
#         bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Days108)
#
#     if message.text == "Monday (108)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Tuesday (108)":
#         bot.send_message(message.chat.id, '<b> Tuesday 🗓 \n\n Introduction To Social And Digital Media 📚 \n 10:30 AM - 11:50 AM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Wednesday (108)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Thursday (108)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Friday (108)":
#         bot.send_message(message.chat.id, '<b> Friday 🗓 \n\n Psychology Applied To Work 📚 \n 13:30 PM - 14:50 PM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Saturday (108)":
#         bot.send_message(message.chat.id, '<b> Saturday 🗓 \n\n Psychology Applied To Work 📚 \n 12:00 PM - 13:20 PM 🕗 \n 402 🔺  </b>', parse_mode='Html', reply_markup=Menu)
#
# # 109
#
#     if message.text == "109":
#         bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Days109)
#
#     if message.text == "Monday (109)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Tuesday (109)":
#         bot.send_message(message.chat.id, '<b> Tuesday 🗓 \n\n Introduction To Social And Digital Media 📚 \n 9:00 AM - 10:20 AM 🕗 \n LR 🔻 </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Wednesday (109)":
#         bot.send_message(message.chat.id, '<b> Wednesday 🗓 \n\n Psychology Applied To Work 📚 \n 10:30 AM - 11:50 AM 🕗 \n LR 🔻  </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Thursday (109)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Friday (109)":
#         bot.send_message(message.chat.id, '<b> Friday 🗓 \n\n Psychology Applied To Work 📚 \n 10:30 AM - 11:50 AM 🕗 \n 302 🔺 </b>', parse_mode = 'Html', reply_markup = Menu)
#     if message.text == "Saturday (109)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode = 'Html', reply_markup = Menu)
#
# # 110
#
#     if message.text == "110":
#         bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Days110)
#
#     if message.text == "Monday (110)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Tuesday (110)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Wednesday (110)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Thursday (110)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Friday (110)":
#         bot.send_message(message.chat.id, '<b> Friday 🗓 \n\n Psychology Applied To Work 📚 \n 15:00 PM - 16:20 PM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup=Menu)#     if message.text == "Saturday (110)":
#         bot.send_message(message.chat.id, '<b> Saturday 🗓 \n\n Psychology Applied To Work 📚 \n 15:00 PM - 16:20 PM 🕗 \n 302 🔺 </b>', parse_mode='Html', reply_markup=Menu)
#
# # 111
#
#     if message.text == "111":
#         bot.send_message(message.chat.id, '<b> Choose The Day 👇 </b>', parse_mode='Html', reply_markup=Days111)
#
#     if message.text == "Monday (111)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Tuesday (111)":
#         bot.send_message(message.chat.id, '<b> Tuesday 🗓 \n\n Introduction To Social And Digital Media 📚 \n 15:00 PM - 16:20 PM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Wednesday (111)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Thursday (111)":
#         bot.send_message(message.chat.id, '<b> Not Scheduled ❌ </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Friday (111)":
#         bot.send_message(message.chat.id, '<b> Friday 🗓 \n\n  Psychology Applied To Work 📚 \n 13:30 PM - 14:50 PM 🕗 \n LR 🔻 </b>', parse_mode='Html', reply_markup=Menu)
#     if message.text == "Saturday (111)":
#         bot.send_message(message.chat.id, '<b> Saturday 🗓 \n\n Psychology Applied To Work 📚 \n 13:30 PM - 14:50 PM 🕗 \n 302 🔺 </b>', parse_mode='Html', reply_markup=Menu)


    if message.text == "Rate Us ⭐️":
        Rate = bot.send_message(message.chat.id, "<b> Please, Rate The Bot 🌟 </b>", parse_mode='Html', reply_markup=Stars)
        bot.register_next_step_handler(Rate, Review)

def Review(message):
    message_to_save = message.text
    RateUserName = message.from_user.username
    NewRateText = 'New Feedback ⚠️'
    UserNameText = 'Username:  @'
    UserIdText = 'User ID:  '
    FeedbackText = 'Feedback:  '
    bot.send_message('@tmcbotratings',
    NewRateText + '\n\n' + UserIdText + str(message.chat.id) + '\n' + UserNameText + str(RateUserName) + '\n\n' + FeedbackText + message_to_save)
    bot.send_message(message.chat.id, '<b> Thanks For Rating  🙏 </b>', parse_mode='Html', reply_markup=Main)


########################################################################################################################

# START BOT

if __name__ == '__main__':
    bot.polling(non_stop=True)