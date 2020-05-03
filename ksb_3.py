t = int(input())
m = 10 ** 9

def cal(s) :
    c = 0
    for i in range(len(s)) :
        if s[i] == '(':
            c += 1
        if s[i] == ')':
            c -= 1
        if c == -1:
            return i
    return -1
        
def decode(s) :
    w = h = 0
    i = 0
    while i < len(s) :
        if s[i] == 'N' :
            h -= 1
        if s[i] == 'S' :
            h += 1
        if s[i] == 'W' :
            w -= 1
        if s[i] == 'E' :
            w += 1
        if s[i].isnumeric() :
            f = int(s[i])
            j = i + 2 + cal(s[i + 2::])
            r = decode(s[i + 2 : j :])
            w += f * r[0]
            h += f * r[1]
            i = j
        i += 1
    return w % m , h % m

for x in range(1 , t + 1) :
    r = decode(input())
    w = r[0] + 1
    h = r[1] + 1
    if w <= 0 :
        w += m
    if h <= 0 :
        h += m
    print('Case #{}: {} {}'.format(x , w , h))
