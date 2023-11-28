def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    # char = list(phrase)
    # # print("char=", char)
    # char.reverse()
    # newStr = ""
    # for letter in char:
    #     newStr += letter
    # return newStr

    return phrase[::-1]