class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] = s[i:] combina com p[j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True  # string vazia combina com padrao vazio

        # preencher de baixo para cima
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):

                # verifica se o caractere atual casa
                first_match = i < m and (p[j] == s[i] or p[j] == '.')

                # caso tenha '*' apos o padrao atual
                if j + 1 < n and p[j + 1] == '*':
                    # duas opcoes:
                    # - ignorar o "c*" ==> dp[i][j+2]
                    # - usar o caractere (se casar) ==> first_match and dp[i+1][j]
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    # caso normal: tem que casar o caractere atual
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]
