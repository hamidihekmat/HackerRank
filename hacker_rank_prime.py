def prime(n):
    prime_number = [1,3,5,7,9]
    for i in prime_number:
        if len(n) > 1:
            if n[-1] == i:
                return "Prime"
        elif n[0] == i:
            return "Prime"
        else:
            return "Not prime"
        
n = int(input())
for i in range(n):
    s = input()
    print(prime(s))