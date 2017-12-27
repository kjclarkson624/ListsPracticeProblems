## Write a Python program to remove duplicates from a list.

def removeDuplicates(list):
    newList = []
    for item in list:
        if item not in newList:
            newList.append(item)
    print(newList)

def main():
    aList = [2,3,5,6,7,6,9]
    removeDuplicates(aList)

main()