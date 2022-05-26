def plus(a,b):
    return a+b

print(__name__)
if __name__ == '__main__':
    if plus(3,4) == 3+4:
        print("통과!!!!")

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
