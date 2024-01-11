from telebot import telebot

    # bot.send_message(message.chat.id, f"<b>{}"
    #                                   f"\n\n{}"
    #                                   f"\n{}"
    #                                   f"\n{}"
    #                                   f"\n{}"
    #                                   f"\n{}"
    #                                   f"\n\n{}"
    #                                   f"\n{}"
    #                                   f"\n{}"
    #                                   f"\n{}"
    #                                   f"\n{}"
    #                                   f"</b>", parse_mode='html', reply_markup=English_Buttons.WeekDaysButtons)


class Buttons:


    #  REGISTRATION BUTTONS  #


    RegistrationLanguageButtons = telebot.types.ReplyKeyboardMarkup(True)
    RegistrationLanguageButtons.row("🇺🇸  English  🇺🇸")
    RegistrationLanguageButtons.row("🇷🇺  Русский  🇷🇺")
    # RegistrationLanguageButtons.row("🇺🇿  O'zbek  🇺🇿")



    LanguageButtons = telebot.types.ReplyKeyboardMarkup(True)
    LanguageButtons.row("🇺🇸  English  🇺🇸")
    LanguageButtons.row("🇷🇺  Русский  🇷🇺")


    EnglishRegTypeButtons = telebot.types.ReplyKeyboardMarkup(True)
    EnglishRegTypeButtons.row("International Group", "Uzbek Group")

    RussianRegTypeButtons = telebot.types.ReplyKeyboardMarkup(True)
    RussianRegTypeButtons.row("Международная Группа", "Узбекская Группа")





    EnglishRegCourseButtons = telebot.types.ReplyKeyboardMarkup(True)
    EnglishRegCourseButtons.row("Foundation", "2  -  Year")

    RussianRegCourseButtons = telebot.types.ReplyKeyboardMarkup(True)
    RussianRegCourseButtons.row("Первый Курс", "Второй Курс")



    FoundationRegGroupButtons = telebot.types.ReplyKeyboardMarkup(True)
    FoundationRegGroupButtons.row("101", "102", "103", "104")
    FoundationRegGroupButtons.row("105", "106", "107", "108")
    FoundationRegGroupButtons.row("109", "110", "111", "112")
    FoundationRegGroupButtons.row("113", "114")

    SecondCourseRegGroupButtons = telebot.types.ReplyKeyboardMarkup(True)
    SecondCourseRegGroupButtons.row("201", "202", "203")
    SecondCourseRegGroupButtons.row("204", "205", "206")
    SecondCourseRegGroupButtons.row("207", "208", "209")



    #  MENU BUTTONS  #


    MenuButtons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    MenuButtons.row("Timetable  🗓", "DeadLines ❗")
    MenuButtons.row("Events  🎉", "Games  🎮")
    MenuButtons.row("Contact Us  🆘", "Rate Us  ⭐")

    Games = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    Games.row("Dart  🎯", "Dice  🎲", "Slot Machine  🎰")
    Games.row("Football  ⚽️", "Basketball  🏀")

    Stars = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    Stars.row("⭐", "⭐⭐", "⭐⭐⭐")
    Stars.row("⭐⭐⭐⭐", "⭐⭐⭐⭐⭐")

    Groups = telebot.types.ReplyKeyboardMarkup(True)
    Groups.row("101", "102", "103", "104", "105")
    Groups.row("106", "107", "108", "109", "110")
    Groups.row("", "111", "")

    DeadlineButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    DeadlineButton.row("Dates  🗓", "Assignment Materials  📑")

    FilesButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    FilesButton.row("Task Descriptions  📝", "Lectures & Tutorials (PPTs)  📁")

    SubjectsButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    SubjectsButton.row("Psychology Applied To Work  📚")
    SubjectsButton.row("Introduction To Information Technology  📚")
    SubjectsButton.row("Introduction To Social And Digital Media  📚")

    # DAYS BUTTONS





























