// Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

package leetcode

func lengthOfLongestSubstring(s string) int {
    longest := 0
    charMap := make(map[rune]int)
    pointer := 0

    for i, ch := range s{
        if _, ok := charMap[ch]; !ok && charMap[ch] >= pointer{
            pointer = charMap[ch] + 1
        }
        charMap[ch] = i
        longest = max(longest, i - pointer + 1)
    }
    return longest
}