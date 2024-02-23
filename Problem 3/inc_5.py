"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Dante Castilleja
Lab Time: Friday 3:00
"""

def inc_5():
    n1 = int(input())
    n2 = int(input())
    print(n1, end = " ")
    if n1 > n2 :
        print("Second integer can't be less than the first.")
    while n2 >= n1 :
        n1 += 5
        print(n1, end = " ")
    

if __name__ == '__main__':
    inc_5()