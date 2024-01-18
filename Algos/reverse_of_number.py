def reverse_number(num):
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev

print(reverse_number(1234))