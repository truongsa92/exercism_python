from string import ascii_uppercase

def make_diamond(lt):
    lines = []
    length = ascii_uppercase.index(lt) + 1
    for l in range(length):
        line = [' '] * length
        line[l] = ascii_uppercase[l]
        lines.append("".join(line[::-1] + line[1:]))
    return("\n".join(lines[:-1] + lines[::-1]) + "\n" )
