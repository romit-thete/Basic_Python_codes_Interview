def list_sum(list_of_nums):
    if len(list_of_nums) == 1:
        return list_of_nums[0]
    return list_of_nums[0] + sum(list_of_nums[1:])


list_of_numbers = [2, 4, 5, 6, 7]
print(list_sum(list_of_numbers))