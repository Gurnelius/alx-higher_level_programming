#!usr/bin/python3
'''
    This module prints text with idetation.
'''


def text_indentation(text):
    '''
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Parameters:
        - text (str): The input text.

    Raises:
        - TypeError: If `text` is not a string.

    Example:
    >>> text_indentation("This is a sentence. Another sentence?")
    This is a sentence.
    Another sentence?
    '''

    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    sentence = ""
    sentences = ""
    # Iterate through each character in the text
    for char in text:
        if char not in ('.', '?', ':'):
            sentence += char
        elif char in ('.', '?', ':'):
            sentence = sentence.strip()
            sentence += char+'\n\n'
            sentences += sentence
            sentence = ""
    if sentences == "":
        sentences += sentence
    text = sentences.strip('\n')
    print(text, end='')
