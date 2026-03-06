text = input("Enter text: ").replace(" ", "").lower()

if text == text[::-1]:
    print("Palindrome.")
else:
    print("Not a palindrome.")
