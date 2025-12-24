#This function splits the words from get_book_text into a list and counts the words that were returned
def word_count(text):
    words = text.split()
    total_words = len(words)
    return total_words