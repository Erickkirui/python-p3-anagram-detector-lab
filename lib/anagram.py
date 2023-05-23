# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        result = []
        for word in word_list:
            if self.is_anagram(word):
                result.append(word)
        return result

    def is_anagram(self, word):
        return sorted(self.word.lower()) == sorted(word.lower())
