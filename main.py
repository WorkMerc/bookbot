def get_book_text():
    #print("Hello! And welcome to bookbot, the automated system for counting the words and letters in a book!")
    #print("Please enter the relative file path to the book you would like to parse:")
    book_title = "./books/frankenstein.txt"
    with open(book_title) as book:
        return print(book.read())
    
get_book_text()