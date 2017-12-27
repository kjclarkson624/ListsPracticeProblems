## Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

def remove_elements(list):
    del list[0]
    del list[4]
    del list[5]
    print(list)

def main():
    list = [1,2,3,4,5,6,7,8,9,10]
    remove_elements(list)

main()