'''
https://leetcode.com/problems/valid-anagram/
'''

class Solution:
    def isAnagram(self, s, t):
        s_dic={}
        t_dic={}
        for i in s:
            if i in s_dic:
                s_dic[i] += 1
            else:
                s_dic[i]=1
        for i in t:
            if i in t_dic:
                t_dic[i] += 1
            else:
                t_dic[i]=1
        return s_dic==t_dic


s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s,t))
print(sol.isAnagram("car","rat"))
print(sol.isAnagram("car","raac"))

