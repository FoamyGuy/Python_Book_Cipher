from book_cipher import BookCipher


class TxtBookCipher(BookCipher):
    """
    BookCipher subclass that reads the book from a given
    .txt file, for instance a book downloaded from
    Project Gutenberg.
    """
    def __init__(self, txt_file):
        super().__init__()
        self.txt_file = txt_file

    @property
    def book_str(self):
        with open(self.txt_file, 'r') as f:
            return f.read()


if __name__ == '__main__':

    tbc = TxtBookCipher('test_book.txt')
    cipher_text = tbc.encrypt("Super secret message!")
    print(cipher_text)
    print(tbc.decrypt(cipher_text))