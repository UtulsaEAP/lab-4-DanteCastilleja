"""
Complete the following python code to reverse the string entered by the user.

Name: Dante Castilleja
Lab Time: Friday 3:00
"""

def reverse_string():
    while True:
        word = input()
        if word == 'Done' or word == 'done' or word == 'd' :
            break
        else :
            bword = word [::-1]
            print(bword)
if __name__ == "__main__":
    reverse_string()