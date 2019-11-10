input  = input("Enter a String to check it's palindrome or not " )
rev=input [::-1]
print("String: " + input)
print("Reverse: " + rev)
if input==rev:
    print(input + " is a palindrome.")
else:
    print(input + " is not a palindrome.")