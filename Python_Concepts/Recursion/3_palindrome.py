def check_palindrome(s):
    s = str(s).lower()
    if len(s) <= 1:
        print("Palindrome")
    else:
        if s[0] == s[-1]:
            return check_palindrome(s[1:-1])
        else:
            print("Not a Palibdrome")

check_palindrome('Saippuakivikauppias')
check_palindrome('madam')