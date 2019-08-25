# Variables
usernames_and_passwords = []  # This list stores the users and their passwords from, "Users.txt" refer to line 7


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
    If, "Users.txt" is empty then the user is prompted to make a new account that will be saved.
    If, "Users.txt" is not empty then the user is prompted to enter their username and password
    and if they are correct are successfully logged into the game.
    If, the user does not have an account they type in "Sign Up" to make an account for themselves.
    """

# ======================================================================================================================
    # This section of code is activated if it is the first time this program is being run

    if len(usernames_and_passwords) == 0:
        print("Welcome to the music game!\n\n")

        print("I have detected it is your first time here\n\n")

        print("Sign up:\n\n")

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

# ======================================================================================================================
    # This section of code prompts the user to type in their details

    username_is_correct = False  # Username is automatically set to incorrect to simplify code
    password_is_correct = False  # Password is automatically set to incorrect to simplify code

    print("Welcome to the music game!\n\n")

    entered_username = input("Enter your Username: ")

    for i, line in enumerate(usernames_and_passwords):

        if i % 2 == 0:  # Usernames are located on the even spots of the list

            if line == entered_username:
                username_is_correct = True

    if username_is_correct:

        entered_password = input("Enter your Password: ")

        for i, line in enumerate(usernames_and_passwords):

            if i % 2 != 0:  # Passwords are located on the odd spots of the list

                if line == entered_password:
                    password_is_correct = True

    elif username_is_correct is False:

        print("\n\nUsername is Incorrect\n\n")

        authenticate_user()

    if password_is_correct:

        print("\n\nSuccessfully logged in!\n\n")  # Will automatically call the next function in, "Main_Script.py" It is the only way out of this function

    elif password_is_correct is False:

        print("\n\nPassword is Incorrect\n\n")

        authenticate_user()

# ======================================================================================================================
# ======================================================================================================================