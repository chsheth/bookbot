from stats import count_words, count_characters, list_of_dict
import sys

def get_book_text(filepath: str) -> str:
    """
    Retrieves the text of the book.

    Returns:
        str: The text of the book.
    """
    # Implementation goes here
    with open(filepath) as f:
        file_content = f.read()
    return file_content



def main():
    if len(sys.argv) != 2:
        # If the count is incorrect, print the usage message.
        print("Usage: python3 main.py <path_to_book>")
        
        # Exit the program with a status code of 1 (indicating an error).
        sys.exit(1)

    # If the check passes, the file path is the second element (index 1).
    book_file_path = sys.argv[1]

    book_text = get_book_text(book_file_path)
    word_count = count_words(book_text)
    char_dict = count_characters(book_text)

    print("========== BOOKBOT =========")
    print(f"Analyszing book found at {book_file_path}")
    print("------------ Word Count ------------")
    print(f"Found {word_count} total words")
    print("------------ Character Count ------------")
    list_of_dict(char_dict)
    print("================== END =================")

#sys.exit(1)    
#print(sys.argv)

main()