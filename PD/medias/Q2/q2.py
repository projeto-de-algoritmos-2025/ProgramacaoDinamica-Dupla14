class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        # dp[i][j] = True se s[i:j+1] e palindromo
        dp = [[False] * n for _ in range(n)]

        start, max_len = 0, 1

        # substrings de tamanho 1 sao palindromos
        for i in range(n):
            dp[i][i] = True

        # substrings de tamanho 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # substrings maiores que 2
        for length in range(3, n + 1):  # tamanho da substring
            for i in range(n - length + 1):
                j = i + length - 1  # fim da substring

                # condicao de palindromo:
                # - extremos iguais
                # - miolo também e palindromo
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_len:
                        start = i
                        max_len = length

        return s[start:start + max_len]
