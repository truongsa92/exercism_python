def test(string):
    arrs = string.strip().split(' ')
    text = ""
    for arr in arrs:
        if arr:
            text += arr[0].upper()
    return text
print(test(' nguyenx trong  sa '))