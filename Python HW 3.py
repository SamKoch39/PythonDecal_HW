#1
x = 2
y = 3
def computePower(any_x, any_y):
    result = 1
    for _ in range(any_y):
        result *= any_x
    return result

print(computePower(x, y))

#2:
readings = [15, 14, 17, 20, 23, 28, 20]
def temperatureRange(any_readings):
    return (min(any_readings), max(any_readings))

print(temperatureRange(readings))

#3:
day = 6 #Saturday
def isWeekend(any_day):
    return any_day == 6 or any_day == 7
        
print(isWeekend(day))

#4
distance = 70 #miles
fuel = 21.5 #gallons
def fuel_efficiency(any_distance, any_fuel):
    return (any_distance/any_fuel)

print(fuel_efficiency(distance, fuel))

#5
n = 12345
def decodeNumbers(any_integer):
    last_digit = any_integer % 10
    nonlast_digits = any_integer // 10
    place_value = 1

    while nonlast_digits >= place_value:
        place_value *= 10

    result = last_digit * place_value + nonlast_digits
    return result

print(decodeNumbers(n))

#6, 6.1a
nums = [2024, 98, 131, 2, 3, 72]
def find_min_with_for_loop(num_list):
    min_value = nums[0]
    for num in num_list:
        if num < min_value:
            min_value = num
    return min_value

print(find_min_with_for_loop(nums))

#6, 6.1b
def find_max_with_for_loop(num_list):
    max_value = num_list[0]
    for num in num_list:
        if num > max_value:
            max_value = num
    return max_value

print (find_max_with_for_loop(nums))

#6, 6.2a
def find_min_with_while_loop(num_list2):
    min_value2 = num_list2[0]
    i = 1
    while i < len(num_list2):
        if num_list2[i] < min_value2:
            min_value2 = nums[i]
        i += 1
    return min_value2

print(find_min_with_while_loop(nums))

#6, 6.2b
def find_max_with_while_loop(num_list2):
    max_value2 = num_list2[0]
    j = 1
    while j > len(num_list2):
        if num_list2[j] > max_value2:
            max_value2 = num_list2[j]
        j += 1
    return max_value2

print(find_max_with_while_loop(nums))

#7
text = "UC Berkeley, founded in 1868!"
def vowel_and_consonant_count(any_text):
    vowels = "AEIOUaeiou"
    number_of_vowels = 0
    number_of_consonants = 0

    for letter in any_text:
        if letter.isalpha():
            if letter in vowels:
                number_of_vowels += 1
            else:
                number_of_consonants += 1
    return (number_of_vowels, number_of_consonants)

print(vowel_and_consonant_count(text))

#8
num = 2468
def digital_root(any_num):
    sum_of_dig = 0
    for dig in str(any_num):
        sum_of_dig += int(dig)
    return sum_of_dig

print(digital_root(num))
