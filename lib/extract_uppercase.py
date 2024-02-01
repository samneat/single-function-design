def extract_uppercase(text):
    words = text.split()
    uppercase_words = [word for word in words if word.isupper()]
    filtered_uppercase_words = []
    for word in uppercase_words:
        filtered_letters = [letter for letter in word if letter.isalpha()]
        filtered_word = "".join(filtered_letters)
        filtered_uppercase_words.append(filtered_word)
    return filtered_uppercase_words
