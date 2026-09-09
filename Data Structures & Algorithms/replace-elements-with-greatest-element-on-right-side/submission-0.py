class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        previous = arr[len(arr) - 1]
        arr[len(arr) - 1] = -1
        for x in range(len(arr) - 2, -1, -1):
            now = arr[x]
            arr[x] = previous
            if now > previous:
                previous = now
        return arr


        