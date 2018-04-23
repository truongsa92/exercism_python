import pdb

def is_isogram(string):
    letters = []
    for l in string:
        if l.isalpha():
            letters.append(l.lower())
    # pdb.set_trace()
    return len(letters) == len(set(letters))       

print(is_isogram('sas'))