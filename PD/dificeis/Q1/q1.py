class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                # Caso 1: "()" simples
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                else:
                    # Caso 2: "))" mas pode fechar algo
                    prev = i - dp[i-1] - 1
                    if prev >= 0 and s[prev] == '(':
                        dp[i] = dp[i-1] + 2
                        if prev - 1 >= 0:
                            dp[i] += dp[prev-1]

                max_len = max(max_len, dp[i])

        return max_len
