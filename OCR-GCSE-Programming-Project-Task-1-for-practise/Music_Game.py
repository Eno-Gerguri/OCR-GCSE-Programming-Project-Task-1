from random import randint

artists_and_songs = []


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

number_of_songs_and_artists = 33
number_of_songs_used = 1

player_points = 0


def start_music_game():
    global number_of_songs_and_artists
    global player_points

    print("Music Game!\n\n")

    while len(artists_and_songs) != 0:
        global number_of_songs_used

        print("Song number " + str(number_of_songs_used) + "\n\n")

        number_of_songs_used += 1

# ======================================================================================================================

        randomly_chosen_song = randint(0, number_of_songs_and_artists)

        if randomly_chosen_song % 2 != 0:
            randomly_chosen_song = randomly_chosen_song - 1

        print(randomly_chosen_song)  # for debugging

        random_artist = artists_and_songs[randomly_chosen_song]

        random_song = artists_and_songs[randomly_chosen_song + 1]

        random_song_split = random_song.split()

        random_song_to_display = " ".join((word[0] + "*" * (len(word) - 1) for word in random_song_split))

        artists_and_songs.pop(randomly_chosen_song + 1)
        artists_and_songs.pop(randomly_chosen_song)

        number_of_songs_and_artists -= 2

        print("\n")


# ======================================================================================================================

        first_guess = input(random_artist + "   " + random_song_to_display + "\n\n")

        if first_guess.lower().strip().replace(" ", "") == random_song.lower().strip().replace(" ", ""):
            player_points += 3
            print("\n\n+3 Points!\n\n")

        else:
            second_guess = input("\nTry again\n\n")

            if second_guess.lower().strip().replace(" ", "") == random_song.lower().strip().replace(" ", ""):
                player_points += 1
                print("\n\n+1 Point!\n\n")

            else:
                print("\n\nYou ran out of tries!\n\n")
                break

        print("\n")

# ======================================================================================================================
# ======================================================================================================================
