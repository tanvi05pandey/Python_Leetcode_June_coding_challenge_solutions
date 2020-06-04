# Write a function that reverses a string. The input string is given as an array of characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
# Example 1:
#
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def reverseString(s):
    p1, p2 = 0, len(s)-1
    while p1 < p2:
        s[p1], s[p2] = s[p2], s[p1]
        p1 += 1
        p2 -= 1
    return s

print(reverseString(["h","e","l","l","o"]))