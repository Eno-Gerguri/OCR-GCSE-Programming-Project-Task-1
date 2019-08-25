# Variables
usernames_and_passwords = []  # This list stores the users and their passwords from, "Users.txt" refer to line 7


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

def sign_up_user():
    with open("lists.txt", "w") as f:
        for item in usernames_and_passwords:
            f.write("%s\n" % item)

# ======================================================================================================================

def authenticate_user():
    if len(usernames_and_passwords) == 0:
        print("Welcome to the music game!\n\n")
        print("I have detected it is your first time here\n\n")
        print("Sign up:\n\n")
        sign_up_username = input("Enter your new Username: ")
        sign_up_password = input("Enter your new Password: ")
        sign_up_password_check = input("Re-enter your password: ")

        if sign_up_password == sign_up_password_check:
            usernames_and_passwords.append(sign_up_username)
            usernames_and_passwords.append(sign_up_password)
            sign_up_user()

        elif sign_up_password != sign_up_password_check:
            print("\n\nPasswords do not match\n\n")
            authenticate_user()

    username_is_correct = False
    password_is_correct = False

    print("Welcome to the music game!\n\n")

    entered_username = input("Enter your Username: ")

    for i, line in enumerate(usernames_and_passwords):

        if i % 2 == 0:

            if line == entered_username:
                username_is_correct = True

    if username_is_correct:

        entered_password = input("Enter your Password: ")

        for i, line in enumerate(usernames_and_passwords):

            if i % 2 != 0:

                if line == entered_password:
                    password_is_correct = True

    elif username_is_correct is False:

        print("\n\nUsername is Incorrect\n\n")

        authenticate_user()

    if password_is_correct:

        print("\n\nLogin Successful!\n\n")  # Do the next part

    elif password_is_correct is False:

        print("\n\nPassword is Incorrect\n\n")

        authenticate_user()

# ======================================================================================================================
