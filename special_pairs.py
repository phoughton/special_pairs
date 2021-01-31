# This week’s question:
# Given an array of integers arr, a pair (n,m) is called “special” if arr[n] == arr[m], and n < m. Return the number of special pairs. Hint: Nested for loops can work for this one, but a hashmap solution will have a better runtime!

# Examples: 
# $ specialPairs([1,2,3,1,1,3])
# $ 4 // (0,3), (0,4), (3,4), (2,5)

def special_pairs(nums):
    match_store = {}
    specials = []
    for index in range(len(nums)):
        current_num = nums[index]
        if current_num in match_store:
            match_store[current_num][index] = True
        else:
            match_store[current_num] = {index: True}

    for indexes in match_store.values():
        index_keys = list(indexes.keys())
        for pos_a in range(0, len(index_keys)):
            for pos_b in range(pos_a+1, len(index_keys)):
                specials.append((index_keys[pos_a], index_keys[pos_b]))

    return len(specials), specials

print(special_pairs([1,2,3,1,1,3]))
print()
print(special_pairs([1,2,3,1,1,3,2]))
print()
print(special_pairs([1,2,2]))
print()
print(special_pairs([1,1,1,1]))
print()
print(special_pairs([1]))
print()
print(special_pairs([111,111]))
print()
print(special_pairs([1,2,3,4,4,3,2,1]))