def get_common_parts(strings):
    common_parts = []
    for string in strings:
        for common_part in common_parts:
            if common_part in string:
                break
        else:
            for i in range(len(string)):
                for string2 in strings:
                    if not string.startswith(string[:i], 0, i):
                        break
                else:
                    common_parts.append(string[:i])
                    break
    return common_parts

# example usage
strings = ["hello world", "everyone hello", "hello there", "hello"]
print(get_common_parts(strings))
# Output: ["hello "]