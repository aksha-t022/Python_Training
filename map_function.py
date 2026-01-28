l1=[1,2,3,4,5,6]

'''ans = map(lambda x: x+x , l1)
for v in ans:
    print(v)
print(ans,end = " ")'''

ans = filter(lambda x: not(x%2), l1)
print(list(ans))