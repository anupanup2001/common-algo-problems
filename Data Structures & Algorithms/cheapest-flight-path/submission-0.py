class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_price = [math.inf]*n
        flight_price[src] = 0

        for _ in range(k + 1):
            tmp_fp = list(flight_price)
            for frm, to, price in flights:
                if flight_price[frm] == math.inf:
                    continue
                
                if price + flight_price[frm] < tmp_fp[to]:
                    tmp_fp[to] = price + flight_price[frm]
            flight_price = tmp_fp
        return flight_price[dst] if flight_price[dst] != math.inf else -1