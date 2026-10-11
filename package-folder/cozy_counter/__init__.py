# Cozy Counter
# Package to count cozy and nostalgic words in a text.
# Words determined using LLMs, which actually are good tools for that kind of thing. 
# (Determining word proximities, relationships, embeddings.)
# August, 2026, Nathaniel Poor, natpoor@gmail.com

# Due to how the cleaning is done, it will false positive on words like " co9zy ".
# Assumes otherwise decently formatted text, not poetry or leetspeak.
# Returns the found word list in alphabetical order.
# If you're in an interactive environment you can easily just print the dictionaries, 
# e.g., print_cozy() and print_nostalgic() . 

# Public-facing functions:
# count_cozy(the_text, verbose=False, condense=True)
# count_nostalgic(the_text, verbose=False, condense=True)
# drop_cozy(dropwords) # Drop given list of words from the dictionary.
# drop_nostalgic(dropwords)
# print_cozy()
# print_nostalgic()


# Public Functions

def count_cozy(the_text, verbose=False, condense=True):
	# Verbose will break it all out, non-verbose is just the count and percentage.
	# Verbose is optional, default is no.
	# Condense is if you want to combine cozy/coziness, etc., in the dictionary. 
	# Condense only works in verbose mode, it is ignored if passed in non-verbose mode.

	# Setup
	cozy_count = 0
	the_text = __preprocess(the_text) # Comes back a list of individual words.
	words_in_the_text = len(the_text)

	if not verbose:
		for each_word in the_text:
			if each_word in cozy_words:
				cozy_count += 1

		return_dict = { 'cozywords':  (cozy_count),
						'totalwords': (words_in_the_text),
						'percentage': (cozy_count / words_in_the_text),
						'wordlist':   dict() # used in verbose mode
						}
		return_dict = __sort_dict(return_dict)
		return return_dict

	elif verbose:
		wordlist = dict()
		for each_word in the_text:
			if each_word in cozy_words:
				cozy_count += 1
				if each_word in wordlist: # if each_word is a key in wordlist
					wordlist[each_word] += 1
				else:
					wordlist[each_word] = 1

		return_dict = { 'cozywords':  (cozy_count),
						'totalwords': (words_in_the_text),
						'percentage': (cozy_count / words_in_the_text),
						'wordlist':    wordlist
						}
		if condense:
			return_dict = __condense_cozy(return_dict)
		return_dict = __sort_dict(return_dict)
		return return_dict

	return # Should not actually reach here.


def count_nostalgic(the_text, verbose=False, condense=True):
	# Verbose will break it all out, non-verbose is just the percentage.
	# Verbose is optional, default is no.
	# Condense is if you want to combine nostalgia/nostalgic, etc., in the dictionary. 
	# Condense only works in verbose mode, it is ignored if passed in non-verbose mode.

	# Setup
	nostalgic_count = 0
	the_text = __preprocess(the_text) # Comes back a list of individual words.
	words_in_the_text = len(the_text)

	if not verbose:
		for each_word in the_text:
			if each_word in nostalgic_words:
				nostalgic_count += 1

		return_dict = { 'nostalgicwords': (nostalgic_count),
						'totalwords':     (words_in_the_text),
						'percentage':     (nostalgic_count / words_in_the_text),
						'wordlist':        dict() # used in verbose mode
						}
		return_dict = __sort_dict(return_dict)
		return return_dict

	elif verbose:
		wordlist = dict()
		for each_word in the_text:
			if each_word in nostalgic_words:
				nostalgic_count += 1
				if each_word in wordlist: # if each_word is a key in wordlist
					wordlist[each_word] += 1
				else:
					wordlist[each_word] = 1

		return_dict = { 'nostalgicwords': (nostalgic_count),
						'totalwords':     (words_in_the_text),
						'percentage':     (nostalgic_count / words_in_the_text),
						'wordlist':        wordlist
						}

		if condense:
			return_dict = __condense_nostalgic(return_dict)
		return_dict = __sort_dict(return_dict)
		return return_dict

	return # Should not actually reach here.


