// Problem Link: https://leetcode.com/problems/3sum
package leetcode

import "slices"

// Time: O(n^2), Space: O(n)
func threeSum(nums []int) [][]int {
	// Sort the array
	slices.Sort(nums)
	result := make([][]int, 0)
	length := len(nums)
	// Iterate through the array
	for i := 0; i < length-2; i++{
		// Check if the current element is the same as the previous element to avoid duplicates
		if i > 0 && nums[i] == nums[i-1]{
			continue
		}
		// Two pointer approach
		left, right := i + 1, length - 1
		for(left < right){
			// Calculate the sum
			sum := nums[i] + nums[left] + nums[right]
			if(sum == 0){
				// Add the triplet to the result if the sum is zero
				result = append(result, []int{nums[i], nums[left], nums[right]})
				// Move the left pointer to avoid duplicates by skipping over the same elements
				for (left < right && nums[left] == nums[left+1]){
					left++
				}
				// Move the right pointer to avoid duplicates by skipping over the same elements
				for (left < right && nums[right] == nums[right-1]){
					right--
				}
				// Move the left and right pointers
				left++
				right--
			} else if sum < 0 {
				// Move the left pointer if the sum is less than zero
				left++
			} else {
				// Move the right pointer if the sum is greater than zero
				right--
			}
		}
	}
	return result
}