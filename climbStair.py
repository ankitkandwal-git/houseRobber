# climbStair Dp

def f(i):
    if i == 1:
        return 1
    if i == 0:
        return 1

    left = f(i - 1)
    right = f(i - 2)

    return left + right

def main():
    n = int(input())
    print(f(n))

if __name__ == "__main__":
    main()