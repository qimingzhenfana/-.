import random

print("请输入数组长度")
N = int(input())
arr = [0] * N
for i in range(len(arr) - 1):
    arr[i] = i + 1
# 最后一个数是随机数
arr[len(arr) - 1] = random.randint(1, len(arr))
# 为随机数设置随机下标
index = random.randint(0, N)
# 将最后一位和相应下标对应位置的数字互换
arr[len(arr) - 1], arr[index] = arr[index], arr[len(arr) - 1]
random.shuffle(arr)
print("原数组为：", arr)
x = 0
for i in range(1, N):
    x = x ^ i
for i in range(N):
    x = x ^ arr[i]
print("重复的数是：", x)
