// Problem Link: https://leetcode.com/problems/two-sum

package leetcode

func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int)

	for i, num := range nums{
		ele := target - num
		if j, ok := numMap[ele]; ok {
			return []int{j, i}
		}
		numMap[num] = i
	}
	return []int{}
}
