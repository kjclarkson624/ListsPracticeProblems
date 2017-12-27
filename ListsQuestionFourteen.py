## Write a Python program to print the numbers of a specified list after removing even numbers from it.

def remove_even(list):
    index = 0
    for item in list:
        if list[index] % 2 == 0:
            del list[index]
        index += 1
    print(list)


def main():
    list = [1,2,3,4,5,6,7,8,9,10]
    remove_even(list)

main()