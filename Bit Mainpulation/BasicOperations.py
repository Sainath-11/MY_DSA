""" 
    machince understand only -- > binary number 
    user --> [input -- > number] --> cpu -->[ ALU --> convert to binary --> perfrom operation] --> output

    1's  compliment --> flips the digits 
    2's compliment --> 1) flips the digits first 2) add 1  --> (1's +1)

    machince stores negative number in 2's compliment 
    For negative sign repersentation the machince store sign bit (MSB) if MSB == 1 Then negative (-) Not postive number 

    Operators :
          AND (&) : all true(1) --> true   one false(0) --> False
          OR(|) : one True (1) --> True  all false(0) --> False 
          XOR(^) : even  1 --> 0  odd 1 --> 1
          NOT(~) : flips the bits 0-->1 1--> 0 
          leftshit(<<) : x >> i == x * (2**i)
          rightshit(>>) : x>>i  == x // (2**i)


    Properties :
            1) a & b = b & a   a ^ b = b ^ a   a|b = b|a 
            2) a & a = a       a ^ a = 0       a | a = a
            3) (a & b)& c = a & (b&c)
            4) (a&b)|c = (a|c) & (b|c)        (a^b)&c = (a&c) ^ (c&b)
            5) ~(a&b) = ~a | ~b                ~(a|b) = ~a & ~b 
            6) ~a = -(a+1)
            7) -a = ~(a-1)
            8) a &(a-1) set last set bit to 0 
            9) a & (-a) keep only last 1 and set remaning to 0 

"""

class Solution:
    def swapNumber(self,a,b)->None:
        a = a ^ b
        b = b ^ a 
        a = a ^ b 

    #check if the given i th bit is set or not 
    def checkbit(self,num,i):
        # ((num*(1<<i))==1  why extra baracket bcz == is higher priorty then << 
        # sol   ((num>>i)&1)==1 or (num & (1<<i)) == (1<<i) or num & (1<<i)!=0
        return num & (1<<i)!=0 
    
    def setbit(self,num,i):
        return num | (1<<i)
    
    def clearbit(self,num,i):
        return num & (~(1<<i))
    
    def toggleBit(self,num,i):
        # 1 --> 0 
        # 0-->1
        return num ^ (1<<i)
    
    def removelastsitbit(self,num,i):
        return num & (num-1)
    
    def ispowerof2(self,num):
        return num & (num-1) == 0 
    
    def nofsitbit(slef,num):
        count = 0 
        while num!=0 :
            num = num & (num-1)
            count = count + 1
        return count 
    
def main():
    num = int(input("Enter the Number "))
    sol = Solution()
    print(sol.nofsitbit(num))


if __name__ == "__main__":
    main()

    