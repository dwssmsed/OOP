# Вправи
# 1
names = ['Kristian', 'Vanya', 'Yura']
print(names[0])
print(names[1])
print(names[2])
# 2
vehicles = ['car', 'plane', 'bus']
print(f"I want to buy a {plane}.")
# 3
years = [2005, 2006, 2007, 2008, 2009, 2010]
print(years[3])
years.append(2011)
print(years)
print(years[-1])
# 4
things = ['wallet', 'mirror', 'umbrella']
print(things[-1].capitalize())
print(things)
print(things[-1].upper())
print(things)
things.pop(-1)
print(things)
# 5
languages = ['Georgian', 'Estonian', 'Ukrainian']
print(languages[2].lower())
print(languages[2].swapcase())
print(languages[2].capitalize())
# 6
software = ['applications', 'programs', 'scripts']
software[0] = 'apps'
print(software)
hardware = ('CPU', 'case', 'monitor')
hardware_list = list(hardware)
hardware_list[0] = 'Central Processing Unit'
hardware = tuple(hardware_list)
print(hardware)

# Задачі
# 1
languages_list = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']
sorted_list = sorted(languages_list)
print(sorted_list)
languages_list.reverse()
print(languages_list)
languages_list.sort()
print(languages_list)

# 2
numbers = '1 3 6 8 2'
list_n = numbers.split(' ')
numsum = 0
for num in list_n:
    num = int(num)
    numsum += num
print(numsum)

# 3
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
# cities.insert(5, 'and')
# print(cities)
# print(", ".join(cities))
print(", ".join(cities[0:5]), 'and', "".join(cities[-1]))

# 4
str_numbers = "1 2 3 4 5"
print(str_numbers.split(' '))
list_2 = str_numbers.split(' ').copy()
list_2.reverse()
print(list_2)
print(''.join(list_2))

# 5
sports = ['football', 'tennis', 'karate', 'skiing']
sports.append('swimming')
sports.reverse()
sports.extend(['running', 'dancing'])
sports.pop(0)
sports.insert(0, 'gymnastics')
sports.remove('tennis')
del sports[-1]
sports.sort()
print(len(sports))
print(sports.index('skiing'))
sports.clear()

print(sports)


# A  return only even indexed elements
nums = [1, 2, 3, 4, 5]
print(nums[0::2])

# B  return even elements
nums1 = [1, 2, 2, 3, 3, 3, 4]
even_nums = []
for num in nums1:
    if num % 2 == 0:
        even_nums.append(num)
print(even_nums)

# C
test_list = [1, 5, 2, 4, 3]
res = []
for idx in range(len(test_list)):
    if any(test_list[idx] > x for x in test_list[:idx]):
        res.append(idx)
print(res)
