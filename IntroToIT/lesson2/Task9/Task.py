#INTRO TO IT 2nd COURSE
# Задача 9: Палиндром ли это?
# Определи, является ли введенная строка палиндромом.
def his_is_a_palindrome(line):
    return line == line[::-1]
line = "radar"
print(f"Is_li '{line}' palindrome? {his_is_a_palindrome(line)}")
