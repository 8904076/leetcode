class Solution:
    def romanToInt(self, s: str) -> int:
        ref = { "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000,
                }
        if not s:
            return 0 
        res = ref[s[0]]
        for i in range(1,len(s)):
            prev = s[i-1]
            cur = s[i]
            if prev and ref[prev]<ref[cur]:
                res +=(ref[cur]- 2*ref[prev])
            else:
                res +=ref[cur]
        return res