def firstUniqChar(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i
    return -1


s = input("Enter string: ")
print(firstUniqChar(s))
