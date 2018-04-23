def is_isogram(string):
    letters = []
    for l in string:
        if l.isalpha():
            letters.append(l.lower())
    return len(letters) == len(set(letters))       
