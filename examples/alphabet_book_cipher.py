from book_cipher import BookCipher
import string


class AlphabetBookCipher(BookCipher):
    """
    Very basic BookCipher subclass that uses a given
    number of copies of the upper and lowercase alphabet.
    """
    def __init__(self, alphabet_count=1):
        super().__init__()
        self.alphabet_count = alphabet_count

    @property
    def book_str(self):
        return (string.ascii_letters + " ") * self.alphabet_count


if __name__ == '__main__':
    # try larger alphabet_count to see how the cipher will
    # attempt to avoid repeating the same number for letters
    # that are repeated in the clear text.
    alphabet_book_cipher = AlphabetBookCipher(alphabet_count=1)
    cipher_text = alphabet_book_cipher.encrypt("Hello world")
    print(cipher_text)
    clear_text = alphabet_book_cipher.decrypt(cipher_text)
    print(clear_text)
