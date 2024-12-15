// problem link: https://leetcode.com/problems/group-anagrams/

package leetcode

import (
	"sort"
)
func sortString(s string) string{
	// create slice of bytes
	b := []byte(s)
	// sort bytes with less function
	sort.Slice(b, func(x int, y int) bool{
		return b[x] < b[y]
	})
	// return sorted bytes again as string
	return string(b)
}

func groupAnagrams(strs []string) [][]string{
	// create map of sorted strings
	strMap := make(map[string][]string)
	// loop through each string
	for _, str := range strs{
		// sort string
		sortedStr := sortString(str)

		// add sorted string to map as key with original string and append other strings,
		// only if their sorted string match the key.
		strMap[sortedStr] = append(strMap[sortedStr], str)
	}
	// convert map to array
	var result [][]string
	for _, val := range strMap{
		result = append(result, val)
	}
	return result
}
