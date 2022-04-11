#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backward

palindrome = input("Enter a string: ")
palindrome = palindrome.replace(" ", "")
rev_palindrome = palindrome[::-1]    #way to reverse a string

if palindrome  == rev_palindrome:
    print("Yes, it is a palindrome")
else:
    print("No, it's not a palindrome.")