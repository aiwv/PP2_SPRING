def is_pangram(s):
     return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())
s = input()
print(bool(is_pangram(s)))


# set() creates a data structure which can't have any duplicates in it, and here:

# The first set is the (English) alphabet letters, in lowercase
# The second set is the characters from the test string, also in lowercase. And all the duplicates are gone as well.
# Subtracting things like set(..) - set(..) returns the contents of the first set, minus the contents of the second set. set('abcde') - set('ace') == set('bd').

# In this pangram test:

# we take the characters in the test string away from the alphabet
# If there's nothing left, then the test string contained all the letters of the alphabet and must be a pangram.
# If there's something leftover, then the test string did not contain all the alphabet letters, so it must not be a pangram.

# any spaces, punctuation characters from the test string set were never in the alphabet set, so they don't matter.

# set(..) - set(..) will return an empty set, or a set with content. If we force sets into the simplest True/False values in Python, then containers with content are 'True' and empty containers are 'False'.

# So we're using not to check "is there anything leftover?" by forcing the result into a True/False value, depending on whether there's any leftovers or not.

# not also changes True -> False, and False -> True. Which is useful here, because (alphabet used up) -> an empty set which is False, but we want is_pangram to return True in that case. And vice-versa, (alphabet has some leftovers) -> a set of letters which is True, but we want is_pangram to return False for that.

# Then return that True/False result.