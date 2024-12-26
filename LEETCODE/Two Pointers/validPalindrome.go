// Problem Link: https://leetcode.com/problems/valid-palindrome
package leetcode

import (
	"unicode"
)

// isAlphanumeric checks if a rune is a letter or digit
func isAlphanumeric(r rune) bool{
	return unicode.IsLetter(r) || unicode.IsDigit(r)
}
func isPalindrome(s string) bool{
	left := 0
	right := len(s) - 1

	for (left < right){
		// Skip non-alphanumeric characters from both ends
		for (left < right && !isAlphanumeric(rune(s[left]))){
			left++
		}
		for (left < right && !isAlphanumeric(rune(s[right]))){
			right--
		}
		// Compare the characters at the ends of the string
		if (unicode.ToLower(rune(s[left])) != unicode.ToLower(rune(s[right]))){
			return false
		}
		left++
		right--
	}
	return true
}