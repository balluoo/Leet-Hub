class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        res = ""
        h = [ (-ord(x), y) for x, y in Counter(s).items() ]
        heapq.heapify(h)
        while h:
            x, y = heapq.heappop(h)
            while y > repeatLimit and h: 
                res += chr(-x) * repeatLimit
                y -= repeatLimit
                a, b = heapq.heappop(h)
                res += chr(-a)
                if (b-1) > 0: heapq.heappush(h, (a, b-1))
            res += chr(-x) * min(y, repeatLimit)
        return res