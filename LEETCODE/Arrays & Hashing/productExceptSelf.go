package leetcode

func productExceptSelf(nums []int) []int {
    length := len(nums)
    result := make([]int, length)
	// Initialize result with all elements as 1
    for i := range result{
        result[i] = 1
    }
	// Left to Right update result
    prod := 1
    for i := 0; i < length; i++{
        result[i] *= prod
        prod *= nums[i]
    }
	// Right to Left update result
    prod = 1 
    for i := length - 1; i >= 0; i--{
        result[i] *= prod
        prod *= nums[i]
    }
    return result
}