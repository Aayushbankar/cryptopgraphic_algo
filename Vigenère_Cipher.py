class vignereCipher :
    def __exp_key (self, key_chr , t_len):
        exky_list = []
        k_len = len(key_chr)
        for i in range(t_len):
            exky_list.append(key_chr[ i%  k_len])

        return exky_list


    def encrypt (self,key , plain_text ):

        # Version 2 
        
        # step 1 

        plns = [ord(c) - ord("A") for c in plain_text if c.isalpha()]
        kns = [ord(c) - ord("A") for c in key if c.isalpha()]

        # step 2 
        expland_k = self.__exp_key(kns,len(plns))

        # step 3 
        ctx_nums = []
        for i in range(len(plns)):
            # The Formula: (P + K) % 26
            val = (plns[i] + expland_k[i]) % 26
            ctx_nums.append(val)
            
        # 4. Convert back to String
        cipher_text = "".join([chr(num + 65) for num in ctx_nums])
        return cipher_text

#       Version 1  --> blueprint for further optimisations 
#       {
#            for i in plain_text:
#                char = ord(f"{i}")
#                if char >= 65 and char <= 90:
#                    pl.append(char - ord("A"))
#            print(pl)
#            for i in key:
#                char = ord(f"{i}")
#                if char >= 65 and char <= 90:
#                    k.append(char - ord("A"))
        
#            pl_len = len(pl)
#            k_len = len(k)
#            diff = pl_len - k_len
#            print(f"pl_len:{pl_len} ; k_len : {k_len} ; diff : {diff}")

#            for i in range(diff):
#                if i < diff :
#                    k.append(k[i % diff])
#                else :
#                    k.append(k[i])

#            print(len(pl) == len(k))
#            print(f"pl = {pl} ; k = {k}")
#            for i in range(len(pl)):
#                val = (pl[i] + k[i]) % 26
#                ctx.append(val)
#            print(ctx)
#            cipher_text = ""
#            for num_val in ctx : 
#                cipher_text += f"{chr(num_val + 65)}"
#                # print(f"{chr(num_val + 65)}")
#            print(cipher_text)
#            return cipher_text 
#           }


    def decrypt (self,key , cipher_text ):
        # step 1
        clns = [ord(c) - ord("A") for c in cipher_text]
        kns = [ ord(c) - ord ("A") for c in key ]

        # step 2 
        expland_k = self.__exp_key(kns,len(clns))


        # step 3 
        ptx_nums = []
        for i in range(len(clns)):
            # The Formula: (P + K) % 26
            val = (clns[i] - expland_k[i]+ 26 ) % 26
            ptx_nums.append(val)

        # step 4 
        plain_text = "".join([chr(num + 65) for num in ptx_nums])
        return plain_text

    def menu(self):
        while True:
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Exit")
            choice = input("Choice: ").strip()

            match choice:
                case "1":
                    pt = input("Plain Text: ").upper().strip()
                    k = input("Key: ").upper().strip()
                    print(self.encrypt(k, pt))

                case "2":
                    ct = input("Cipher Text: ").upper().strip()
                    k = input("Key: ").upper().strip()
                    print(self.decrypt(k, ct))

                case "3":
                    return

                case _:
                    continue


if __name__ == "__main__":
    vc = vignereCipher()
    vc.menu()

