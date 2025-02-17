
def encrypt(flag,i):
    charSet = b""
    for byte in flag:
        a=int(str(i)[:2])
        new_char_code = byte^a
        charSet += bytes([new_char_code%255]) 
        i*=2
        
    return charSet


encrypted_flag=b'|u{WxLS)\x7fR(~\x7fUymT'

i=635

