class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        start = 0
        last = len(s) - 1
        
        while start <= last:
            curr_first, curr_last = s[start], s[last]
            
            if not curr_first.isalnum():
                start += 1
            elif not curr_last.isalnum():
                last -= 1
            else:
                if curr_first.lower() != curr_last.lower():
                    return False
                start += 1
                last -= 1
        
        return True
        