def removeDuplicates(data):
    result = {}
    for key,value in data.items():
        if value not in result.values():
            result[key] = value
    print(result)
removeDuplicates(nums)