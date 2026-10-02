class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        dig = "0123456789"
        c = ""
        for b in s:
            if b.isalpha():
                c+=b.lower()
            elif b in dig:
                c+=b
            else:
                continue


        print(c)
        return c == c[::-1]