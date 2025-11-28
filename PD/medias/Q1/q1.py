class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Usando DP com espaço otimizado (apenas uma linha)
        dp = [1] * n  # primeira linha tem apenas 1 caminho

        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]  # soma: cima + esquerda

        return dp[-1]
