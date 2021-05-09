def revString(s):
    if len(s)%4==0:
        return "".join(reversed(s))
    return s

print(revString("tutsa"))