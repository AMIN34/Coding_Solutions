"""
ou are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 
Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.


Example 2:

Input: s = "", t = "y"
Output: "y"
 

Constraints:

0 <= s.length <= 1000
t.length == s.length + 1
s and t consist of lowercase English letters.
"""

# Solution
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # return (Counter(t)-Counter(s)).popitem()[0]  # This works too
        return list((Counter(t)-Counter(s)).keys()).pop()