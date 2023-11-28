def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    # iterate through the phrase
    # if the character in phrase matches the to_swap
    # we will change character to the opposite case using method swapcase()
    new_swap_phrase = ""
    for char in phrase :
        if char.lower() == to_swap.lower() :
            new_swap_phrase += char.swapcase()
        else :
            new_swap_phrase += char

    return new_swap_phrase