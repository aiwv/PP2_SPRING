n = int(input())
s = list(input())
for i in range(len(s)):
    s[i] = chr(ord(s[i]) + (n % 26))
    if ord(s[i]) > 90:
        s[i] = chr(64 + ord(s[i]) - 90)

print (*s, sep='')