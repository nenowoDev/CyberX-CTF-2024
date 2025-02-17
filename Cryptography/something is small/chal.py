import random
from sympy import isprime
from sympy import primefactors
from sympy import mod_inverse

def generate_random_prime(min_value, max_value): return next(x for x in (random.randint(min_value, max_value) for _ in iter(int, 1)) if isprime(x))



p=generate_random_prime(10, 1000)
q=generate_random_prime(10, 1000)
p=449
q=617
n=p*q
phi= (p-1)*(q-1)
e = 65537
d=mod_inverse(e, phi)



public_key = (e, n)
private_key = (d, n)

def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]


def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

message="message"
encrypted_message=encrypt(message,public_key)

print(f"N is {n}")
print(f"encrypted message = {encrypted_message}")

# N is 32819
# encrypted message = [24108, 8462, 797, 529, 23224, 18825, 27784, 8575, 13746, 29595, 24798, 2306, 2306, 21446, 14949, 23224, 11319, 13746, 26891, 27150] 
