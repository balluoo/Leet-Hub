class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count=0
        result = False
        for x in arr:
            if x%2 != 0:
                count +=1
                if count == 3:
                    result = True
                    return result
            else:
                count = 0
        return result