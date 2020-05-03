t = int(input())
for x in range(1 , t + 1) :
    n , d = map(int , input().split())
    X = list(map(int , input().split()))
    for i in X[ : : -1 ] :
        y = i * ( d // i )
        d = y
    print('Case #{}: {}'.format( x , y ))
