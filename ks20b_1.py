t = int(input())
for x in range(1 , t + 1) :
    n = int(input())
    a = list(map(int , input().split()))
    y = 0
    for i in range(1 , n - 1) :
        if a[i] > a[i - 1] and a[i] > a[i + 1] :
            y += 1
    print('Case #{}: {}'.format(x , y))
