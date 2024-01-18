def reverse_string(string):
    chars = list(string)
    k = len(chars) - 1
    for i in range(k):
        temp = chars[i]
        chars[i] = chars[k]
        chars[k] = temp
        k = k - 1
    return ''.join(chars)

print(reverse_string('hello'))