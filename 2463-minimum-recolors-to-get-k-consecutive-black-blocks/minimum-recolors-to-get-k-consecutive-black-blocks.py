class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = blocks[:k]
        count = w.count("W")
        minimum = count

        for i in range(k,len(blocks)):

            if blocks[i] == "W":
                count +=1 
            if blocks[i -k] =="W":
                count -= 1
           
            minimum = min(count,minimum)

        return minimum