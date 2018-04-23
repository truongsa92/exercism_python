def flatten(iterable):
    if type(iterable) is str:
        return list(iterable)
    flat = []
    for item in iterable:
        try:
            flat.extend(flatten(item))
        except TypeError:
            if item is not None:
                flat.append(item)
    return flat

print(flatten([1,[15,3,None,4],[None],5]))