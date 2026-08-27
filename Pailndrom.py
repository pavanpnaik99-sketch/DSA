def isPalindrome(x):
    
    original = x
    reverse = 0

    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10

    if original == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"


print(isPalindrome(121))
print(isPalindrome(122))
