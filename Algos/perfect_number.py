def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False
    
print(perfect_number(6))
print(perfect_number(8))