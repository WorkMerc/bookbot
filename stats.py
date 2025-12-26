#This function splits the words from get_book_text into a list and counts the words that were returned
def word_split(text):
    word_list = text.split()
    return word_list

#This function counts how many words are in the text
def word_count(word_list):
    total_words = len(word_list)
    return total_words

#This function creates a dictionary of each individual character in the text and a count of how many were found
def char_count(text):
    characters = {}
    string_text = str(text)
    for character in string_text.lower():
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

#This is a helping function that is designed to sort off the "num" dictionary value that will be defined in the sorted characters function
def sorting(dictionary):
    return dictionary["num"]

#This function creates a list of new dictionaries with new key:value pairs. 
#Setting a "char" key with unique characters filtered by previous function as the value 
#then sets a "num" key with integer value
def sorted_chars(num_chars):
    dictionary_list = []
    for k,v in num_chars.items():
        new_kv_pair = {"char" : "", "num" : ""}
        new_kv_pair["char"] = k
        new_kv_pair["num"] = v
        dictionary_list.append(new_kv_pair)
    dictionary_list.sort(reverse=True, key=sorting)
    return dictionary_list

