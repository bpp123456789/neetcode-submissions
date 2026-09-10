class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        length = 0
        count = 0
        for x in range(0,len(operations)):
            if operations[x] == "+":
                score.append(score[length - 1] + score[length - 2])
                length += 1
                count += score[length - 1]
            elif operations[x] == "D":
                score.append(score[length -1 ] * 2)
                length += 1
                count += score[length - 1]
            elif operations[x] == "C":
                num = score.pop()
                count -= num
                length -= 1
            else:
                score.append(int(operations[x]))
                length += 1
                count += score[length - 1]
        return count

        