def find_largest_element(list):
    if len(list) == 1:  # Base case
        return list[0]
    
    first_element = list[0]
    rest_of_list = list[1:]

    # Recursive call to find the largest element in the rest of the list
    largest_in_rest = find_largest_element(rest_of_list)

    if first_element > largest_in_rest:
        return first_element
    else:
        return largest_in_rest
    
#specified using spaces because was having issues with ","
integer_input = input("Please enter a list of integers using spaces: ")
#used list to make the input into a list, then used map, int to transform the elements into integers
#split to split the input integers
integer_list = list(map(int, integer_input.split()))

result = find_largest_element(integer_list)
print("The largest element in the list is:", result)