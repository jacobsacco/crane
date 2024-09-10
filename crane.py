
class Word(str):
    pass

class Wordle:
    def __init__(self, input_file):
        with open('5letters.txt') as infile:
            self.words = input_file.readlines()
            self.words = [Word(word.strip()) for word in self.words]

        for i, word in enumerate(self.words):
            word.rank = i
            word.shares_letters_with = 0
            word.set = set(word)

        for i, word in enumerate(self.words[:-1]):
            for other in self.words[i+1:]:
                if word.set & other.set:
                    word.shares_letters_with += 1
                    other.shares_letters_with += 1

        for word in self.words:
            word.score = word.shares_letters_with + 100*(1 - word.rank/len(words))

        self.words.sort(key=lambda word: -word.score)

    def guess(self):
        self.most_recent_guess = self.words[0]
        return self.most_recent_guess

    


#print(words[:10], sep="\n")
for word in words[:5]:
    print(f"{word} | {word.rank: 5} | {word.shares_letters_with}")
