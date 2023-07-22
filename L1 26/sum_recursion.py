def integers_sum(numbers, index):
    if index == 0:             #base case, if the index is 0, return the number at index 0
        return numbers[0]
    
    #recursive case
    return numbers[index] + integers_sum(numbers, index - 1)

integers_list = [2,4,6,8,10]
index_target = 3
    
result_exercise = integers_sum(integers_list, index_target)

print(f"The sum of the integers up to index {index_target} is {result_exercise}")