def drop_cozy(dropwords):
	global cozy_words # Local / global variable issue.

	if len(dropwords) == 0:
		print("No dropwords provided.")
	else:
		for word in dropwords:
			word = word.lower()
			if word in cozy_words:
				cozy_words.remove(word)
				print("Removed", word, "from cozy_words list.")
			else:
				print("Error,", word, "is not in cozy_words.")
				chosen = False
				while not chosen:
					the_choice = input("Continue process? Y/N:")
					chosen = True
					if (the_choice == 'Y' or the_choice == 'y'):
						print("Continuing.")
					elif (the_choice == 'N' or the_choice == 'n'):
						print("Ending process.")
						return
					else:
						choice_count += 1
						print("Not valid input, Y/y or N/n:")
						chosen = False
						if choice_count == 3:
							print("Too many invalid inputs, ending process.")
							return

def drop_nostalgic(dropwords):
	global nostalgic_words # Local / global variable issue.

	if len(dropwords) == 0:
		print("No dropwords provided.")
	else:
		for word in dropwords:
			word = word.lower()
			if word in nostalgic_words:
				nostalgic_words.remove(word)
				print("Removed", word, "from nostalgic_words list.")
			else:
				print("Error,", word, "is not in nostalgic_words.")
				chosen = False
				while not chosen:
					the_choice = input("Continue process? Y/N:")
					chosen = True
					if (the_choice == 'Y' or the_choice == 'y'):
						print("Continuing.")
					elif (the_choice == 'N' or the_choice == 'n'):
						print("Ending process.")
						return
					else:
						choice_count += 1
						print("Not valid input, Y/y or N/n:")
						chosen = False
						if choice_count == 3:
							print("Too many invalid inputs, ending process.")
							return

def print_cozy():
	print(cozy_words)

def print_nostalgic():
	print(nostalgic_words)


# The Dictionaries, Cozy Words and Nostalgic Words

# Cozy - had to remove the word 'still' as it is used too often in other contexts in my initial tests.
cozy_words = [	"cozy", "coziness", # In alphabetical order except for the concept words which are first.
				"amber", 
				"autumnal", 
				"belong", "belonging", "belongs",
				"bundled",
				"calm", 
				"candlelit",
				"cocooned", 
				"comfort", "comforts", "comfortable", "comforting", 
				"content", "contentment",	# May cause problems due to "game content".
				"cushioned",
				"daydream", "daydreams", "daydreaming",
				"dreamy", 
				"dusky", 
				"familiar", "familiarity",
				"festive", 
				"fireside", "firelit", "fireplace", 
				"flickers", "flickering",
				"fuzzy", 
				"glimmers", "glimmering", 
				"glows", "glowing",
				"golden", 
				"grounded", 
				"haven", "havens", 
				"hearth", 
				"heartwarming",
				"home",
				"hushed", 
				"hygge", 
				"innocence", "innocent",
				"intimate", 
				"languid", 
				"leafy", 
				"linger", "lingers", "lingering", 
				"misty", 
				"nestled",
				"nook", # Will cause problem if you are studying Animal Crossing.
				"peace", "peaceful", 
				"quiet",
				"refuge", 
				"relax", "relaxing", "relaxed", "relaxes",
				"rest", "restful", 
				"rustic", 
				"safe", "safety", 
				"sanctuary", 
				"security", "secure",
				"serene", "serenity", 
				"settled", 
				"shelter", "sheltered",
				"simplicity", "simple", 
				"snug", 
				"soft", 
				"solace",
				"toasty", 
				"tradition", "traditional", "traditions",
				"tranquil", "tranquility", 
				"unhurried", 
				"velvety", 
				"warm", "warmth",
				"wrapped"
				]

# Nostalgia
nostalgic_words = [ "nostalgia", "nostalgic", # In alphabetical order except for the concept words which are first.
					"affection",
					"antiquity",
					"atavistic",
					"bittersweet", "bittersweetness",
					"bygone",
					"childhood",
					"classic",
					"evocative",
					"flashback",
					"fondness",
					"halcyon",
					"heyday",
					"homesick", "homesickness",
					"keepsake", "keepsakes",
					"longing",
					"melancholy",
					"memento", "mementos",
					"memory", "memories",
					"old-fashioned",
					"poignant", "poignancy ",
					"recollection", "recollections",
					"reflection",
					"reminisce", "reminiscent", "reminiscence",
					"retrospect", "retrospection",
					"reverie",
					"sentimental", "sentimentality",
					"tender", "tenderness",
					"timeless",
					"tradition", "traditions",
					"vintage",
					"wistful", "wistfulness", 
					"yearning", "yearnings", 
					"yesterday", "yesteryear",
					"yore"
					]


