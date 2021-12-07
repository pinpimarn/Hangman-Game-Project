class VocabContainer:
    def __init__(self, container=[]):
        self.container = container

    def add_word(self, vocab):
        """collect the vocabulary words in a list"""
        self.container.append(vocab)
