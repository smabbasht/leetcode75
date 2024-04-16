class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Let n and m hold the lengths of the source and target strings respectively
        n,m = len(s),len(t)
        # i and j are the two pointers initiated as 0
        i = j = 0

        # While loop until pointer has reached the end for either strings traversed
        while i < n and j < m:
            # update both pointers if match else update only target pointer j
            if s[i] == t[j]:
                i += 1
            j += 1
        # If i is the same as source string length at the end of this, we've found a substring!
        return i == n
