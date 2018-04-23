def check_brackets(strings):
    match = dict(("()","{}","[]"))
    queue = []
    for char in strings:
        if char in match:
            queue.append(match[char])
        elif char in match.values():
            if len(queue) <= 0 or char != queue[-1]:
                return False
            queue.pop()
    return queue == []
print(check_brackets('sa nguyen [{}]'))