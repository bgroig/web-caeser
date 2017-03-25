def encrypt(text, rot):

    newtext = ""
    for char in text:
        newchar = rotate_character(char, rot)
        newtext += newchar
    return newtext

def alphabet_position(letter):

    lettercount = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(lettercount)


def rotate_character(char, rot):

    if char.isalpha():
        firstSpot = alphabet_position(char)
        newSpot = firstSpot + rot
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alphabet) -1):
            if alphabet[i] == newSpot:
                newSpot = alphabet[newSpot]
            elif newSpot > 25:
                newSpot = newSpot % 26
            if char == char.upper():
                return alphabet[newSpot].upper()
            return alphabet[newSpot].lower()
    else:
        return char
