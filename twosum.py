def twosum(num, target):
    x = 0
    n = len(num)
    
    while x < n:
        z = x + 1
        while z < n:
            if num[x] + num[z] == target:
                return [x, z]
            z += 1
        x += 1
    
    return []

n = [2, 7, 13, 15]
print(twosum(n, 9))
