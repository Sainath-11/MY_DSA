"""
    Recursion : 
                1) Assumption 
                2) Main Logic 
                3) Base Condition 
        Direction of recursion is always from top to bottom ( calling of function)
        Work of Direction is either top-to -bottom or bottom-to -top


basics Questions :
 1. Write a recursive function that prints "Hello" exactly 5 times.
 2. Print numbers from 1 to 5 using recursion without parameters.
 3. Print numbers from 5 to 1 using recursion without loops.
 4. Print "Before Call" and "After Call" to observe call order.
 5. Print numbers from 1 to n after the recursive call. // ( same as 3)
 6. Print numbers from 1 to n before the recursive call.
 7. Print "Start" only once and "End" only once using recursion.
 8. Print the current value of n during each recursive call.
 9. Write a recursive function that stops only when n == 0.
10. Dry-run a recursive function manually and write call stack states.


from 7 to 10 class work 

"""
class Solution:
    def print_hello(self,num):
        if num == 0:
            return 
        print("Hello")
        self.print_hello(num-1)
    def recurivseOb(self,num):
        if num == 0 :
            return 
        print("Before Call")
        self.recurivseOb(num-1)
        print("After call")
    def printNumber1toN(self,num):
        if num == 0:
            return
        self.printNumber1toN(num-1)
        print(num)
    def printNumber1toNB(self,num,i=0):
        if num ==i :
            return 
        print(i+1)
        self.printNumber1toN(num,i+1)
    

    
