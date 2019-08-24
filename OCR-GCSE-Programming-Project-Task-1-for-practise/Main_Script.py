class User:
    
    def __init__(self, Username, Password):

        self.Username = Username
        self.Password = Password 


def  Authenticate_User():
    username_is_correct = False
    password_is_correct = False

    print("Welcome to the music game!\n\n")

    Entered_Username = input("Enter your Username: ")

    with open("Users.txt", "r") as f:

        count = 0

        for line in f:

           count += 1

           if count % 2 != 0:

               if line == Entered_Username:
                   username_is_correct = True

                elif line != Entered_Username:
                    pass
            
            elif count % 2 == 0:
                pass

    if username_is_correct is True:

        Entered_Password = input("Enter your Password: ")

        with open("Users.txt", "r") as f:

            count = 0

            for line in f:

                count += 1

                if count % 2 == 0:

                    if line == Entered_Password:
                        password_is_correct = True

                    elif line != Entered_Password:
                        pass

                elif count % 2 != 0:
                    pass

    elif username_is_correct is False:
        print("\n\nUsername is Incorrect\n\n")
        Authenticate_User()


# ======================================================================

# Code Starts Here

Authenticate_User()