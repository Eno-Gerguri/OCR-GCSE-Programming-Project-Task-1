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

# ======================================================================================================================

def authenticate_user():
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
