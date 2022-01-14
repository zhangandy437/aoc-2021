def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

nums = input("/Users/andyzhang/Documents/sandbox/python/adventofcode2021/Day3/in.txt")

n = len(nums)

def finditOne(arr):
    print(arr[0])
    for i in range(len(arr[0])):
        m, n = [num for num in arr if num[i] == '1'], [num for num in arr if num[i] == '0']
        arr = m if len(m) >= len(n) else n
        if len(arr) == 1: return arr[0]
    return arr[0]

def finditZero(arr):
    print(arr[0])
    for i in range(len(arr[0])):
        m, n = [num for num in arr if num[i] == '1'], [num for num in arr if num[i] == '0']
        arr = n if len(n) <= len(m) else m
        if len(arr) == 1: return arr[0]
    return arr[0]

def strbin(bin):
    print(bin)
    bin = bin[::-1]
    ans = 0
    for i in range(len(bin)):
        if bin[i] == '1':
            ans |= 1 << i
    return ans

oxygen = strbin(finditOne(nums))
cotwo = strbin(finditZero(nums))

print(oxygen, cotwo, oxygen * cotwo)