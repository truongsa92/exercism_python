def detect_anagrams(string, words):
    letters = sorted(string.lower())
    arrs = []
    for word in words: 
        if sorted(word.lower()) == letters and word.lower() != string.lower():
            arrs.append(word)
    return arrs
print(detect_anagrams('listen', ['nguyen', 'truong', 'tenlis']))