import telebot


class Russian_Buttons:


    #  MENU BUTTON  #

    MenuButtons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    MenuButtons.row("Расписание  🗓", "Дэдлайны ❗")
    MenuButtons.row("События  🎉", "Клубы  🎲", "Новости  📬")
    MenuButtons.row("Поддержка  🆘", "Язык  🌐")
    MenuButtons.row("Профиль  👤")

    #  WEEK DAYS BUTTON  #

    WeekDaysButtons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    WeekDaysButtons.row("Понедельник", "Вторник", "Среда")
    WeekDaysButtons.row("Четверг", "Пятница", "Суббота")
    WeekDaysButtons.row("Главное Меню  🏠")

    #  DEADLINES BUTTON  #

    DeadlinesButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    DeadlinesButton.row("Даты  🗓", "Материалы для задания  📑")
    DeadlinesButton.row("Главное Меню  🏠")

    #  CLUBS BUTTON  #

    ClubsButtons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    ClubsButtons.row("Speaking клуб  ⏳", "Клуб 2", "Клуб 3")
    ClubsButtons.row("Клуб 4", "Клуб 5", "Клуб 6")
    ClubsButtons.row("Главное Меню  🏠")

    #  PORFILE BUTTONS  #

    VerificationButtons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    VerificationButtons.row("Верификация  ✅")
    VerificationButtons.row("Главное Меню  🏠")


