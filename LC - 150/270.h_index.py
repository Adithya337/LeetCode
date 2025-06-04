class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # TC - O(N) ; SC - O(N)
        '''
        n = len(citations)
        paper_counts = [0]*(n + 1)
        for i in range(len(citations)):
            paper_counts[min(n,citations[i])] += 1
        h = n
        papers = paper_counts[n]

        while papers < h:
            h -= 1
            papers += paper_counts[h]
        return h
        '''
        # TC - O(N^2) ; SC - O(1)
        n = len(citations)
        h = 1
        for i in range(n):
            paper_count = 0
            for j in range(n):
                if citations[j] >= h:
                    paper_count += 1
                if paper_count == h:
                    h += 1
                    break
        return h - 1

    



'''
citations = [3,0,6,1,5] , o/p : 3
citations = [1,3,1] ,o/p : 1
'''