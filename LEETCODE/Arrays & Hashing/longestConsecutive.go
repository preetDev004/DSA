// Problem Link: https://leetcode.com/problems/longest-consecutive-sequence
package leetcode


func longestConsecutive(nums []int) int{
	longest := 0
	numMap := make(map[int]bool)

	// creating a map of nums to use it as a set
	for _, num := range nums{
		numMap[num] = true	
	}
	// looping through the map/set
	for num := range numMap{
		length := 0
		// checking if the number is the start of a consecutive sequence
		if (!numMap[num - 1]){
			// finding the length of the consecutive sequence
			for(numMap[num+length]){
				length += 1
			}
			// updating longest
			if (length > longest) {longest = length}
		}
	}
	return longest
}
