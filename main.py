from stats import word_split, word_count, char_count, sorted_chars
 
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
    list_characters = sorted_chars(num_chars)

    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_path}...')
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for line in list_characters:
        if line['char'].isalpha():
            print(f'{line['char']}: {line['num']}')
    print("============= END ===============")

main()
