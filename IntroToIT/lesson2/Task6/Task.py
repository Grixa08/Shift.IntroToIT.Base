#INTRO TO IT 2nd COURSE
# Задача 6: Гласные в высоте!
# Посчитай количество гласных букв в строке.
def counting_of_the_voiceless(сline):
    return sum(1 for символ in сline if символ.lower() in "аеёиоуыэюя")
line = "Привет, мир!"
print(f"В '{line}' {counting_of_the_voiceless(line)} vowels")
