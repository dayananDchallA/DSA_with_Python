def gcd(a, b):
    while b!= 0:
        a, b = b, a % b
    return a

def gcd1(a, b):
    while(a!=b):
        if (a<b):
            b=b-a
        if (a> b):
            a=a-b
    return a

print(gcd(12, 18))

print(gcd1(12, 18))