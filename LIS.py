# Находим самую длинную подпоследовательность в списке

def longest_increasing_subsequence(list_a):
    n = len(list_a)

    dp = [1] * n   # так как последовательность начинается с цифры 1

    for i in range(1, n):
        for j in range(i):
            if list_a[i] > list_a[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


ex = [10, 34, 3, 5, 6, 56, 87, 2, 16]

