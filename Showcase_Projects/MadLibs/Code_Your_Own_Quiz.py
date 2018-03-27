# Below are the Variables for the Song, Song String and Replaceable Words of the Song String.
song_name1 = "Yesterday by The Beatles"

input_string_1 = "___1___ all my troubles seemed so far away. Now it looks as though they're here to ___2___ .  Oh, I believe in yesterday.  Suddenly I'm not half the man I used to be.  There's a ___3___ hanging over me. Oh, yesterday came suddenly.  Why she had to go, I don't know, she wouldn't say.  I said something ___4___, now I long for yesterday."

replace_words_1 = ["Yesterday", "stay", "shadow", "wrong"]

song_name2 = "What Does the Fox Say by Ylvis"

input_string_2 = "Dog goes ___1___ . Cat ___2___ meow. Bird goes tweet and mouse goes squeek. Cow goes ___3___. Frog goes croak and the elephant goes ___4___ ."

replace_words_2 = ["woof", "goes", "moo", "toot"]

song_name3 = "Fresh Prince of Bel-Air (Theme Song)"

input_string_3 = "Now this is a ___1___ all about how my life got flipped-turned ___2___ down. And I'd like to take a minute. Just sit right there, I'll tell you how I became the ___3___ of a town called Bel-Air. In west Philadelphia born and raised. On the playground was where I spent most of my days. ___4___ out maxin' relaxin' all cool and all ___5___ some b-ball outside of the school. When a ___6___ of guys who were up to no good, started making trouble in my neighborhood. I got in one little fight and my mom got scared She said, You're movin' with your ___7___ and ___8___ in Bel-Air."

replace_words_3 = ["story", "upside", "prince", "Chilling", "shooting", "couple", "auntie", "uncle"]

#Below is the opening text information for the program.  I isolated this information since some of it only occurs on startup.
print "WELCOME TO LYRIC MASTERS!!! HOW WELL DO YOU KNOW YOUR MUSICAL LYRICS"
print "You have 3 songs to choose from:"
print "Enter '1' for Yesterday by John Lennon"
print "Enter '2' for What Does the Fox Say by Ylvis"
print "Enter '3' for the Fresh Prince of Bellaire Theme Song"
print "Enter '4' to Exit the game"
user_input = raw_input("Enter a value here:")

#Choose a song function.  This is a function that returns the appropriate song information given the user's selection.
def choose_song(input): 
	if input == '1':
		return [song_name1, input_string_1,replace_words_1]
	if input == '2':
		return [song_name2, input_string_2,replace_words_2]
	if input == '3':
		return [song_name3, input_string_3,replace_words_3]
	if input == '4':
		from sys import exit
		exit()
	else:
		return "Not an option."

def Incorrect_Answer_Check(Incorrect_Answer):
	Incorrect_Answer -= 1
	if Incorrect_Answer == 1:
		print "Incorrect.  Try again. You have " + str(Incorrect_Answer) + " attempt left."
	elif Incorrect_Answer == 0:
		print "Incorrect.  You have " + str(Incorrect_Answer) + " attempt left."
	else:
		print "Incorrect.  Try again. You have " + str(Incorrect_Answer) + " attempts left."
	return Incorrect_Answer

def check_game_state(Incorrect_Answer, index_missing_word, Missing_Words_List):
	if Incorrect_Answer == 0: # Special Case: If the player makes 5 incorrect guesses then they lose the game.
		output = "You Lose!"
		print "You Lose!"
		return output
	if index_missing_word == len(Missing_Words_List)+1: #Special Case: If the player answers all questions, they win the game!!! Note that the index_missing_word value is initialized to 1.  Therefore the length of the Missing_Words_List must add a 1 to account for this.
		output = "You Win!"
		print "You Win!"
		return output

def correct_answer(song_lyrics_list):
	print "Correct!"
	print " ".join(song_lyrics_list)

#This is the function that takes in the Song String and replaceable words and asks the user to input the missing words.
def Questions(song_lyrics_list, Missing_Words_List):
	index_missing_word = 1 #This increments through the number of each missing word.
	Incorrect_Answer = 5 # This variable keeps track of the amount of missed questions.
	output = []
	while output != "You Lose!" and output != "You Win!": # The game will stop when either someone has won or lost.
		index_missing_word_location_in_list = 0
		for word in song_lyrics_list:
			output = check_game_state(Incorrect_Answer, index_missing_word, Missing_Words_List)
			if output == "You Lose!" or output == "You Win!":
				break
			else:	
				if str(index_missing_word) in word:
					user_answer = raw_input("What is the missing word for ___" + str(index_missing_word) + "___:")
					if user_answer == Missing_Words_List[index_missing_word-1]: #Since index_missing_word is initialized to 1 we have to subtract one to set the initial index to zero.
						song_lyrics_list[index_missing_word_location_in_list] = song_lyrics_list[index_missing_word_location_in_list].replace(song_lyrics_list[index_missing_word_location_in_list], user_answer) 
						index_missing_word += 1
						correct_answer(song_lyrics_list)
					else:
						Incorrect_Answer = Incorrect_Answer_Check(Incorrect_Answer)							
			index_missing_word_location_in_list += 1

#Function that simply prints text to inquire if the user wants to play again.
def play_again():
	print "Play again?"
	print "You have 3 songs to choose from:"
	print "Enter '1' for Yesterday by John Lennon"
	print "Enter '2' for What Does the Fox Say by Ylvis"
	print "Enter '3' for the Fresh Prince of Bellaire Theme Song"
	print "Enter '4' to Exit the game"
	user_input = raw_input("Enter a value here:")
	return user_input

"""This is the main function that takes in the initial user_input to determine what game they want to play.  
It will call the Choos_song function to import the appropriate song information and then call the Questions 
function to play the game.  Once the game ends, this function will prompt the user if they want to play again 
and present them with the three song options or to quit by typing in '4'."""
def play_game(user_input):
	while user_input != '4':
		if user_input == '1' or user_input == '2' or user_input == '3':
			choose_song_output = choose_song(user_input)
			song_name = choose_song_output[0]
			print song_name
			song_lyrics_string = choose_song_output[1]
			song_lyrics_list = song_lyrics_string.split()
			Missing_Words_List = choose_song_output[2]
			print " ".join(song_lyrics_list)
			Questions(song_lyrics_list, Missing_Words_List)
			user_input = play_again()
		else:
			print "Not an acceptable input."
			user_input = raw_input("Enter a value here:")
	return "Thanks for playing!"	
	

print play_game(user_input)