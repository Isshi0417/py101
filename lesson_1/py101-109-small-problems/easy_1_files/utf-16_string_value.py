def utf16_value(s):
    value = 0
    # for each character in string
    for c in s:
        # add value to total
        value += ord(c)
    return value

OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)