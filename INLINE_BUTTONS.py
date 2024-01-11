from telebot import types, telebot

class Inline_Buttons:



    #  CREATE A CLUB #

    CreateTheClubButton = types.InlineKeyboardMarkup(row_width=2)
    CreateTheClubLink = types.InlineKeyboardButton(text="Create a club", url="https://t.me/ShaHriXMusic")
    CreateTheClubButton.add(CreateTheClubLink)

    #  SPEAKING CLUB LINK  #

    SpeakingClubButton = types.InlineKeyboardMarkup(row_width=2)
    SpeakingClubChannelLink = types.InlineKeyboardButton(text="Join  ✅", url="https://t.me/englishhub_tmc")
    SpeakingClubButton.add(SpeakingClubChannelLink)

    #  CONTACT US  #

    SupportButton = types.InlineKeyboardMarkup(row_width=2)
    FounderButton1 = types.InlineKeyboardButton(text="Shahrizod", url="https://t.me/ShaHriXMusic")
    FounderButton2 = types.InlineKeyboardButton(text="Ulugbekhon", url="https://t.me/theulugbekhon")
    SupportButton.add(FounderButton1, FounderButton2)



    ClubsButton = telebot.types.InlineKeyboardMarkup(row_width=2)
    club_1 = types.InlineKeyboardButton(text="Speaking club", callback_data="club_1")
    club_2 = types.InlineKeyboardButton(text="Club 2", callback_data="club_2")
    club_3 = types.InlineKeyboardButton(text="Club 3", callback_data="club_3")
    club_4 = types.InlineKeyboardButton(text="Club 4", callback_data="club_4")
    club_5 = types.InlineKeyboardButton(text="Club 5", callback_data="club_5")
    club_6 = types.InlineKeyboardButton(text="Club 6", callback_data="club_6")
    ClubsButton.add(club_1, club_2, club_3, club_4, club_5, club_6)




    ProjectManagement_1 = telebot.types.InlineKeyboardMarkup(row_width=1)
    P_M_File_1 = types.InlineKeyboardButton(text="Project Scope Management", callback_data="P_M_Session_1")
    P_M_File_2 = types.InlineKeyboardButton(text="Project Management Methodologies", callback_data="P_M_Session_2")
    P_M_File_3 = types.InlineKeyboardButton(text="Introduction to Project Management", callback_data="P_M_Session_3")
    P_M_File_4 = types.InlineKeyboardButton(text="Empty", callback_data="session_4")
    P_M_File_5 = types.InlineKeyboardButton(text="Empty", callback_data="session_5")
    P_M_File_6 = types.InlineKeyboardButton(text="Empty", callback_data="session_6")
    P_M_File_7 = types.InlineKeyboardButton(text="Empty", callback_data="session_7")
    P_M_File_8 = types.InlineKeyboardButton(text="Empty", callback_data="session_8")
    P_M_File_9 = types.InlineKeyboardButton(text="Empty", callback_data="session_9")
    P_M_File_10 = types.InlineKeyboardButton(text="Empty", callback_data="session_10")
    ProjectManagement_Next_Page = types.InlineKeyboardButton(text="Next page   ➡", callback_data="P_M_Next")
    ProjectManagement_1.add(P_M_File_1, P_M_File_2, P_M_File_3, P_M_File_4, P_M_File_5, P_M_File_6, P_M_File_7, P_M_File_8, P_M_File_9, P_M_File_10, ProjectManagement_Next_Page)

    ProjectManagement_2 = telebot.types.InlineKeyboardMarkup(row_width=1)
    file_11 = types.InlineKeyboardButton(text="Empty", callback_data="session_11")
    file_12 = types.InlineKeyboardButton(text="Empty", callback_data="session_12")
    file_13 = types.InlineKeyboardButton(text="Empty", callback_data="session_13")
    file_14 = types.InlineKeyboardButton(text="Empty", callback_data="session_14")
    file_15 = types.InlineKeyboardButton(text="Empty", callback_data="session_15")
    file_16 = types.InlineKeyboardButton(text="Empty", callback_data="session_16")
    file_17 = types.InlineKeyboardButton(text="Empty", callback_data="session_17")
    file_18 = types.InlineKeyboardButton(text="Empty", callback_data="session_18")
    file_19 = types.InlineKeyboardButton(text="Empty", callback_data="session_19")
    file_20 = types.InlineKeyboardButton(text="Empty", callback_data="session_20")
    ProjectManagement_Previous_Page = types.InlineKeyboardButton(text="Previous page   ⬅", callback_data="P_M_Back")
    ProjectManagement_2.add(file_11, file_12, file_13, file_14, file_15, file_16, file_17, file_18, file_19, file_20, ProjectManagement_Previous_Page)





