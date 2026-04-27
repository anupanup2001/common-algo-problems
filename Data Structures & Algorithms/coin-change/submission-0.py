from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(amt: int):
            if amt == 0:
                return 0
            if amt < 0:
                return -1
            num_coins = math.inf
            for coin in coins:
                n = dp(amt - coin)
                if n == -1:
                    continue
                num_coins = min(num_coins, n)
            return num_coins + 1 if num_coins != math.inf else -1
        
        return dp(amount)