

### Q3.	Write a function that can define whether a word is a Palindrome or not
#   (a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam)

def is_Palindrome():
    chosen_word = is_Palindrome()
    chosen_word_list = # convert chosen word to list of individual letters
    left_index = # assign iteration of chosen_word_list from left
    right_index = # assign iteration of chosen_word_list from right
    if len(chosen_word) % 2 == 0 and left_index == right_index:
        # 'len(chosen_word) % 2 == 0' is used to determine even numbered word
        # 'left_index == right_index' is used to determine that each iteration of each letter is the same from left_index and right_index
        print("{} is a palindrome".format(chosen_word))
    elif # if len(chosen_word) is an an odd number, ignore the middle number and left_index == right_index:
        print("{} is a palindrome".format(chosen_word))
    else:
        print("{} is NOT a palindrome".format(chosen_word))


is_Palindrome('madam')








#### Q9.TWO NUMBER SUM ###

# Please note I did 3 different versions to show my thinking and how I landed on the answer.
# If I had to choose 1, attempt 3 would be my final answer.

## Attempt 1: (including input within function)

def add_to_ten(num1, num2, num3, num4, num5, num6, num7, num8):
    numbers_list = []  # output list, could also be a set since in no specific order
    target_sum = 10

    for num_1 in numbers_list:
        for num_2 in numbers_list:
            if sum(num_1, num_2) == target_sum and num_1 != num_2: # the sum of number 1 and number 2 iterated
                print(list(num_1, num_2))   # convert to list
        else:
            print([None]) # print an empty array - not sure how!

result = add_to_ten(3, 5, -4, 7, 11, 1, -1, 6)
print(result)

## Attempt 2: enitre code outside of a function:

list = [3, 5, -4, 7, 11, 1, -1, 6]

output_list = []  # output list, could also be a set since in no specific order
target_sum = 10

for num_1 in list:
    for num_2 in list:
        if num_1 + num_2 == target_sum and num_1 != num_2:
                print([num_1, num_2])
        else:
            pass

# Attempt 3:

list = [3, 5, -4, 7, 11, 1, -1, 6] # could also be a set since in no specific order

def add_to_ten(list):
    numbers_list = []  # output list
    target_sum = 10

    for num_1 in list:
        for num_2 in list:
            if num_1 + num_2 == target_sum and num_1 != num_2: # can also use 'sum(num_1, num_2)'
                print([num_1, num_2])   # convert to list
        else:
            print([]) # print an empty array as per question, otherwise I'd use 'pass'

result = add_to_ten(list)