import telebot


class English_Buttons:



    #  REGISTRATION BUTTONS  #

    EnglishRegCourseButtons = telebot.types.ReplyKeyboardMarkup(True)
    EnglishRegCourseButtons.row("Foundation", "Year 2")

    FoundationRegGroupButtons = telebot.types.ReplyKeyboardMarkup(True)
    FoundationRegGroupButtons.row("101", "102", "103", "104")
    FoundationRegGroupButtons.row("105", "106", "107", "108")
    FoundationRegGroupButtons.row("109", "110", "111", "112")
    FoundationRegGroupButtons.row("113", "114")

    SecondCourseRegGroupButtons = telebot.types.ReplyKeyboardMarkup(True)
    SecondCourseRegGroupButtons.row("201", "202", "203")
    SecondCourseRegGroupButtons.row("204", "205", "206")
    SecondCourseRegGroupButtons.row("207", "208", "209")



    #  MENU BUTTON  #

    MenuButtons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    MenuButtons.row("Timetable  🗓", "Deadlines ❗")
    MenuButtons.row("Events  🎉", "Clubs  🎲", "News  📬")
    MenuButtons.row("Files  📁", "Contact Us  🆘")
    MenuButtons.row("Profile  👤")



    #  WEEK DAYS BUTTON  #

    WeekDaysButtons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    WeekDaysButtons.row("Monday", "Tuesday", "Wednesday")
    WeekDaysButtons.row("Thursday", "Friday", "Saturday")
    WeekDaysButtons.row("Main Menu  🏠")



    #  DEADLINES BUTTON  #

    DeadlinesButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    DeadlinesButton.row("Dates  🗓", "Assignment Materials  📑")
    DeadlinesButton.row("Main Menu  🏠")

    FilesButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    FilesButton.row("Task Descriptions  📝", "Lectures & Tutorials (PPTs)  📁")

    SubjectsButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    SubjectsButton.row("Psychology Applied To Work  📚")
    SubjectsButton.row("Introduction To Information Technology  📚")
    SubjectsButton.row("Introduction To Social And Digital Media  📚")



    #  CLUBS BUTTON  #

    ClubsButtons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    ClubsButtons.row("Speaking club", "Club 2", "Club 3")
    ClubsButtons.row("Club 4", "Club 5", "Club 6")
    ClubsButtons.row("Main Menu  🏠")



    #  FILES BUTTON  #


    FilesCourseButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    FilesCourseButton.row("Foundation  📁", "2  -  Year  📁")


    FoundationSubjectsButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    FoundationSubjectsButton.row("Communication  📁")
    FoundationSubjectsButton.row("Introduction to Information Technology  📁")
    FoundationSubjectsButton.row("Introduction to Study Skills  📁")
    FoundationSubjectsButton.row("Introduction to Social and Digital Media  📁")
    FoundationSubjectsButton.row("Psychology Applied to Work  📁")
    FoundationSubjectsButton.row("Main Menu  🏠")


    AccountingFilesButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    AccountingFilesButton.row("Business Communication and ICT  📁")
    AccountingFilesButton.row("Introduction to Management  📁")
    AccountingFilesButton.row("Marketing for Managers  📁")
    AccountingFilesButton.row("Main Menu  🏠")

    BusinessFilesButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    BusinessFilesButton.row("Business Communication and ICT  📁")
    BusinessFilesButton.row("Introduction to Management  📁")
    BusinessFilesButton.row("Marketing for Managers  📁")
    BusinessFilesButton.row("Main Menu  🏠")

    ITFilesButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    ITFilesButton.row("Project Management  📁")
    ITFilesButton.row("Application Programming with Java  📁")
    ITFilesButton.row("Database Systems  📁")
    ITFilesButton.row("Main Menu  🏠")

    LogisticsFilesButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    LogisticsFilesButton.row("Business Communication and ICT  📁")
    LogisticsFilesButton.row("Introduction for Management  📁")
    LogisticsFilesButton.row("Marketing for Managers  📁")
    LogisticsFilesButton.row("Main Menu  🏠")

    TourismFilesButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    TourismFilesButton.row("ICT in the Hospitality and Leisure Industry  📁")
    TourismFilesButton.row("International Hotel and Resort Management  📁")
    TourismFilesButton.row("Marketing for Hospitality and Leisure  📁")
    TourismFilesButton.row("Main Menu  🏠")





    MajorFilesButton = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    MajorFilesButton.row("Accounting", "Business", "IT")
    MajorFilesButton.row("Logistics", "Tourism")






    # PROFILE BUTTON  #

    VerificationButtons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    VerificationButtons.row("Verification  ✅")
    VerificationButtons.row("Main Menu  🏠")



    #  ADMIN BUTTON  #

    AdminButtons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    AdminButtons.row("CHANGE THE GROUP")
    AdminButtons.row("Main Menu  🏠")



