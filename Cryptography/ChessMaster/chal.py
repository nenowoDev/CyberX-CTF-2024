import random

mapping = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
    'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z','1', '2', '3', '4', 
    '5', '6', '7', '8', '9', '0','{', '}'
]

scrambled_mapping = mapping.copy()

random.seed(12423915)
random.shuffle(scrambled_mapping)

def encrypt(flag):
    value=[]
    for i in range(len(flag)):
        z=scrambled_mapping.index(flag[i])
        chars = "abcdefgh"

        filemodulus=(z%8)
        file=chars[filemodulus]
        
        rank=int(z/8)+1 

        value.append(''.join(f'{file}{rank}'))
    return value


message="CyberX{m4teIn1rip}"
try:
    print(encrypt(message))
except:
    print("Error: Message contains characters not in the mapping.")

