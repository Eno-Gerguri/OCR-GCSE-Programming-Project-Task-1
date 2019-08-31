from Authenticate_User import get_usernames_and_passwords, authenticate_user
from Music_Game import get_artists_and_songs, start_music_game


# ====================================================initialisation====================================================
# ======================================================================================================================

get_usernames_and_passwords()

get_artists_and_songs()


# ======================================================================================================================
# ======================================================================================================================

def usernames_and_passwords_into_users_txt():
    """
    Gets the, "usernames_and_passwords" list and puts it into, "Users.txt" line by line for each item.
    """

    with open("Users.txt", "w") as f:

        for item in usernames_and_passwords:

            f.write("%s\n" % item)


# ======================================================================================================================
# ======================================================================================================================

def artists_and_songs_into_song_list_txt():
    """
    Gets the, "artists_and_songs" list and puts it into, "Song_List.txt" line by line for each item.
    """

    with open("Song_List.txt", "w") as f:

        for item in artists_and_songs:

            f.write("%s\n" % item)


# ======================================================================================================================
# ======================================================================================================================

from Authenticate_User import usernames_and_passwords

# Imports, "usernames_and_passwords" list after initialisation

from Music_Game import artists_and_songs

# Imports, "artists_and_songs" list after initialisation


def main_menu():

    print("Main Menu\n\n")

    print("Play\n\nSettings\n\nSign Out\n\nExit\n\n")

    picked_option = input()

    print("\n\n")

    if picked_option.lower().strip().replace(" ", "") == "play":

        start_music_game()

        main_menu()  # Returns to main menu

    elif picked_option.lower().strip().replace(" ", "") == "settings":

        settings()

    elif picked_option.lower().strip().replace(" ", "") == "signout":

        authenticate_user()  # Goes back to the sign in menu

        main_menu()  # Returns to main menu

    elif picked_option.lower().strip().replace(" ", "") == "exit":

        print("Goodbye!\n\n")

        quit()

    else:

        print("That is invalid. Check your spelling.\n\n")

        main_menu()


# ======================================================================================================================
# ======================================================================================================================

def settings():

    print("Settings\n\n")

    print("Account Settings\n\nSong Settings\n\nScore Settings\n\nBack\n\n")

    picked_setting = input()

    print("\n\n")


# ======================================================================================================================
# This section of code is the Account Settings

    if picked_setting.lower().strip().replace(" ", "") == "accountsettings":

        print("Account Settings\n\n")

        print("Change Username\n\nChange Password\n\nDelete Account\n\nBack\n\n")

        picked_account_setting = input()

        print("\n\n")

        if picked_account_setting.lower().strip().replace(" ", "") == "changeusername":

            change_username()

        elif picked_account_setting.lower().strip().replace(" ", "") == "changepassword":

            change_password()

        elif picked_account_setting.lower().strip().replace(" ", "") == "deleteaccount":

            picked_are_you_sure_option = input("Are you sure?(yes/no)\n\n")

            print("\n\n")

            if picked_are_you_sure_option.lower().strip().replace(" ", "") == "yes":

                delete_account()

            elif picked_are_you_sure_option.lower().strip().replace(" ", "") == "no":

                print("Operation cancelled.\n\n")

                settings()

            else:

                print("That is invalid. Check your spelling.\n\n")

                settings()

            delete_account()

        elif picked_account_setting.lower().strip().replace(" ", "") == "back":

            settings()

        else:

            print("That is invalid. Check your spelling.\n\n")

            settings()


# ======================================================================================================================
# This section of code is the Song Settings

    elif picked_setting.lower().strip().replace(" ", "") == "songsettings":

        print("Song Settings\n\n")

        print("Add Song\n\nEdit Song\n\nDelete Song\n\nBack\n\n")

        picked_song_setting = input()

        print("\n\n")

        if picked_song_setting.lower().strip().replace(" ", "") == "addsong":

            pass  # TODO: add a add song function

        elif picked_song_setting.lower().strip().replace(" ", "") == "editsong":

            pass  # TODO: add a edit song function

        elif picked_song_setting.lower().strip().replace(" ", "") == "deletesong":

            pass  # TODO: add a delete song function

        elif picked_song_setting.lower().strip().replace(" ", "") == "back":

            settings()

        else:

            print("That is invalid. Check your spelling.\n\n")

            settings()


# ======================================================================================================================
# This section of code is the Score Settings

    elif picked_setting.lower().strip().replace(" ", "") == "scoresettings":

        print("Score Settings\n\n")

        print("View Scores\n\nDelete All Scores\n\nBack\n\n")

        picked_score_setting = input()

        print("\n\n")

        if picked_score_setting.lower().strip().replace(" ", "") == "View Scores":

            pass  # TODO: add a view scores function

        elif picked_score_setting.lower().strip().replace(" ", "") == "Delete All Scores":

            # This one is built-in to the, "settings" function because of its simplicity

            picked_are_you_sure_option = input("Are you sure?(yes/no)\n\n")

            print("\n\n")

            if picked_are_you_sure_option.lower().strip().replace(" ", "") == "yes":

                open('Scores.txt', 'w').close()

                settings()

            elif picked_are_you_sure_option.lower().strip().replace(" ", "") == "no":

                print("Operation cancelled.\n\n")

                settings()

            else:

                print("That is invalid. Check your spelling.\n\n")

                settings()

        else:

            print("That is invalid. Check your spelling.\n\n")

            settings()


