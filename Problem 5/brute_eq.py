"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: Dante Castilleja
Lab Time: Friday 3:00
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())

    for x in [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] :
        y = ((a * x) - c) // -b
        y2 = ((d * x) - f) // -e
        if y == y2 :
            break
    for y in [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] :
        x = ((b * y) - c) // -a
        x2 = ((e * y) - f) // -d
        if x == x2 :
            break
    if y == y2 and x == x2 :
        print(f'x = {x2} , y = {y2}')
    else :
        print('There is no solution')

    
if __name__ == "__main__":
    brute_eq()