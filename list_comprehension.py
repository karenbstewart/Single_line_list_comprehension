# numbers =range(1,11)

# evens_squared = [expression for_loop condition]

# evens_squared = [number * number for number in numbers if number % 2 == 0]
# print(evens_squared)

# for number in numbers:
#     if number % 2 == 0:
#         evens_squared.append(number * number)

# print(evens_squared)

ages = [5, 15, 64, 27, 84, 26]
odd_ages = []
for age in ages:
    if age % 2 != 0:
        odd_ages.append(age)

print(odd_ages)

odd_ages2 = [age for age in ages if age % 2 != 0]
print(odd_ages2)
    
chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]

long_names = [name for name in chicken_names if len(name) > 10]
print(long_names)

h_names = [name for name in chicken_names if name[0] == "H"]
print(h_names)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

first = [word[0].lower() for word in words ]
print(first)