"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Dante Castilleja
Lab Time: Friday 3:00

"""


def reverse_binary():
    user_num = int(input())
    while user_num >= 1 :
        if user_num % 2 == 0 :
            print(0, end = "")
            user_num //= 2
        elif user_num % 2 != 0 :
            print(1, end = "")
            user_num //= 2
        elif user_num <= 1 :
            print(1, end = "")

if __name__ == "__main__":
    reverse_binary()