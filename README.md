# OCR-GCSE-Programming-Project-Task-1-for-practise-
https://www.ocr.org.uk/Images/503195-programming-project-tasks-june-2019-and-june-2020.pdf

The point of this project is to practise my basic python skills with a task from the OCR computer science programming projects from June 2019 to 2020.

## Table of Contents



## Task

Noel is creating a music quiz game.

The game stores a list of song names and their artist
(e.g. the band or solo artist name). The player needs to
try and guess the song name.

The game is played as follows:

•   A random song name and artist are chosen.  
•   The artist and the first letter of each word in the song title are displayed.  
•   The user has two chances to guess the name of the song.  
•   If the user guesses the answer correctly the first time, they score 3 points. If the user guesses
the answer correctly the second time they score 1 point. The game repeats.  
•   The game ends when a player guesses the song name incorrectly the second time.  

Only authorised players are allowed to play the game.
Where appropriate, input from the user should be validated.

Design, develop, test and evaluate a system (using python and no external modules) that:

1. Allows a player to enter their details, which are then authenticated to ensure that they are an
authorised player.
2. Stores a list of song names and artists in an external file.
3. Randomly selects a song from the file, displaying the artist and the first letter of each word of the song title.
4. Allows the user up to two chances to guess the name of the song, stopping the game if they guess
a song incorrectly on the second chance.
5. If the guess is correct, add the points to the player’s score depending on the number of guesses.
6. Displays the number of points the player has when the game ends.
7. Stores the name of the player and their score in an external file.
8. Displays the score and player name of the top 5 winning scores from the external file.

## Version 1

### Why?

The purpose of version 1 is to create an easier to read project meant for reading and understanding. It can still run but it will be limited with functionality and will only serve the purpose of the task and nothing beyond it to make it more user-friendly. It is split into multiple python files to make the code easier to read.

### Installation

This works for Mac, Linux and Windows and anybody can run it, nothing extra is necessary for installation. However, there are two ways to run this program. You can choose to use python to run it in the command line or you can run the .exe file, which is slower than using python to load up but performance within program is not noticable.

#### METHOD 1: Using Python in the Command Line

This method is requires that python 3 is installed on your system. This method is a little longer to run the program but significantly faster than the other method.

**1.** Make sure that python is installed on your operating system and your python directory is in your PATH

**2.** Download this repository onto your system

**3.** Open the command line and change its directory into the, "Version 1 (Limited, Multiple Files)" folder within this repository

**4.** Type "python3 Main_Script.py"

You have successfully run the Python Version 1 files on your system!

#### Method 2: Running the Executable

This method does not require you have anything pre-installed on your system. It is significantly slower than the other method in terms of start up time, which requires that you wait a few seconds for it to run, but performance within the program is almost identical to METHOD 1.

**1.** Download this repository onto your system

**2.** Open your file explorer, locate it and open the, "Version 1 (Limited, Executable)" folder within the repository

**3.** Right-click the .exe file and click run

You have successfully run the Version 1 Executable on your system!

### Editing Version 1

Within Version 1 you can edit the code as well as some other variables stored in the .txt files. This includes: Users, the Song List and scores.

#### Editing Users

If you want to edit the users you can run the program and create an account, edit account username and password and delete your account. Nevertheless, you can still manually change this with, "Users.txt". Here's how you do it:

##### Making a New Account Manually

**1.** Open, "Users.txt" with your text editor of choice

**2.** Make a new line and put your desired Username on it. This line should be an odd numbered line if you start counting from the first line counting from 1

**3.** Make a new line and put your desired Password on it. This line should be an even numbered line if you start counting from the first line counting from 1

That's it, you have created a new account!

##### Editing an Existing Account Manually

**1.** Open, "Users.txt" with your text editor of choice

**2.** Find your already existing account and you will be able to see your Username and Password. Change them to whatever you desire.

That's it, you have edited an already existing account

##### Deleting your Account Manually

**1.** Open, "Users.txt" with your text editor of choice

**2.** Find your account Username and Password and delete both the Username and Password as well as the lines that they are on.

That's it, you have deleted your account!

#### Editing the Song List

If you want to edit the Song List you can do so within the program just go into the, "Settings" menu and go into the Song List menu to add, modify and delete songs. Nonetheless, you can manually change the Song List that you play through by editing, "Song_List.txt". Here's how you do it:

##### Adding a Song Manually

**1.** Open, "Song_List.txt" with your text editor of choice

**2.** Make a new line and include the Artists name of the song of your choice. This line should be an odd numbered line if you start counting from the first line counting from 1.

**3.** Make a new line and include the Song of choice. This line should be an even numbered line if you start counting from the first line counting from 1

That's it, you have just added a song!

##### Editing an Already Existing Song Manually

**1.** Open, "Song_List.txt" with your text editor of choice

**2.** Find the song you wish to edit

**3.** Change the artists name and the song to whatever you desire

That's it, you have edited a song!

##### Delete a Song Manually

**1.** Open, "Song_List.txt" with your text editor of choice

**2.** Find the song you wish to delete. Delete the Artist and Song as well as the lines they were on

That's it, you have deleted a song!

####  Editing Scores

Within the program you get a score every time you play and can clear all of your scores in the menu but it is limited to that. Despite that, you can manually add, modify and delete scores from, "Scores.txt". Here's how you do it:

##### Adding a Score Manually

**1.** Open, "Scores.txt" with your text editor of choice

**2.** Make a new line and your desired score

That's it, you have added a custom score!

##### Changing an Already Existing Score Manually

**1.** Open, "Scores.txt" with your text editor of choice

**2.** Find the score you want and change its value to whatever you want

That's it, you have changed an already existing score!

##### Delete a Specific Score Manually

**1.** Open, "Scores.txt" with your text editor of choice

**2.** Find the score you wish to delete and delete it as well as the line it was on.

That's it, you have deleted a specific score!

## Comments about code

Sections of code are splitted with double closers:

===============================================================================

===============================================================================

Sections within sections are splitted with one closer:

===============================================================================

This is in order to make reading the code easier and make the sections of sections of code easier to find, modify, read, and understand

One of the things I did with the code is that instead of putting "else:" statements where I could I only put them where they where necessary making "elif:" statements instead to make the code easier to read.

One import was necessary and that was the, "randint" function from the random module built into python. It was absolutely unavoidable
as I had to randomly generate a number to pick a song from the list.

## Bugs

There have been no reported bugs.
