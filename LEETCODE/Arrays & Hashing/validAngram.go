// Problem Link: https://leetcode.com/problems/valid-anagram

package leetcode

func isAnagram(s string, t string) bool {
	// check length
    if len(s) != len(t) {
        return false
     }
	
	//  create map 
    m := make([]int, 26)

	// add the charcter with count (Howmany time it appears in the first string)
    for _, v := range s {
        m[v-'a']++
    }

	// subtract the charcter with count (Howmany time it appears in the second string)
    for _, v := range t {
        m[v-'a']--

		// if negative return false 
        if m[v-'a'] < 0 {
            return false
        }
    }
    return true
}