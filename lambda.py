#lambda parameters: expression

double = lambda x: x * 2
add = lambda x, y: x + y

print(double(7))
print(add(4, 5))

max_value = lambda x, y: x if x > y else y

print(max_value(7, 10))

full_name = lambda first, last: first + " " + last

print(full_name("Žiga", "js"))

is_even = lambda x: x % 2 == 0

print(is_even(7))

age_check = lambda age: True if age > 18 else False

print(age_check(75))

st_znakov = lambda sez: sum(len(i) for i in sez)

print(st_znakov(["asd", "asd", "i"]))

list = [["asd", "asd", "i"], ["asd", "asd", "iertzui"], ["asd", "asdasdrtzuio"]]
print(min(list, key=lambda x: sum(len(i) for i in x)))



