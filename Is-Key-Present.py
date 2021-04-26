dic={'1': 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(key):
    if key in dic:
        print("Present")
    else:
        print("Not Present")

is_key_present('1')