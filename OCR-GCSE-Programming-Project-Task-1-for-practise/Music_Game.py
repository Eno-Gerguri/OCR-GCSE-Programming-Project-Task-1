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

def start_music_game():
    print("Music Game!\n\n")
