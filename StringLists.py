UserString = raw_input("Enter a string, man. ")

ReverseString = UserString[::-1]

if UserString == ReverseString:
    print("This is a palindrome.")
else:
    print "This is not a palindrome."
