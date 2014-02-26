import sys
import os
import time

timing = 666 #wpm
sleep_time = (1/(timing/60.0))-.01
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
punctuation = ["\"","\'",".",";",":"]
vowels = ["a","e","i","o","u","y"]
spacing = 15

if len(sys.argv) > 1:
	print("reading file " + str(sys.argv[1]))
	text = '\n'.join(open(sys.argv[1],'r').readlines())
else:
	print("No File, reading from sample")
	text = """Reading is inherently time consuming because your eyes have to move from word to word and line to line. 
	Traditional reading also consumes huge amounts of physical space on a page or screen, 
	which limits reading effectiveness on small displays. Scrolling, pinching, and resizing 
	a reading area doesn’t fix the problem and only frustrates people. Now, with compact text 
	streaming from Spritz, content can be streamed one word at a time, without forcing your 
	eyes to spend time moving around the page. Spritz makes streaming your content easy and 
	more comfortable, especially on small displays. Our “Redicle” technology enhances 
	readability even more by using horizontal lines and hash marks to direct your eyes 
	to the red letter in each word, so you can focus on the content that interests you. 
	Best of all, Spritz’s patent-pending technology can integrate into photos, maps, videos, 
	and websites to promote more effective communication."""

def get_word_correction(word,correction_type="last_vowel_first_syllable"):
	if word == "":
		return ""
	if correction_type == "last_vowel_first_syllable":
		x = 0
		while x < len(word):
			if word[x].lower() not in consonants+punctuation:
				break
			x += 1
		while x < len(word):
			if word[x].lower() not in vowels+punctuation:
				break
			x += 1
		#x is the location of the last vowel in the first syllable
		x -= 1
		new_string = " "*(spacing-x) + word[:x] + "\033[1;31m" + word[x] + "\033[0m" + word[x+1:]
		return  new_string
	if correction_type == "last_consonant_first_syllable":
		x = 0
		while x < len(word):
			if word[x].lower() not in consonants+punctuation:
				break
			x += 1
		while x < len(word):
			if word[x].lower() not in vowels+punctuation:
				break
			x += 1
		while x < len(word):
			if word[x].lower() not in consonants+punctuation:
				break
			x += 1
		#x is the location of the last vowel in the first syllable
		if x == len(word):
			x = len(word)//2
		else:
			x -= 1
		new_string = " "*(spacing-x) + word[:x] + "\033[1;31m" + word[x] + "\033[0m" + word[(x+1):]
		return  new_string

def format_for_spritzing(t):
	lines = t.replace("\t",'').replace("-",'').replace(".","\n").split("\n")
	for line in range(len(lines)):
		lines[line] = lines[line].replace("\n",'').split(" ")
	return lines

if __name__ == "__main__":
	os.system("clear")
	print("\n")
	print(get_word_correction("ready?",correction_type="last_consonant_first_syllable"))
	for a in format_for_spritzing(text):
		time.sleep(.5)
		for b in a:
			time.sleep(sleep_time)
			os.system("clear")
			print("\n")
			print(get_word_correction(b),correction_type="last_consonant_first_syllable"))
