#!/usr/bin/env python3

def return_evens(num_list):
    return [i for i in num_list if i % 2 == 0]

return_evens([1, 2, 3, 4, 5, 6, 11, 12, 13, 15, 16])
#     list = [i for i in num_list if 1 % 2 == 0]
#     print(list)
# return_evens([1, 2, 3, 4, 5, 6, 10, 11, 20])
    
    
    
#     for i in range(1, num_list, 2):
#         print([])
    
#     for i in range(0, num_list, 2):
#         print(i)

# return_evens(10)
        

def make_exclamation(sentence_list):
    return [i + '!' for i in sentence_list]