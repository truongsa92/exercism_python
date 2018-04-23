def transform(old):
    new = {}
    for key, items in old.items():
        for item in items:
            new[item.lower()] = key
    return new
