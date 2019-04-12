n = int(input())

phonebook = {}
for keyvalue in range(n*2):
    s1 = input()
    kv = s1.split(" ")
    if len(kv) == 2:
        phonebook[kv[0]] = kv[1]
    else:
        if kv[0] in phonebook:
            print(str(kv[0]) + "=" + phonebook[kv[0]])
        else:
            print(str(kv))