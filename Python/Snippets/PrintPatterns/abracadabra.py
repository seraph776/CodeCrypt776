def magical_incantation() -> str:
    """
    Prints the ABRACADABRA inside a magick triangle, and
    returns the word as a string.
    """
    magick_runes = '>=-><>;>=->'
    alchemy = [chr(int(bin(int(rune, 2) ^ (2 ** (len(rune) + 1) - 1))[3:], 2)) for rune in
               ['0' + bin(ord(i))[2:] for i in magick_runes]]
    the_great_void = ""
    for i in range(len(alchemy), 0, -1):
        print(the_great_void, end="")
        for spell in alchemy[0:i]:
            print(spell, end=' ')
        print()
        the_great_void += " "

    return ''.join(alchemy)


magical_incantation()
