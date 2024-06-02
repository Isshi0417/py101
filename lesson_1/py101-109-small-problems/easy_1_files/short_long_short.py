def short_long_short(s1, s2):
    # if length of s1 is shorter than s2
    if len(s1) < len(s2):
        return s1 + s2 + s1
    else:
        return s2 + s1 + s2

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")