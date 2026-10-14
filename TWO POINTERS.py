#Question : Two sum where pair equals  to target
#Platform : Leetcode
#Approch : Two Pointers

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         l=0
#         r=len(numbers)-1
#         while l<r:
#             sum=numbers[l]+numbers[r]
#             if sum==target:
#                 return [l+1,r+1]
#             elif sum<target:
#                 l+=1
#             else:
#                 r-=1
#         return []


# checking palindrome using two pointers
#leetcode 125

a="A man, a plan, a canal: Panama"
b=[]
for ch in a:
    if ch.isalnum():
        b.append(ch.lower())
d=0
l=0
r=len(b)-1
while l<r:
    if b[l]!=b[r]:
        d=2
    l+=1
    r-=1
if d==0:
    print('Palindrome')
else:
    print('not a Palindrome')
