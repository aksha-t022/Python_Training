def max_product(nums):
    n = nums   
    mv = n[0]
    minv = n[0]
    ans = n[0]
    for i in range(1, len(n)):
        data = n[i]
        old_mv = mv
        old_minv = minv
        mv = max(data, old_mv * data, old_minv * data)
        minv = min(data, old_mv * data, old_minv * data)
        ans = max(ans, mv)
    return ans
