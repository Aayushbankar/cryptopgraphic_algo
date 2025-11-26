# additive cipher 

class additive_cipher :
    # Encryption rule:
    # E(x) = (x + k) mod 26.
    def encrypt(self ,key , plain_text ):
        ctx = [chr((((ord(c) - ord("A")) + key) % 26) + ord("A")) for c in plain_text]
        # print(ctx)
        return  "".join(ctx)



    def decrypt(self, key, cipher_text):
        ptx = [chr((((ord(c) - ord("A")) - key) % 26) + ord("A")) for c in cipher_text]
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
                    print(self.encrypt(k, pt))

                case "2":
                    ct = input("Cipher Text: ").upper().strip()
                    k = int(input("Key: ").strip())
                    print(self.decrypt(k, ct))

                case "3":
                    return

                case _:
                    continue


if __name__ == "__main__":
    adc = additive_cipher()
    adc.menu()