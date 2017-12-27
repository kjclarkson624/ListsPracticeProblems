## Write a Python function that takes two lists and returns True if they have at least one common member.

def comparelists(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

def main():
    list1 = [1,2,5,55,6,67,39344,4,5]
    list2 = [2,3,4,5,6,7,5,3]
    list3 = [5,6,7,8,9,10]
    list4 = [1,2,3,4]
    print(comparelists(list1, list2))
    print(comparelists(list3, list4))

main()