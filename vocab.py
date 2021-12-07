import random
import math


class Vocabulary:
    def __init__(self, filename, vocab, correct):
        self.filename = filename
        self.vocab = vocab
        self.correct = correct

    def random_word(self):
        """ Read the .txt file. """
        text_file = open(self.filename, "r")
        lines = text_file.read().splitlines()
        index_w = random.randint(0, len(lines) - 1)
        self.vocab = lines[index_w]

    def index_clue(self):
        """ Random the clue for the user.

        :return: string, list, int, list
        """
        num_clue = (10/100) * len(self.vocab)
        list_of_index = []
        for i in range(math.ceil(num_clue)):
            index_clue = random.randint(0, len(self.vocab)-1)
            list_of_index.append(index_clue)
        list_of_clue = []
        all_clue_ch = []
        count = 0
        for index in list_of_index:
            all_clue_ch.append(self.vocab[index])
            count += 1
        for i in self.vocab:
            if i not in all_clue_ch:
                list_of_clue.append("_")
            else:
                list_of_clue.append(i)
        word = " "
        for n in list_of_clue:
            word = word + n + " "
        return word, list_of_index, count, all_clue_ch

    def count_correct(self):
        """ Count how many alphabets that user need to fill in to win this game."""
        lst = []
        for i in self.vocab:
            if i not in lst:
                lst.append(i)
            else:
                pass
        self.correct = len(lst)
