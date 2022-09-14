def f(n, b): return f(n//b, b) + (str(n%b) if n % b < 10 else chr(55 + n%b)) if n > 0 else ""

def ff(x):
    x = list(x)
    fibs = [1]*(len(x)+1)
    for i in range(2, len(x)+1): fibs[i] = fibs[i-1] + fibs[i-2]
    return sum(fibs[len(x) - i - 1] for i in range(len(x)) if x[i] == "1")

def tf(x):
    fibs = [1]*(x+1)
    for i in range(2, x+1): fibs[i] = fibs[i-1] + fibs[i-2]
    a = []
    c = False
    t = x

    for j in range(t+1):
        if x >= fibs[t - j]:
            a += [1]
            x -= fibs[t - j]
            c = True
        elif c: a += [0]
    
    return "".join(map(str, a))

print(ff(tf(75)))