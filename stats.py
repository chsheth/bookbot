def count_words(file_content: str):
    """
    Counts the number of words in the book text.

    Returns:
        int: The number of words in the book text.
    """
    words = file_content.split()
    return len(words)

def count_characters(file_content: str):
    """
    Counts the number of characters in the book text.

    Returns:
        int: The number of characters in the book text.
        
        dictionary: charater -> count.
    """
    char_dict = {}
    words = file_content.split()
    for word in words:
        word=word.lower()
        for i in range(len(word)):
            if word[i] in char_dict:
                char_dict[word[i]] += 1
            else:
                char_dict[word[i]] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def list_of_dict(any_dict: dict):
    l = []
    for key, value in any_dict.items():
        l.append({"char": key, "num":value})
        l.sort(reverse=True, key=sort_on)
        
    for i in l:
        print(f"{i['char']}: {i['num']}")


