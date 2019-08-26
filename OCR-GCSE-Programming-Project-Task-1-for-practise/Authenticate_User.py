# Variables
usernames_and_passwords = []  # This list stores the users and their passwords from, "Users.txt" refer to line 10

signed_in_username = ""

# ======================================================================================================================
# ======================================================================================================================

def get_usernames_and_passwords():
    """
    Takes the usernames and passwords from, "Users.txt" and puts them in the usernames_and_passwords list
    in an order of ["username", "password"] repeating in the list.
    """
    opening_the_list = open("Users.txt", "r")

    true_a = [line.split(",") for line in opening_the_list.readlines()]  # splits each line of the text file into a list
    true_a = sum(true_a, [])

    for i in true_a:
        # Takes the extra "\n" from each string and replaces them accordingly

        a = i.strip("\n")

        true_a.insert(true_a.index(i), a)
        true_a.remove(i)

    usernames_and_passwords.clear()
    usernames_and_passwords.extend(true_a)

    opening_the_list.close()


# ======================================================================================================================
# ======================================================================================================================

def sign_up_user():
    """
    This writes in the, "usernames_and_passwords" list into, "Users.txt" line by line for each item in the list
    """

    with open("Users.txt", "w") as f:
        for item in usernames_and_passwords:
            f.write("%s\n" % item)


# ======================================================================================================================
# ======================================================================================================================

def authenticate_user():
    """
    Users are prompted to sign in or create an account.
    Creating an account will store their details onto, "Users.txt"
    Signing in will prompt them to enter their username and password,
    which will both be checked to see if they are correct,
    if they are the user will now be able to begin the game
    """

# ======================================================================================================================
# This section of code is activated if it is the first time this program is being run

    print("Welcome to the music game!\n\n")
    sign_in_or_create_account_option = input("Sign in\nCreate an account\n\n")

    if sign_in_or_create_account_option.lower().strip().replace(" ", "") == "createanaccount":
        print("\n\nSign up:\n\n")

        sign_up_username = input("Enter your new Username: ")

        sign_up_password = input("Enter your new Password: ")

        sign_up_password_check = input("Re-enter your password: ")

        if sign_up_password == sign_up_password_check:
            # The, "usernames_and_passwords" list acts as a bridge between the, "Users.txt" file and the code

            usernames_and_passwords.append(sign_up_username)

            usernames_and_passwords.append(sign_up_password)

            sign_up_user()

            print("\n\nAccount has been Successfully created!\n\n")

        elif sign_up_password != sign_up_password_check:
            print("\n\nPasswords do not match\n\n")

            authenticate_user()

            return  # Return is there so the second half of this function is not looped through once it ends

    elif sign_in_or_create_account_option.lower().strip().replace(" ", "") == "signin":
        print("\n\n")  # Will automatically move onto the sign-in page

    else:
        print("\n\nSorry that is invalid. Try checking your spelling.\n\n")

        authenticate_user()

        return  # Return is there so the second half of this function is not looped through once it ends

# ======================================================================================================================
# This section of code prompts the user to type in their details

    username_is_correct = False  # Username is automatically set to incorrect to simplify code
    password_is_correct = False  # Password is automatically set to incorrect to simplify code

    entered_username = input("Enter your Username: ")

    for i, line in enumerate(usernames_and_passwords):  # "line" is the username

        if i % 2 == 0:  # Usernames are located on the even spots of the list

            if line == entered_username:
                username_is_correct = True
                signed_in_username = line

    if username_is_correct:

        entered_password = input("Enter your Password: ")

        for i, line in enumerate(usernames_and_passwords):  # "line" is the password

            if i % 2 != 0:  # Passwords are located on the odd spots of the list

                if line == entered_password:
                    password_is_correct = True

    elif username_is_correct is False:

        print("\n\nUsername is Incorrect\n\n")

        authenticate_user()

        return

    if password_is_correct:

        print("\n\nSuccessfully logged in!\n\n")  # Will automatically call the next function in, "Main_Script.py"

    elif password_is_correct is False:

        print("\n\nPassword is Incorrect\n\n")

        authenticate_user()

        return

# ======================================================================================================================
# ======================================================================================================================
