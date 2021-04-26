def generate_dic(n):
    d = dict()
    for x in range(1,n+1):
        d[x]=x*x
    return d

#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).