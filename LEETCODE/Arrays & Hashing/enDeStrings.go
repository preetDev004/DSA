// Problem Link: https://leetcode.com/problems/encode-and-decode-strings/
package leetcode

import (
	"strconv"
	"strings"
)

// encodes ["leet", "code", "love", "you"] to 4leet4code4love3you 
func encode(strs []string) string {
	var builder strings.Builder
	for _, str := range strs {
		builder.WriteString(strconv.Itoa(len(str)))
		builder.WriteString(str)
	}
	return builder.String()
}

// decodes 4leet4code4love3you to ["leet", "code", "love", "you"]
func decode(str string) []string{
	var strs []string
	newStr := str
	end := int(newStr[0] - '0')
	for(end != 0){
		strs = append(strs, newStr[1:end+1])
		newStr = newStr[end+1:]
		if len(newStr) == 0 {
			end = 0
			continue
		}
		end = int(newStr[0] - '0')
	}
	return strs
}
