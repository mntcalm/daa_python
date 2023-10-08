#import string

print("введить Ім'я")
im=input()
print("введить Прізвище")
pr=input()

out_str="Форматуємо строку: ім'я: {}, прізвище: {}"

print(out_str.format(im,pr))
