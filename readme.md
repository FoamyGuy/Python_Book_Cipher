# Python Book Cipher

Easily create your own [book cipher](https://en.wikipedia.org/wiki/Book_cipher) by extending BookCipher class 
and providing a `book_str` property implementation that returns
whatever string you want to use for the carrier text. 

Once instantiated the class can encrypt clear text into a list of numbers
referencing locations in the carrier text, and decrypt the list of numbers
back into clear text. 

Some examples are provided inside the `examples/` directory.