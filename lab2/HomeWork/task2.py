import os.path


class TextViewer:

    def __init__(self,file, charecters = 0, words = 0, sentences = 0):
        self.file = file
        self.charecters = charecters;
        self.words = words
        self.sentences = sentences

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        if not os.path.isfile(file):
            return IOError('file doest exist')
        self.__file = file

    @property
    def charecters(self):
        return self.__charecters

    @charecters.setter
    def charecters(self, charecters):
        self.__charecters = charecters

    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, words):
        self.__words = words

    @property
    def sentences(self):
        return self.__sentences

    @sentences.setter
    def sentences(self, sentences):
        self.__sentences = sentences

    def count_words(self):
        with open(self.__file, "r") as f:
            self.__words = len(f.read().split())

    def count_charecters(self):
        with open(self.__file, "r") as f:
            self.__charecters = len(f.read())

    def count_sentences(self):
        with open(self.__file, "r") as f:
            self.__sentences =  (f.read().count('.'))

    def get_charecters(self):
        return self.__charecters

    def get_words(self):
        return self.__words

    def get_sentences(self):
        return self.__sentences


if __name__ == '__main__':
    viewer = TextViewer("text.txt")
    viewer.count_sentences()
    print("sentences", viewer.get_sentences())
    viewer.count_words()
    print("words", viewer.get_words())
    viewer.count_charecters()
    print("charecters", viewer.get_charecters())

