## Write a Python program to generate all permutations of a list in Python.

# So we can approach this problem in a few ways.
# For starters we can use the recursion way of getting our permutations, but this takes a long time to do.
# Next we can create our function for our permutations, which would work.
# But there is an easier, much more efficient way of creating permutations from tuples.
from itertools import permutations  ## we import the permutations function from the module itertools

def main():
    list = [1,2,3,5]
    permulist = permutations(list)
    ## simply printing the list right after line 11 above will not get the result we want.
    ## we want to see every possible combination of the elements in our list(s), so we must
    ## loop through them element by element.
    for element in permulist:
        print(element)

main()