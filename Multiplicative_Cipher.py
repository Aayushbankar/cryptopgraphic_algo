# Multiplicative Cipher
from extended_eucledian_gcd import extended_gcd as egcd

def modinv(a,m = 26):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception ("unsupported key enter another key ")
    else:
        return x % m
   

class multiplicativeCipher :


    def encrypt (self,key,plain_text ):
        '''
        Encryption rule:
        C ≡ (P × K) mod 26
        '''
        ctx = [ chr((((ord (char) - ord("A")) * key ) % 26 )+ ord("A"))  for char in plain_text]
        # for char in plain_text :
        #     x = (char * key ) % 26
        #     ctx.append(char * key ) 
        # for i in range(len(ctx)):
        #     print(f"diff = {ctx[i] - ord(plain_text[i])}")
        # print(ctx)
        return "".join(ctx)

    def decrypt (self,key , cipher_text):
        ptx = [ chr((((ord (char) - ord("A")) * modinv(key) ) % 26 )+  ord("A"))  for char in cipher_text]

        return "".join(ptx)
    def menu(self):
        while True:
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Exit")
            choice = input("Choice: ").strip()

            match choice:
                case "1":
                    pt = input("Plain Text: ").upper().strip()
                    k = int(input("Key: ").strip())
                    try:
                        modinv(k)
                        print(self.encrypt(k, pt))
                    except Exception as e:
                        print(e)

                case "2":
                    ct = input("Cipher Text: ").upper().strip()
                    k = int(input("Key: ").strip())
                    try:
                        modinv(k)
                        print(self.decrypt(k, ct))
                    except Exception as e:
                        print(e)

                case "3":
                    return

                case _:
                    continue


if __name__ == "__main__":
    mc = multiplicativeCipher()
    mc.menu()