# ======================================================================================================================

    elif picked_setting.lower().strip().replace(" ", "") == "back":

        main_menu()

    else:

        print("That is invalid. Check your spelling.\n\n")

        settings()


# ======================================================================================================================
# ======================================================================================================================

def change_username():
    """
    Gets user input for their username, then gets user input for the new username that has to be entered twice to make
    sure it was entered correctly. Changes the old username to the new username and stores it in, "Users.txt".
    """

    username_is_correct = False

    print("Change Username\n\n")

    original_username = input("Type your current Username: ")

    for i, line in enumerate(usernames_and_passwords):

        if i % 2 == 0:  # Usernames are located on the even spots of the list

            if line == original_username:  # If the username typed exists

                username_is_correct = True

                global index

                index = i

    if username_is_correct:

        new_username = input("Type your new Username: ")

        new_username_confirm = input("Re-enter your new Username: ")

        print("\n\n")

        if new_username == new_username_confirm:

            usernames_and_passwords.insert(index, new_username)

            usernames_and_passwords.pop(index + 1)

            usernames_and_passwords_into_users_txt()

            print("Successfully changed Username\n\n")

            settings()

        else:

            print("Usernames do not match. Please check your spelling.\n\n")

            settings()

            return

    elif username_is_correct is False:

        print("That is invalid. Check your spelling.\n\n")

        settings()

        return


# ======================================================================================================================
# ======================================================================================================================

def change_password():
    """
    Gets user input for their password, then gets user input for the new password that has to be entered twice to make
    sure it was entered correctly. Changes the old password to the new password and stores it in, "Users.txt".
    """

    password_is_correct = False

    print("Change Password\n\n")

    original_password = input("Type your current Password: ")

    for i, line in enumerate(usernames_and_passwords):

        if i % 2 != 0:  # Passwords are located on the odd spots of the list

            if line == original_password:  # If password typed exists

                password_is_correct = True

                global password_index

                password_index = i

    if password_is_correct:

        new_password = input("Type your new Password: ")

        new_password_confirm = input("Re-enter your new Password: ")

        print("\n\n")

        if new_password == new_password_confirm:

            usernames_and_passwords.insert(password_index, new_password)

            usernames_and_passwords.pop(password_index + 1)

            usernames_and_passwords_into_users_txt()

            print("Successfully changed Password")

            settings()

        else:

            print("Password do not match. Please check your spelling.\n\n")

            settings()

            return

    elif password_is_correct is False:

        print("That is invalid. Check your spelling.\n\n")

        settings()

        return


# ======================================================================================================================
# ======================================================================================================================

def delete_account():
    """
    Gets user input for their username and password, checks if they are correct and then removes them from, "Users.txt".
    """

    username_is_correct = False

    password_is_correct = False

    print("Delete Account\n\n")

    typed_username = input("Enter your Username: ")

    for i, line in enumerate(usernames_and_passwords):

        if i % 2 == 0:  # Usernames are located on the even spots of the list

            if line == typed_username:  # If username exists

                username_is_correct = True

    if username_is_correct:

        global typed_password

        typed_password = input("Enter your Password: ")

        print("\n\n")

        for i, line in enumerate(usernames_and_passwords):

            if i % 2 != 0:  # Passwords are located on the odd spots of the list

                if line == typed_password:  # If correct password exists

                    password_is_correct = True

    elif username_is_correct is False:

        print("That is invalid. Check your spelling.\n\n")

        settings()

        return

    if password_is_correct:

        usernames_and_passwords.remove(typed_username)

        usernames_and_passwords.remove(typed_password)

        usernames_and_passwords_into_users_txt()

        print("Account Successfully Deleted\n\n")

        settings()

    elif password_is_correct is False:

        print("That is invalid. Check your spelling.\n\n")

        settings()

        return


# ======================================================================================================================
# ======================================================================================================================

def add_song():
    """
    Takes in user input for artist name and song name and puts it into, "Song_List.txt".
    """

    print("Add Song\n\n")

    typed_artist = input("Type the Artist: ")

    typed_song_name = input("Type the Song Name: ")

    print("\n\n")

    artists_and_songs.append(typed_artist)

    artists_and_songs.append(typed_song_name)

    artists_and_songs_into_song_list_txt()

    print("Successfully added song!\n\n")

    settings()


# ======================================================================================================================
# ======================================================================================================================

def change_song():

    print("Change Song\n\n")

    original_artist = input("Type in the Artist's name: ")

    for i, line in enumerate(artists_and_songs):

        if 1:
            pass


# ====================================================Program Starts====================================================
# ======================================================================================================================

authenticate_user()

main_menu()
