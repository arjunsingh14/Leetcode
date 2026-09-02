# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return mergeHelper(0, len(pairs) - 1, pairs)

def mergeHelper(s, e, arr):
    if e - s + 1 <= 1:
        return arr

    m = (e + s) // 2
    
    mergeHelper(s, m, arr)
    mergeHelper(m + 1, e, arr)

    merge(s, e, m, arr)
    
    return arr
    
def merge(s, e, m, arr):
    L = arr[s : m + 1]
    R = arr[m + 1: e + 1]
    i, j, k = 0, 0, s

    while i < len(L) and j < len(R):
        if L[i].key <= R[j].key:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        

        