def is_palindrome(string):
    return string == string[::-1]

def is_palindrome_chunk(string):
    len = string.__len__()
    for i in range(len // 2):
        if string[i]!= string[len - i - 1]:
            return False
    return True

print(is_palindrome('madam'))
print(is_palindrome_chunk('madam'))