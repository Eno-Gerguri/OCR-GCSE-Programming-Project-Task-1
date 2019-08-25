# Variables
usernames_and_passwords = []  # This list stores the users and their passwords from, "Users.txt" refer to line 12


def get_usernames_and_passwords():  # This a
    opening_the_list = open("Users.txt", "r")

    true_a = [line.split(",") for line in opening_the_list.readlines()]
    true_a = sum(true_a, [])

    for i in true_a:
        a = i.strip("\n")

        true_a.insert(true_a.index(i), a)
        true_a.remove(i)

    usernames_and_passwords.clear()
    usernames_and_passwords.extend(true_a)

    opening_the_list.close()


def authenticate_user():
    username_is_correct = False
    password_is_correct = False

    print("Welcome to the music game!\n\n")

    entered_username = input("Enter your Username: ")

    for i, line in enumerate(usernames_and_passwords):

        if i % 2 != 0:

            if line == entered_username:
                username_is_correct = True

    if username_is_correct:

        entered_password = input("Enter your Password: ")

        for i, line in enumerate(usernames_and_passwords):

            if i % 2 == 0:

                if line == entered_password:
                    password_is_correct = True

    elif username_is_correct is False:

        print("\n\nUsername is Incorrect\n\n")

        authenticate_user()

    if password_is_correct:

        pass  # Do the next part

    elif password_is_correct is False:

        print("\n\nPassword is Incorrect\n\n")

        authenticate_user()
