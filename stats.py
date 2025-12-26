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

def sorting(dictionary):
    return dictionary["num"]

def sorted_chars(num_chars):
    dictionary_list = []
    for k,v in num_chars.items():
        new_kv_pair = {"char" : "", "num" : ""}
        new_kv_pair["char"] = k
        new_kv_pair["num"] = v
        dictionary_list.append(new_kv_pair)
    dictionary_list.sort(reverse=True, key=sorting)
    return dictionary_list

