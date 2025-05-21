# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Sort the original word once
        sorted_word = sorted(self.word)

        # Create a list of words that are anagrams of the original word
        return [candidate for candidate in word_list if sorted(candidate) == sorted_word and candidate != self.word]
