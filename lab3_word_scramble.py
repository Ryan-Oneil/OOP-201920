# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3


class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3
        sentence = str(self.user_input).split()

        # Scrambles every word in sentence first
        for i in range(0, len(sentence)):
            sentence[i] = self.scrambleWord(sentence[i])

        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation

        for i in range(0, len(sentence), 2):
            if i < len(sentence) - 1:
                print(i)
                sentence[i], sentence[i+1] = sentence[i+1], sentence[i]

        print (sentence)

    def scrambleWord(self, word):
        wordlist = list(word)
        wordlist[0], wordlist[1] = wordlist[1], wordlist[0]
        wordlist[-1], wordlist[-2] = wordlist[-2], wordlist[-1]
        return "".join(wordlist)


word_scrambler = WordScramble()
word_scrambler.scramble()

