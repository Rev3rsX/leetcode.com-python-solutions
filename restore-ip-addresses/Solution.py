#17.02.2024 - Rev3rsX
class Solution(object):
    def restoreIpAddresses(self, s):

        def backtrack(start, path):
            if start == len(s) and len(path) == 4:
                result.append(".".join(path))
                return
            if len(path) > 4:
                return
            for i in range(1, 4):
                if start + i > len(s):
                    break
                segment = s[start:start + i]
                if (len(segment) > 1 and segment[0] == '0') or (i == 3 and int(segment) > 255):
                    continue
                backtrack(start + i, path + [segment])

        result = []
        backtrack(0, [])
        return result

