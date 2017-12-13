def compare_dict(source, destination, keys):
    for key, value in keys.items():
        try:
            if not compare_key(source[key], destination[key], value):
                return False
        except KeyError:
            return False
    return True


def compare_list(source, destination, ref):
    if len(ref) == 0:
        return source == destination
    if isinstance(ref[0], dict):
        return has_all_dicts(source, destination, ref[0])
    if isinstance(ref[0], list):
        return has_all_lists(source, destination, ref[0])


def compare_key(source, destination, key):
    if isinstance(key, list):
        return compare_list(source, destination, key)
    if isinstance(key, dict):
        return compare_dict(source, destination, key)
    return source == destination


def has_all_dicts(source, destination, keys):
    matches = []
    for i in source:
        for index, j in enumerate(destination):
            if index not in matches and compare_dict(i, j, keys):
                matches.append(index)
                break
    if len(matches) == len(source) and len(matches) == len(destination):
        return True
    return False


def has_all_lists(source, destination, keys):
    matches = []
    for i in source:
        for index, j in enumerate(destination):
            if index not in matches and compare_list(i, j, keys):
                matches.append(index)
                break
    if len(matches) == len(source) and len(matches) == len(destination):
        return True
    return False
