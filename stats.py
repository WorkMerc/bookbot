#This function splits the words from get_book_text into a list and counts the words that were returned
def word_split(text):
    word_list = text.split()
    return word_list

def word_count(word_list):
    total_words = len(word_list)
    return total_words

def char_count(text):
    characters = {}
    string_text = str(text)
    for character in string_text.lower():
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters
