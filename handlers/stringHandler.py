import difflib
# ChatGtP nonsense


def get_common_parts_old(strings):
    common_parts = set(strings)
    no_common_parts = []
    while common_parts:
        string1 = common_parts.pop()
        new_common_parts = set()
        for string2 in common_parts:
            for i in range(min(len(string1), len(string2))):
                if string1[i] != string2[i]:
                    common = string1[:i]
                    if common:
                        new_common_parts.add(common)
                    break
            else:
                common = string1[:i+1]
                if common:
                    new_common_parts.add(common)
        if not new_common_parts:
            common_parts = new_common_parts
        else:
            common_parts = new_common_parts
    for string in strings:
        if string not in common_parts:
            no_common_parts.append(string)
    return list(common_parts).extend(no_common_parts)


def get_common_parts(strings):
    s = difflib.SequenceMatcher(a=strings[0], b=strings[1])
    common_parts = s.find_longest_match(0, len(strings[0]), 0, len(strings[1]))
    common_parts = strings[0][common_parts[0]:common_parts[0]+common_parts[2]]
    for i in range(2, len(strings)):
        s = difflib.SequenceMatcher(a=common_parts, b=strings[i])
        match = s.find_longest_match(0, len(common_parts), 0, len(strings[i]))
        if match[2] == 0:
            common_parts = ''
            break
        else:
            common_parts = common_parts[match[0]:match[0]+match[2]]
    no_common_parts = [string.replace(common_parts, "", 1) for string in strings]
    return [common_parts], no_common_parts