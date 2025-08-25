import pandas as pd


def longest_common_subsequence(list_a, list_b):
    m = len(list_a)
    n = len(list_b)

    # Создаем таблицу для хранения длины LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Заполняем таблицу
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if list_a[i - 1] == list_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Создаем DataFrame для наглядного отображения таблицы dp
    dp_df = pd.DataFrame(dp)
    print("Таблица dp:")
    print(dp_df)

    # Возвращаем длину наибольшей общей подпоследовательности
    return dp[m][n]


list_a = [1, 2, 3, 4, 5]
list_b = [2, 4, 6, 8, 10]

ex = longest_common_subsequence(list_a, list_b)
print(ex)