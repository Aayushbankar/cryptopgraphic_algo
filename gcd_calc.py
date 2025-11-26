'''

for this practical i have used recursion .

'''
def gcd_calculator(a,b):
    if b == 0  :
        return a 
      
    r = a % b

    return gcd_calculator( b , r )

if __name__ == "__main__":
    

    # taking inputs 
    a = int(input("enter the value for a "))
    b = int(input("enter the value for b "))


    gcd = gcd_calculator(a,b)

    print(gcd)