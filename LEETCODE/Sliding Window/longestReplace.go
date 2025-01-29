// Problem Link: https://leetcode.com/problems/longest-repeating-character-replacement

package leetcode

func characterReplacement(s string, k int) int {
    longest := 0
    start := 0
    maxFreq := 0
    charMap := [26]int{}

    for r, ch := range s {
        charMap[ch - 'A']++
        maxFreq = max(maxFreq, charMap[ch - 'A'])
        if ((r-start+1) - maxFreq > k){
            charMap[s[start] - 'A']-- 
            start++
        }
        longest = max(longest, r-start+1)      
    }
	
    return longest

}