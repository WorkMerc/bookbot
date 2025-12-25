from stats import word_split, word_count, char_count
 
#This function opens the .txt file that is needed for the count function
def get_book_text(path):
    with open(path) as book:
        return book.read()

#This is the main function that brings all the pieces of the bookbot program together
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_list = word_split(text)
    num_words = word_count(word_list)
    num_chars = char_count(word_list)
    print(f'Found {num_words} total words')
    print(f'Found {num_chars} in total of each character')

main()
