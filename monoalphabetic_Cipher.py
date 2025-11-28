# Monoalphabetic cipher 
from Additive_Cipher import additive_cipher


class monoAlphabeticCipher :
    # def __init__(self,key):
    #     key = self.key()
    def __key_mapper(self,key):
        key_map = {}
        add = additive_cipher()
        for char in range(ord("A"), ord("Z")+1):
            key_map[chr(char)] = add.encrypt(key, chr(char))
        # print(map)
        return key_map

    def encrypt (self,plain_text,key):
        key_map = self.__key_mapper(key)
        # ctx = [ ch := key_map[ch]  for ch in plain_text]
        ctx = []
        for ch in plain_text:
            if ord(ch) > ord("A") and ord(ch) < ord("Z"):
                ctx.append(key_map[ch])
        # print(ctx)
        return "".join(ctx)
    def decrypt (self,cipher_text, key ) :
        key_map = self.__key_mapper(key)
        # ctx = [ ch := key_map[ch]  for ch in plain_text]
        # chars = cipher_text.split()
        # print(chars)
        # # for char , key_val in key_map.items():
        # #     if key_val == 
        
        REV_KEY_MAP = dict(zip(key_map.values(),key_map.keys()))
        # print(REV_KEY_MAP)
        ptx = [REV_KEY_MAP[ch] for ch in cipher_text]
        # for ch in cipher_text :
        #     ptx.append(REV_KEY_MAP[ch])

        return "".join(ptx)

if __name__ == "__main__":
    mac = monoAlphabeticCipher()
    key = int(input("key = "))
    plaintext = input("enter the plaintext ").strip().upper()
    cipher_text =  mac.encrypt(plaintext, key)
    plaintext = mac.decrypt(cipher_text, key)
    print(cipher_text)
    print(plaintext)
