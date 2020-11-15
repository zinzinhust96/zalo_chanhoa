def get_items_that_duplicate_from_list(dup_list):
    seen = {}
    dupes = []

    for item in dup_list:
        if item not in seen:
            seen[item] = 1
        else:
            if seen[item] == 1:
                dupes.append(item)
            seen[item] += 1

    return dupes