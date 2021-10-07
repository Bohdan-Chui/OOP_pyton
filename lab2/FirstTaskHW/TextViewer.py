class TextViewer:

    def __init__(self,file = ' ', charecters = 0, words = 0, sentences = 0):
        self.__file = file
        self.__charecters = charecters;
        self.__words = words
        self.__sentences = sentences

    def count_words(self):
        with open(self.__file) as f:
            count = len(f.read().split())
        return count

    def count_charecters(self):
        with open(self.__file) as f:
            return len(f.read())

    def count_sentences(self):
        with open(self.__file) as file:
            return (file.read().count('.'))

if __name__ == '__main__':
    viewer = TextViewer("text.txt")
    print("sentences", viewer.count_sentences())
    print("words", viewer.count_words())
    print("charecters", viewer.count_charecters())

