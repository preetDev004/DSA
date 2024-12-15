// Problem Link: https://leetcode.com/problems/contains-duplicate

package leetcode

func containsDuplicate(nums []int) bool {
    numMap := make(map[int]bool)

    for _, num := range nums{
        if numMap[num]{
            return true
        }
        numMap[num] = true
    }
    return false
}

