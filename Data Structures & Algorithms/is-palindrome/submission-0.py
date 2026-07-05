class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum())
        clean = clean.lower()
        clean2 = clean[::-1].lower()
        return clean == clean2