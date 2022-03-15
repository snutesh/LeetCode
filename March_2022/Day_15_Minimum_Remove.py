class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count_open = 0
        count_close = 0
        result = ''
        for ch in s:
            if ch == '(':
                count_open += 1
            if ch == ')':
                count_close += 1
            if count_open < count_close :
                count_close -= 1
            else :
                result = result + ch
        
        s = result
        count_open = 0
        count_close = 0
        result = ''
        for ch in reversed(s):
            if ch == '(':
                count_open += 1
            if ch == ')':
                count_close += 1
            if count_open > count_close :
                count_open -= 1
            else :
                result = ch + result
                
        return result