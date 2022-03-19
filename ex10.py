def alphabet_index(string):
    meno = list(string.lower())
    n = []
    for x in meno:
        n.append(ord(x) - 96)
    return(str(max(n)) + chr(max(n)+96))
print(alphabet_index("Katarina"))