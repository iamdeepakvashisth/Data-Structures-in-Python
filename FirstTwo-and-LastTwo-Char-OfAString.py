#first 2 and the last 2 chars of a string
a="ydddddddsldjwlkkkkkdjwqxw"

def new_string(nums):
    if len(nums)<4:
        return ""
    return nums[:2]+nums[-2:]
new_string(a)