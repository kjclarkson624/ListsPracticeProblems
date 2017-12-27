## Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

def last(n): return n[-1]

def sort_tuples(tuples):
    return sorted(tuples, key = last)

def main():
    print(sort_tuples([(2,5),(5,6),(4,3),(7,9),(13,1)]))

main()