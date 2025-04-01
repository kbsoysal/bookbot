from stats import get_word_count, count_characters, sort_character_count
import sys


def get_book_text(bookPath):
    """
    Reads the content of a book file and returns it as a string.
    """
    with open(bookPath, 'r', encoding='utf-8') as f:
        book_text = f.read()
    return book_text


if __name__ == '__main__':

    if len(sys.argv)!= 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    path = sys.argv[1]
    
    #path = 'books/frankenstein.txt'
    book_text = get_book_text(path)
    word_count = get_word_count(book_text)
    #print(f'{word_count} words found in the document.')
    character_count = count_characters(book_text)
    sorted_characters = sort_character_count(character_count)
    #print(f'{sorted_characters}')

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for char in sorted_characters:
        print(f'{char[0]}: {char[1]}')
    print('============= END ===============')