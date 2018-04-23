def transform(old):
    new = {}
    for key, items in old.items():
        for item in items:
            new[item.lower()] = key
    return new
print(transform({1: ['APPLE', 'ARTICHOKE'], 2: ['BOAT', 'BALLERINA']}))