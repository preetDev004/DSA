// Problem Link: https://leetcode.com/problems/minimum-window-substring
package leetcode

import "math"
func minWindow(s string, t string) string {
    l,r, startIdx := 0,0,-1
    count := len(t)
    tMap := make(map[byte]int)
    minLen := math.MaxInt32

    for _, ch := range t{
        tMap[byte(ch)]++
    }

    for r < len(s){
        if tMap[s[r]] > 0{
            count--
        }
        tMap[s[r]]--
        r++

        for count == 0 {
            if r - l < minLen{
                minLen = r - l
                startIdx = l
            }
            if tMap[s[l]] == 0 {
                count++
            }
            tMap[s[l]]++
            l++
        }
    }

    if startIdx == -1{
        return ""
    }

    return s[startIdx : minLen+startIdx]
}