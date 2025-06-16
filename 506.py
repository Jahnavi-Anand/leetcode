class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])

        result = [""] * len(score)

        for i, (idx, _) in enumerate(sorted_scores):
            if i == 0:
                result[idx] = "Gold Medal"
            elif i == 1:
                result[idx] = "Silver Medal"
            elif i == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(i + 1)

        return result
