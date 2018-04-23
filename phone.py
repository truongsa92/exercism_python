def clean(number):
    digits = [c for c in number if c.isdigit()]
    if len(digits) == 11 and digits[0] == "1":
        return ''.join(digits[1:])
    elif len(digits) != 10:
        return "0000000000"
    else:
        return ''.join(digits)

print(clean('0987654321'))
print(clean('4534536547567'))
print(clean('12345678900'))