
def reversd(s):

    s= s.strip()
    s = s.split()
    s.reverse()
    return " ".join(s)

print(reversd("This is python reversed  "))