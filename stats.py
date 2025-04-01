def get_word_count(book_text):
    """
    Counts the number of words in the book text.
    """
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    """
    Returns a dictionary of characters and their frequencies in the book.
    """
    character_count = {}
    for char in book_text:
        if char.isalpha():
            char = char.lower()
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

def sort_character_count(character_count):
    """
    Sorts the character count dictionary by frequency in descending order.
    """
    sorted_characters = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_characters