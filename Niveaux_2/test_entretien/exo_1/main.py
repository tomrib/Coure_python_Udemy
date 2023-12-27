def reverse_string(str):
    r = ""
    for c in str:
        r = c + r
    return r


def reverse(s):
    return s[::-1]


print(reverse_string("bonjour tout le monde"))

s = "bonjour tout le monde"
print(reverse(s))

