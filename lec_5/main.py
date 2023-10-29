def sum_of_elements(numbers, exclude_negative=False):
    myList=[int(num) for num in numbers]
    if exclude_negative:
        filtered_numbers = [num for num in myList if num >= 0]
        total = sum(filtered_numbers)
    else:
        total = sum(myList)
    return total



input_numbers = "1 2 3 -1"  # Replace this with user input
answer = sum_of_elements(input_numbers.split())
print(answer)
