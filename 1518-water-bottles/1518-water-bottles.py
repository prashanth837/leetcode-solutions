class Solution:
    def numWaterBottles(self, num: int, numEx: int) -> int:
        empty=num
        count=num
        while empty>=numEx:
            full=empty//numEx
            count+=full
            empty=empty%numEx
            empty+=full
        return count
        