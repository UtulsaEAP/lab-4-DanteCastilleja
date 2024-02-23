"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Dante Castilleja
Lab Time: Friday 3:00
"""

def norm():
    num = int(input())
    data = []
    for _ in range(num):
        point = float(input())
        data.append(point)
        maxdata = max(data)
    for point in data:
        newdata = point / maxdata
        print(f'{newdata:.2f}')


if __name__ == "__main__":
    norm()