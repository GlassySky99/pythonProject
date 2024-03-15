def is_palindrome(s):
    s = s.lower().replace(" ", "")

    return s == s[::-1]
string = input("Введите строку: ")

if is_palindrome(string):
    print("Это палиндром!")
else:
    print("Это какая то шляпа.")