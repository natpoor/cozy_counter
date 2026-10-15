Library to count both cozy words and nostalgic words in a text.
Good for content analysis (counting) of such concepts.
Python 3.


Functions:
  count_cozy(the_text, verbose=False, condense=True)
  count_nostalgic(the_text, verbose=False, condense=True)
  drop_cozy(dropwords) # Pass a list
  drop_nostalgic(dropwords)
  print_cozy()
  print_nostalgic()

The main functions take a text string object as input, clean it up, and return a dictionary object with the following structure:
	return_dict = { 'cozywords':  (cozy_count), # Count of cozy words.
					'totalwords': (words_in_the_text), # Total words in the text.
					'percentage': (cozy_count / words_in_the_text), # Percentage of cozy words.
					'wordlist':   dict() # Has non-zero cozy words as keys, counts as their values.
					}

count_nostalgic is similar but with "nostalgicwords" as the first key, and it uses the nostalic dictionary.

You can do...
from cozy_counter import count_cozy
from cozy_counter import count_nostalgic

Or...
import cozy_counter as cc

And then call the functions like so:
cc.count_cozy(the_text)
cc.count_nostalgic(the_text)

Arguments:
Verbose, if True, expands to have all the words in the dictionary broken out in the results (the wordlist).
Condense goes along with Verbose and essentially tokenizes the relevant words, so e.g. "cozy" and "coziness" are counted as the same item when Condense is True.
Dropwords is a list you can pass for words to drop from the analysis for that one run, so perhaps you are analyzing Animal Crossing posts on Reddit and "Nook" refers to the character, not a cozy nook, so you can pass a list of the words to not include.

Both dictionaries are in the file (so you can adjust as you see fit).
Dictionaries were created using LLMs, as they use word embeddings so asking them what words
are associated with each term is actually something they can do accurately. 
You can print them with print_cozy() and print_nostalgic().

drop_words:
	I made these their own functions as calling them as a keyword argument in the main call,
	in a loop, did not work, as it tried to remove the word each loop and so threw an error.
	These are useful for words that are used in a non-cozy or nostalgic way, which happens. 
	Pass them a list of the words you want to drop. 
	You don't have to use drop_words(), you could do it on your own end pretty easily. 
	This may be a bit of feature creep!

A note on the words in and not in the dictionaries:
Cozy words:
	The word "still" was highly over-represented in the results in the tests I ran, I believe people
	use the word "still" in the non-cozy manner more than they do in the cozy manner, so I dropped "still" from the dictionary.
	"Content" (like contentment, "I feel content") was also a problem with game-related text, as in "new content is available for 
	the game," but it is still in the dictionary. 
	The word "home" may also cause trouble depending on your context. 
	If you are studying the game Animal Crossing: New Horizons, the word "nook" is a problem as it is a character in the game,
	as are some other words perhaps (content, home, rest, simple).

Nostalgic words:
	The words "yesterday" (yesterday/yesteryear) and "memory" (memory/memories) were over-represented
	in the test I ran, but not a huge amount, so I left them in the dictionaries but beware your results with these two words.

It's a good idea as always to get to know your data and see if words are over-represented and are maybe being used in non-cozy/nostalgic contexts.


Initial work, July 2026.
Nathaniel Poor, natpoor@gmail.com