# Private Functions

def __preprocess(the_text):
	# Changes the text to all lower-case for ease of analysis, removes non-letters, returns a list of words.
	# Assumes rather boring text in a basic format, not poetry or leetspeak. 
	# Will false-positive on words like " co9zy " which will turn into " cozy ".
	new_text_words = list()

	lower_text = the_text.lower()

	the_words = the_text.split(' ')
	for each_word in the_words:
		cleaned_word = ''.join(char for char in each_word if char.isalpha()) # Keeps letters only.
		new_text_words.append(cleaned_word)

	return new_text_words # Returns list of words.


def __sort_dict(the_dict):
	# Makes the dict (by key) in alphabetical order, not in the order words were encountered in the input text.
	# Not the top-level keys, but the keys in wordlist, a sub-dict. Important!
	# General code idea from: https://www.geeksforgeeks.org/python/python-rearrange-dictionary-for-consective-value-keys/
	# See also: https://realpython.com/sort-python-dictionary/
	sorted_keys = sorted(the_dict["wordlist"].keys())
	matched_values = [the_dict["wordlist"][k] for k in sorted_keys] # Keep values associated with correct keys, in the right order. 
	sorted_wordlist = dict(zip(sorted_keys, matched_values))
	the_dict["wordlist"] = sorted_wordlist
	return the_dict




# Dictionary Condensing Functions

