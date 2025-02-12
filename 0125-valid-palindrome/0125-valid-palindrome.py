class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(i.lower() for i in s if i.isalnum())
        if s != s[::-1]:
            return False
        else:
            return True 
        

        