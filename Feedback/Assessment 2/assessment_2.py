

### Q3.	Write a function that can define whether a word is a Palindrome or not
#   (a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam)

def is_Palindrome():
    chosen_word = is_Palindrome() # <--- this calls itself? Recursive, infinite loop here
    chosen_word_list = "madam".split() # convert chosen word to list of individual letters
    left_index = # assign iteration of chosen_word_list from left
    right_index = # assign iteration of chosen_word_list from right
    if len(chosen_word) % 2 == 0 and left_index == right_index:
        # 'len(chosen_word) % 2 == 0' is used to determine even numbered word
        # 'left_index == right_index'    is used to determine that each iteration of each letter is the same from left_index and right_index
        print("{} is a palindrome".format(chosen_word))
    elif # if len(chosen_word) is an an odd number, ignore the middle number and left_index == right_index:
        print("{} is a palindrome".format(chosen_word))
    else:
        print("{} is NOT a palindrome".format(chosen_word))


is_Palindrome('madam')

"""
Mark: 3 / 8
The length of the word doesn't necessarily matter - we could have asdfe which is odd in length, but not a palindrome
as it is not the same inverse, making parts like line 15 redundant. 

Line 7 is likely going to crash the program - the function is apt to infinitely call itself over and over again,
eventually making us run out of memory. We're studying recursion later in future sessions, but for the time being
be careful of making self-function calls within the very same function itself as this could cause a infinite recursive
loop

Function seems unfinished? The function should be able to act independently (e.g. can juts call it instead of needing
to say modify some variables). Moreover, not sure how the left & right index work - even if they are set to a specific
index value, and those two characters at those indexes match, how would we know necessarily that the others do or
don't match?

I understand how you're trying to approach the question - I recommend to take this further by adding a for loop,
so you check every single left & right index (starting from v left & v right)
and progressively make those two pointers meet in the middle. If at no point
there was no mismatch, then we can confidently say that the word is a palindrome
"""







#### Q9.TWO NUMBER SUM ###

# Please note I did 3 different versions to show my thinking and how I landed on the answer.
# If I had to choose 1, attempt 3 would be my final answer.

## Attempt 1: (including input within function)
#
# def add_to_ten(num1, num2, num3, num4, num5, num6, num7, num8):
#     numbers_list = []  # output list, could also be a set since in no specific order
#     target_sum = 10
#
#     for num_1 in numbers_list:
#         for num_2 in numbers_list:
#             if sum(num_1, num_2) == target_sum and num_1 != num_2: # the sum of number 1 and number 2 iterated
#                 print(list(num_1, num_2))   # convert to list
#         else:
#             print([None]) # print an empty array - not sure how!
#
# result = add_to_ten(3, 5, -4, 7, 11, 1, -1, 6)
# print(result)

## Attempt 2: enitre code outside of a function:

# list = [3, 5, -4, 7, 11, 1, -1, 6]
#
# output_list = []  # output list, could also be a set since in no specific order
# target_sum = 10
#
# for num_1 in list:
#     for num_2 in list:
#         if num_1 + num_2 == target_sum and num_1 != num_2:
#                 print([num_1, num_2])
#         else:
#             pass

# Attempt 3:

list = [3, 5, -4, 7, 11, 1, -1, 6] # could also be a set since in no specific order

def add_to_ten(list, target): # Added new parameter target to speed function calls
    numbers_list = []  # output list
    target_sum = target

    for num_1 in list:
        for num_2 in list: # Better to begin num_2 after num_1, instead of from the very beginning each time
            if num_1 + num_2 == target_sum and num_1 != num_2: # can also use 'sum(num_1, num_2)'
                print([num_1, num_2])   # convert to list
        else:
            print([]) # print an empty array as per question, otherwise I'd use 'pass'

# Instructor Function Checks
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
target = 18
# Expect [3, 15]

result = add_to_ten(array, target)
print ("-\n")

array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
target = 163
# Expect [-47, 210]

result = add_to_ten(array, target)
print ("-\n")

array = [15]
target = 15
# Expect []

result = add_to_ten(array, target)
print ("-\n")

"""
Mark: 20 / 22
Outstanding! The function in answer 3 works correctly - I get the correct answer, evne in instances where there is no
actual answer (in which case I get an empty array). Note that you don't have to print ([]) in the else statement every time
- you could .append each new list to your output list, and at the very end either output that output_list or a empty list
depending on how many elements you added.

Work in general is very good and shows clear thought! Consider below as well for areas to improve. Lmk if you have Qs, this
was fantastic to mark!

Two points for feedback:
What if we have a array of [15, 15], and the target is 30? In this instance, we shouldn't dismiss the values because
both are 15. I understand that the num1 != num2 is intended for avoiding the same number (in the same position of the loop)
being counted twice, but this does potentially cause issues later on. To avoid this, I recommend formatting your for loops
so that the second one begins AFTER the first one's position (e.g.
for idx in range(0, len(list) - 1): # <- goes through index by index
    for jdx in range(idx + 1 len(list)): # <- second index that begins AFTER idx
        num1 = list[idx]
        num2 = list[jdx]
        
Second point:
Similar to the first one - both for loops begin from the very beginning of thhe list everytime (pertinent most to the second
loop). This means the second loop starts from index of 0, and iterates every time - as a result, the answer we get e.g.
[x, y] is also alongside other answers like [y, x] (since both for loops will go through it all). Something for-loop like above
would fix this
"""