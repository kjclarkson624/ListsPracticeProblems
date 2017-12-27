## Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
def squares(list):
    for num in range(1,31):
        list.append(num**2)
    print(list[:5])
    print(list[-5:])

def main():
    numlist = []
    squares(numlist)

main()