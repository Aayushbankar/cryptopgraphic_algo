import numpy as np 


class hillCipher :

    # def _converter(self,text ):
    #     pass
    # ver 1.0 - inital guessing 
    # def _matrix_distributor(self,str, k):
    #     lstl  = []
    #     for i in range(len(str)):
    #         if i %k == 0:
    #             sub = str[i:i+k]
    #             lst = []
    #             for j in sub:
    #                 lst.append(ord(j) - ord("A"))
    #             vls = len(lst) < 3  and len(lst) !=3
    #             while vls :
    #                 lst.append(ord("X")) #padded value 
    #             lstl.append(lst)

    #     return lstl      
    # v2 after reding and watching some videos 
    def _matrix_distributor(self, text, k):
        """
        Converts text into a list of k-length vectors (list of lists of integers).
        Pads with 'X' if necessary.
        """
        lstl = []
        
        # 1. Pad the text if its length is not a multiple of k
        if len(text) % k != 0:
            padding_len = k - (len(text) % k)
            # Pad with 'X' 
            text += 'X' * padding_len
        
        # 2. Convert and chunk the text
        for i in range(0, len(text), k):
            sub = text[i:i+k]
            lst = [ord(char) - ord("A") for char in sub]
            lstl.append(lst)
            
        return lstl
    # helper func
    def _convert_to_text(self, vector_list):
        """Converts a list of integer vectors back into a single string."""
        text = ""
        for vector in vector_list:
            # Convert integer (0-25) back to character (A-Z)
            text += "".join([chr(i % 26 + ord("A")) for i in vector])
        return text

    def encrypt ( self , key_mt , pt_mt):
        # print(f" key : { key} \n plain_text : { plain_text } ")
        ke  = np.array(key_mt)

        ci_vec = []

        print(f" key matrix : {ke} \n")

        # --- Matrix Multiplication: C = (P * K) mod 26 ---
        for pvi in pt_mt:
            p_arr = np.array(pvi).T
            C_unmod = np.dot(p_arr, ke)
            C_mod = C_unmod % 26
            ci_vec.append(C_mod.tolist())
        
        CIPHER_TEXT =   self._convert_to_text(ci_vec)

        return CIPHER_TEXT


    def decrypt ( self , key , cipher_text):
        pass



if __name__ == "__main__":
    hc = hillCipher()
    try:
        key_str = input("Enter a key with 9 characters (A-Z): ").strip().upper()
        if len(key_str) != 9:
            raise Exception("[invalid key] : Key must be 9 characters for a 3x3 matrix.")

        # Key validation check: The determinant must be coprime to 26 (i.e., gcd(det, 26) = 1)
        # This is a crucial step for decryption, but we'll skip the full check for now.
        
        plain_text = input("Enter your plain text (A-Z only, no spaces): ").strip().upper()
        
        # 1. Distribute key and plaintext into matrices/vectors
        key_list = hc._matrix_distributor(key_str, 3)
        plain_list = hc._matrix_distributor(plain_text, 3)
        
        # 2. Encrypt
        cipher_text = hc.encrypt(key_mt=key_list, pt_mt=plain_list)
        print(f"\nCipher Text: {cipher_text}")

    except Exception as e:
        print(e)
