def is_palindrome(s):
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())  
    
    return cleaned_s == cleaned_s[::-1]

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