def __condense_cozy(return_dict):

	if ("cozy" in return_dict["wordlist"]) or ("coziness" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("cozy", 0) # Deletes key /returns value if exists, returns 0 if not.
		b = return_dict["wordlist"].pop("coziness", 0)
		return_dict["wordlist"]["cozy/ness"] = a + b

	# "belong", "belonging", "belongs",
	if ("belong" in return_dict["wordlist"]) or ("belonging" in return_dict["wordlist"]) or ("belongs" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("belong", 0)
		b = return_dict["wordlist"].pop("belonging", 0)
		c = return_dict["wordlist"].pop("belongs", 0)
		return_dict["wordlist"]["belong/s/ing"] = a + b + c

	# "comfort", "comforts", "comfortable", "comforting", 
	if ("comfort" in return_dict["wordlist"]) or ("comfortable" in return_dict["wordlist"]) or ("comforts" in return_dict["wordlist"]) or ("comforting" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("comfort", 0)
		b = return_dict["wordlist"].pop("comfortable", 0)
		c = return_dict["wordlist"].pop("comforts", 0)
		d = return_dict["wordlist"].pop("comforting", 0)
		return_dict["wordlist"]["comfort/s/able/ing"] = a + b + c + d

	# "content", "contentment",
	if ("content" in return_dict["wordlist"]) or ("contentment" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("content", 0) 
		b = return_dict["wordlist"].pop("contentment", 0)
		return_dict["wordlist"]["content/ment"] = a + b

	# "daydream", "daydreaming","daydreams"
	if ("daydream" in return_dict["wordlist"]) or ("daydreaming" in return_dict["wordlist"]) or ("daydreams" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("daydream", 0) 
		b = return_dict["wordlist"].pop("daydreaming", 0)
		c = return_dict["wordlist"].pop("daydreams", 0)
		return_dict["wordlist"]["daydream/s/ing"] = a + b + c

	# "familiar", "familiarity",
	if ("familiar" in return_dict["wordlist"]) or ("familiarity" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("familiar", 0) 
		b = return_dict["wordlist"].pop("familiarity", 0)
		return_dict["wordlist"]["familiar/ity"] = a + b

	# "fireside", "firelit", "fireplace", 
	if ("fireside" in return_dict["wordlist"]) or ("firelit" in return_dict["wordlist"]) or ("fireplace" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("fireside", 0)
		b = return_dict["wordlist"].pop("firelit", 0)
		c = return_dict["wordlist"].pop("fireplace", 0)
		return_dict["wordlist"]["fire/side/place/lit"] = a + b + c

	# "flickers", "flickering",
	if ("flickers" in return_dict["wordlist"]) or ("flickering" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("flickers", 0)
		b = return_dict["wordlist"].pop("flickering", 0)
		return_dict["wordlist"]["flickers/ing"] = a + b

	# "glimmers", "glimmering", 
	if ("glimmers" in return_dict["wordlist"]) or ("glimmering" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("glimmers", 0)
		b = return_dict["wordlist"].pop("glimmering", 0)
		return_dict["wordlist"]["glimmers/ing"] = a + b
	
	# "glows", "glowing",
	if ("glows" in return_dict["wordlist"]) or ("glowing" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("glows", 0)
		b = return_dict["wordlist"].pop("glowing", 0)
		return_dict["wordlist"]["glows/ing"] = a + b

	# "haven", "havens", 
	if ("haven" in return_dict["wordlist"]) or ("havens" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("haven", 0)
		b = return_dict["wordlist"].pop("havens", 0)
		return_dict["wordlist"]["haven/s"] = a + b

	# "innocence", "innocent",
	if ("innocence" in return_dict["wordlist"]) or ("innocent" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("innocence", 0)
		b = return_dict["wordlist"].pop("innocent", 0)
		return_dict["wordlist"]["innocent/ce"] = a + b

	# "linger", "lingering", "lingers"
	if ("linger" in return_dict["wordlist"]) or ("lingers" in return_dict["wordlist"]) or ("lingering" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("linger", 0)
		b = return_dict["wordlist"].pop("lingers", 0)
		c = return_dict["wordlist"].pop("lingering", 0)
		return_dict["wordlist"]["linger/s/ing"] = a + b + c

	# "peace", "peaceful", 
	if ("peace" in return_dict["wordlist"]) or ("peaceful" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("peace", 0)
		b = return_dict["wordlist"].pop("peaceful", 0)
		return_dict["wordlist"]["peace/ful"] = a + b

	# "relax", "relaxing", "relaxed", "relaxes"
	if ("relax" in return_dict["wordlist"]) or ("relaxing" in return_dict["wordlist"]) or ("relaxed" in return_dict["wordlist"]) or ("relaxes" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("relax", 0)
		b = return_dict["wordlist"].pop("relaxing", 0)
		c = return_dict["wordlist"].pop("relaxed", 0)
		d = return_dict["wordlist"].pop("relaxes", 0)
		return_dict["wordlist"]["relax/ed/es/ing"] = a + b + c + d

	# "rest", "restful", 
	if ("rest" in return_dict["wordlist"]) or ("restful" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("rest", 0)
		b = return_dict["wordlist"].pop("restful", 0)
		return_dict["wordlist"]["rest/ful"] = a + b

	# "safe", "safety", 
	if ("safe" in return_dict["wordlist"]) or ("safety" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("safe", 0)
		b = return_dict["wordlist"].pop("safety", 0)
		return_dict["wordlist"]["safe/ty"] = a + b

	# "security", "secure",
	if ("security" in return_dict["wordlist"]) or ("secure" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("security", 0)
		b = return_dict["wordlist"].pop("secure", 0)
		return_dict["wordlist"]["secure/ity"] = a + b

	# "serene", "serenity", 
	if ("serene" in return_dict["wordlist"]) or ("serenity" in return_dict["wordlist"]): # firefly
		a = return_dict["wordlist"].pop("serene", 0)
		b = return_dict["wordlist"].pop("serenity", 0)
		return_dict["wordlist"]["serene/ity"] = a + b

	# "shelter", "sheltered",
	if ("shelter" in return_dict["wordlist"]) or ("sheltered" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("shelter", 0)
		b = return_dict["wordlist"].pop("sheltered", 0)
		return_dict["wordlist"]["shelter/ed"] = a + b

	# "simplicity", "simple", 
	if ("simplicity" in return_dict["wordlist"]) or ("simple" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("simplicity", 0)
		b = return_dict["wordlist"].pop("simple", 0)
		return_dict["wordlist"]["simple/icity"] = a + b

	# "tradition", "traditional", "traditions",
	if ("tradition" in return_dict["wordlist"]) or ("traditional" in return_dict["wordlist"]) or ("traditions" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("tradition", 0)
		b = return_dict["wordlist"].pop("traditional", 0)
		c = return_dict["wordlist"].pop("traditions", 0)
		return_dict["wordlist"]["tradition/s/al"] = a + b + c

	# "tranquil", "tranquility", 
	if ("tranquil" in return_dict["wordlist"]) or ("tranquility" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("tranquil", 0)
		b = return_dict["wordlist"].pop("tranquility", 0)
		return_dict["wordlist"]["tranquil/ity"] = a + b

	# "warm", "warmth",
	if ("warm" in return_dict["wordlist"]) or ("warmth" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("warm", 0)
		b = return_dict["wordlist"].pop("warmth", 0)
		return_dict["wordlist"]["warm/th"] = a + b

	return return_dict


def __condense_nostalgic(return_dict): # Because it is the one that is returned.

	if ("nostalgia" in return_dict["wordlist"]) or ("nostalgic" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("nostalgia", 0) # Deletes key /returns value if exists, returns 0 if not.
		b = return_dict["wordlist"].pop("nostalgic", 0)
		return_dict["wordlist"]["nostalgia/ic"] = a + b

	if ("bittersweet" in return_dict["wordlist"]) or ("bittersweetness" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("bittersweet", 0)
		b = return_dict["wordlist"].pop("bittersweetness", 0)
		return_dict["wordlist"]["bittersweet/ness"] = a + b

	if ("homesick" in return_dict["wordlist"]) or ("homesickness" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("homesick", 0)
		b = return_dict["wordlist"].pop("homesickness", 0)
		return_dict["wordlist"]["homesick/ness"] = a + b

	if ("keepsake" in return_dict["wordlist"]) or ("keepsakes" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("keepsake", 0)
		b = return_dict["wordlist"].pop("keepsakes", 0)
		return_dict["wordlist"]["keepsake/s"] = a + b

	if ("memento" in return_dict["wordlist"]) or ("mementos" in return_dict["wordlist"]): # freshmaker
		a = return_dict["wordlist"].pop("memento", 0) 
		b = return_dict["wordlist"].pop("mementos", 0)
		return_dict["wordlist"]["memento/s"] = a + b

	if ("memory" in return_dict["wordlist"]) or ("memories" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("memory", 0) 
		b = return_dict["wordlist"].pop("memories", 0)
		return_dict["wordlist"]["memory/ies"] = a + b

	if ("poignant" in return_dict["wordlist"]) or ("poignancy" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("poignant", 0) 
		b = return_dict["wordlist"].pop("poignancy", 0)
		return_dict["wordlist"]["poignant/cies"] = a + b

	if ("recollection" in return_dict["wordlist"]) or ("recollections" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("recollection", 0) 
		b = return_dict["wordlist"].pop("recollections", 0)
		return_dict["wordlist"]["recollection/s"] = a + b

	if ("reminisce" in return_dict["wordlist"]) or ("reminiscent" in return_dict["wordlist"]) or ("reminiscence" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("reminisce", 0) 
		b = return_dict["wordlist"].pop("reminiscent", 0)
		c = return_dict["wordlist"].pop("reminiscence", 0)
		return_dict["wordlist"]["reminisce/ent/ence"] = a + b + c

	if ("retrospect" in return_dict["wordlist"]) or ("retrospection" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("retrospect", 0) 
		b = return_dict["wordlist"].pop("retrospection", 0)
		return_dict["wordlist"]["retrospect/ion"] = a + b

	if ("sentimental" in return_dict["wordlist"]) or ("sentimentality" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("sentimental", 0) 
		b = return_dict["wordlist"].pop("sentimentality", 0)
		return_dict["wordlist"]["sentimental/ity"] = a + b

	if ("tender" in return_dict["wordlist"]) or ("tenderness" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("tender", 0) 
		b = return_dict["wordlist"].pop("tenderness", 0)
		return_dict["wordlist"]["tender/ness"] = a + b

	if ("tradition" in return_dict["wordlist"]) or ("traditions" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("tradition", 0) 
		b = return_dict["wordlist"].pop("traditions", 0)
		return_dict["wordlist"]["tradition/s"] = a + b

	if ("wistful" in return_dict["wordlist"]) or ("wistfulness" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("wistful", 0) 
		b = return_dict["wordlist"].pop("wistfulness", 0)
		return_dict["wordlist"]["wistful/ness"] = a + b

	if ("yearning" in return_dict["wordlist"]) or ("yearnings" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("yearning", 0) 
		b = return_dict["wordlist"].pop("yearnings", 0)
		return_dict["wordlist"]["yearning/s"] = a + b

	if ("yesterday" in return_dict["wordlist"]) or ("yesteryear" in return_dict["wordlist"]):
		a = return_dict["wordlist"].pop("yesterday", 0) 
		b = return_dict["wordlist"].pop("yesteryear", 0)
		return_dict["wordlist"]["yesterday/year"] = a + b

	return return_dict



if __name__ == "__main__":
	pass






