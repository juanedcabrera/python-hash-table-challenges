'''
1. Character Count:
given a string count each letter in the string and then print the result.

Example 1:

character_count('banana')

Input: 'banana'
Output (in the console): 
the character b occurs 1 times
the character a occurs 3 times
the character n occurs 2 times

Example 2:

character_count('hello world')

Input: 'hello world'
Output (in the console): 
the character h occurs 1 times
the character e occurs 1 times
the character l occurs 3 times
the character o occurs 2 times
the character   occurs 1 times
the character w occurs 1 times
the character r occurs 1 times
the character d occurs 1 times
'''

def character_count(string):
    for i in string:
        print(f"the character {i} occurs {string.count(i)} times")

character_count('banana')
character_count('hello world')


# def character_count(string):
#     count_dict = {}
#     for i in string:
#         if i in count_dict:
#             count_dict[i] += 1
#         else:
#             count_dict[i] = 1
#     for key, value in count_dict.items():
#         print(f"the character {key} occurs {value} times")

character_count('banana')
character_count('hello world')
