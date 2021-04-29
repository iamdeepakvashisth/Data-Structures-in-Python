#Max  and min value in a dictionary
d={'Y': 9874, 'B': 988, 'C': 15, 'D': 987, 'Z': 88, 'A': 15}
def min_value_dictionary(nums):
        return min(nums.values())
print(min_value_dictionary(d))

def max_value_dictionary(nums):
    return max(nums.values())
print(max_value_dictionary(d))