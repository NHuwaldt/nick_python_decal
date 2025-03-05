import numpy as np
import re


##Problem 1

def square_func(x, y):
    return np.power(x, y)

tesst=square_func(2, 4)
tesst

def alt(x, y):
    return np.exp(y*np.log(x))

alt(2,3)


##Problem 2

def list_to_tuple(list):
    return (np.max(list), np.min(list))

test_list = [1, 4, 17, 12, 99, 36, 74, 16, 52, 82]

print(list_to_tuple(test_list))


##Problem 3

def weekend(day):
    if day<=1:
        print("No, it's monday, bummer")
    elif day<=2:
        print("Nope, it's tuesday")
    elif day<=3:
        print("Nuh uh, Wednesday")
    elif day<=4:
        print("Nope, Thursday")
    elif day<=5:
        print("Depending on who you ask, Friday is basically the weekend...")
    elif day<=7:
        print("Yes, enjoy it while it lasts!")
    else: print("Invalid Input, Please enter integer representation of a day of the week")

weekend(5)


##Problem 4

def fuel_eff(dist, fuel):
    return dist/fuel

fuel_eff(70, 21.5)


##Problem 5

def decoder(n):
    last_digit = n%10
    print(last_digit)
    order = n//10
    print(order)
    power = (np.log10(n)//1)
    print(power)
    return last_digit*(10**power) + order

test_number = 54321
decoder(test_number)


# #Problem 6
# #This code keeps reiterating indefinitely and I can't figure out why. I'll have to ask why, but for now it's commented out

# #For Loop

# def max_finder(list):
#     max = list[0]
#     for i in list:
#         if i > max:
#             max = i

#     return max


# def min_finder(list):
#     min = list[0]
#     for i in list:
#         if i < min:
#             min = i

#     return min

# #While Loop

# def while_max(list):
#     i=1
#     max = list[0]
#     while i<len(list):
#         if list[i]>max:
#             max = list[i]
#     return max

# def while_min(list):
#     i=1
#     min = list[0]
#     while i<len(list):
#         if list[i]<min:
#             min = list[i]
#     return min


##Problem 7

def vowel_consonant_num(input):
    vowel_num = len(re.findall(r'[AEIOUaeiou]', input))#note: when defining a pattern, [] brackets will treat each entity inside as an individual
    cons_num = len(input)-vowel_num
    return ("Vowels:", vowel_num, "Consonants:", cons_num)


##Problem 8
num=2468
def dig_root(n):
    string_conv = str(n)
    int_conv = [int(i) for i in string_conv]
    return np.sum(int_conv)