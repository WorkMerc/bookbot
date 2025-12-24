from stats import word_count
 
#This function opens the .txt file that is needed for the count function
def get_book_text(path):
    with open(path) as book:
        return book.read()

#This is the main function that brings all the pieces of the bookbot program together
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f'Found {num_words} total words')

main()
