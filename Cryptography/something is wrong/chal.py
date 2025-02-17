from sympy import mod_inverse

# ------------------------------------------------------------------------------------------
# hey bob, use this value for rsa, please implement the rsa algorithm , i want to use it to secure the flag for cyberx ctf --simon
# ok simon ,,--bob

p=449
q=617
n=p*q
phi= (p-1)*(q-1)
e = 65537
d=mod_inverse(e, phi)

public_key = (e, n)
private_key = (d, n)
# ------------------------------------------------------------------------------------------

# done. -- bob
# ok, i'll check it later --simon

def encrypt(message, public_key):
    e, n = public_key
    return [ord(char)*e% n for char in message]


def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(char * d % n) for char in ciphertext])
# ------------------------------------------------------------------------------------------

# WHAT THE HECK BOB, IT DOESNT WORK 
# i put the flag as message ,encrypt and decrypt it ,, and it doesnt give the flag back..
# please fix it bob....
# here is the output btw 
# encrypted message = [235484, 173053, 50867, 247478, 268360, 226596, 27094, 50867, 71749, 50867, 74640, 56864, 125292, 71749, 122401, 110407, 247478, 262363, 152171, 158168]
# encrypted message = 𻨎𫅊𑤅鈒𑪻३𼀋𑤅𚆮𑤅𪰨𻼰𳏶𚆮𢥼𑝏鈒𪺹𢢡钣
# 
# --simon



message="input???"
encrypted_message=encrypt(message,public_key)
decrypted_message=decrypt(encrypted_message,private_key)

print(f"encrypted message = {encrypted_message}")
print(f"encrypted message = {decrypted_message}")

# bob.. are you there?


# please bob.. please fix it....