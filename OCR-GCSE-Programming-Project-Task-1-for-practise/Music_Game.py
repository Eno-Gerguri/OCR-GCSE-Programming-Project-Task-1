from random import randint

artists_and_songs = []  # This list stores the artists and their songs from, "Song_List.txt" refer to line 13

scores = []

high_scores = []


# ======================================================================================================================
# ======================================================================================================================

def get_artists_and_songs():
    """
    Takes the Artists and Songs from, "Song_List.txt" and puts them in the artists_and_songs list
    in an order of ["artist", "song"] repeating in the list.
    """
    opening_the_list = open("Song_List.txt", "r")

    true_a = [line.split(",") for line in opening_the_list.readlines()]  # splits each line of the text file into a list

    true_a = sum(true_a, [])

    for i in true_a:
        # Takes the extra "\n" from each string and replaces them accordingly

        a = i.strip("\n")

        true_a.insert(true_a.index(i), a)

        true_a.remove(i)

    artists_and_songs.clear()

    artists_and_songs.extend(true_a)

    opening_the_list.close()


# ======================================================================================================================
# ======================================================================================================================

def record_score():
    with open("Scores.txt", "a") as f:
        f.write("%s\n" % player_points)  # Appends the players points to, "Scores.txt"


# ======================================================================================================================
# ======================================================================================================================

def get_scores():
    opening_the_list = open("Scores.txt", "r")

    true_a = [line.split(",") for line in opening_the_list.readlines()]  # splits each line of the text file into a list

    true_a = sum(true_a, [])

    for i in true_a:
        # Takes the extra "\n" from each string and replaces them accordingly

        a = i.strip("\n")

        true_a.insert(true_a.index(i), a)

        true_a.remove(i)

    scores.clear()

    scores.extend(true_a)

    opening_the_list.close()

    true_scores = [int(i) for i in scores]

    for i in range(5):
        try:
            high_score = max(true_scores)  # Gets highest score from, "true_scores"

            high_scores.append(high_score)  # Adds it to, "high_scores" list

            true_scores.remove(high_score)  # Removes it from, "true_scores"
        except ValueError:
            high_scores.append("-")


# ======================================================================================================================
# ======================================================================================================================

def print_scores():
    for i in high_scores:
        if isinstance(i, int):
            print(str(i))

        else:  # If it is a string
            print(i)

        print("\n")


# ======================================================================================================================
# ======================================================================================================================

number_of_songs_used = 1  # Keeps count of what song you are on

player_points = 0


def start_music_game():
    """
    Completes steps 3 and 4 of Task
    Plays game as intended displaying the artist and the first letter of the name of the song replacing the rest with,
    "*". Player gets two tries to guess the song or the game ends storing their score in an external file
    and displaying the top 5 scores from that file.
    The player gets +3 points for getting it right first time and +1 point for getting it right on the second try
    """
    global player_points

    print("Music Game!\n\n")

    while len(artists_and_songs) != 0:  # Game loop
        global number_of_songs_used

        print("Song number " + str(number_of_songs_used) + "\n\n")  # Displays song number

        number_of_songs_used += 1

        # ======================================================================================================================
        # This section of code randomly chooses the artist and the song
        randomly_chosen_song = randint(0, len(artists_and_songs) - 1)  # picks a random number

        if randomly_chosen_song % 2 != 0:  # If the number chose is not on an artist
            randomly_chosen_song = randomly_chosen_song - 1  # Put it onto that songs artist

        random_artist = artists_and_songs[randomly_chosen_song]  # Gets the artist

        random_song = artists_and_songs[randomly_chosen_song + 1]  # Gets the song

        random_song_split = random_song.split()  # split at whitespaces into separate words

        random_song_to_display = " ".join((word[0] + "*" * (len(word) - 1) for word in random_song_split))
        # take the first character, fill up with * till length matches for each word we just split.
        # put together with spaces and store it in, "random_song_to_display"

        artists_and_songs.pop(randomly_chosen_song + 1)  # Gets rid of song so it is not repeated

        artists_and_songs.pop(randomly_chosen_song)  # Gets rid of artist so its not repeated

        print("\n")

        # ======================================================================================================================
        # This section of code deals with point scoring and checking answers

        first_guess = input(random_artist + "   " + random_song_to_display + "\n\n")
        # Displays artist and song showing the first letter and replacing the rest with, "*"

        if first_guess.lower().strip().replace(" ", "") == random_song.lower().strip().replace(" ", ""):
            player_points += 3

            print("\n\n+3 Points!\n\n")

        else:
            second_guess = input("\nTry again!\n\n")

            if second_guess.lower().strip().replace(" ", "") == random_song.lower().strip().replace(" ", ""):
                player_points += 1

                print("\n\n+1 Point!\n\n")

            else:
                print("\n\nYou ran out of tries!\n\n")

                if player_points == 1:
                    print("You scored " + str(player_points) + " point!\n\n")

                else:
                    print("You scored " + str(player_points) + " points!\n\n")

                print("Top High Scores\n\n")

                record_score()

                get_scores()

                print_scores()

                break


    if len(artists_and_songs) == 0:
        print("\n\nYou got all of the songs correct!\n\n")

        if player_points == 1:
            print("You scored " + str(player_points) + " point!\n\n")

        else:
            print("You scored " + str(player_points) + " points!\n\n")

        print("Top High Scores\n\n")

        record_score()

        get_scores()

        print_scores()

        return


        print("\n")

# ======================================================================================================================
# ======================================================================================================================
