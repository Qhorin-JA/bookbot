def count_words(text):
    words = text.split()
    return len(words)

def count_character(text):
    lower_text = text.lower()
    lower_text.split()
    dict_of_characters = {}
    for character in lower_text:
        if character not in dict_of_characters:
            dict_of_characters[character] = 1
        else:
            dict_of_characters[character] += 1
    return dict_of_characters

def sort_on(dict):
    return dict["count"]

def sorted_character_numbers(character_dict):
    character_list = []
    for key, value in character_dict.items():
        if key.isalpha():
            character_list.append({"char": key, "count": value})
    character_list.sort(reverse=True, key=sort_on)
    return character_list