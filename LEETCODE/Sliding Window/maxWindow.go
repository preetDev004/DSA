// Problem Link: https://leetcode.com/problems/sliding-window-maximum

package leetcode

func maxSlidingWindow(nums []int, k int) []int {
    deque := make([]int, 0, k)
    result := make([]int, 0, len(nums) - k + 1)

    for i, n := range nums {
		// If the deque is not empty and the current element is greater than the last element in the deque,
		// pop the last element from the deque
        for len(deque) > 0 && nums[deque[len(deque) - 1]] < n {
            deque = deque[:len(deque) - 1]
        }
		// Add the current element to the deque
        deque = append(deque, i)

		// we continue till we have a proper k size window
        if i < k - 1 {
            continue
        }
		// first element of the deque is the index of the maximum element (Monotonically decreasing queue)
        result = append(result, nums[deque[0]])

		// If the first element of the deque is out of the window, remove it
        if deque[0] == i - k + 1{
            deque = deque[1:]
        }
    }

    return result
}



// O(k * n)

// func maxSlidingWindow(nums []int, k int) []int {
//     l, r := 0, k
//     result := []int{}
//     for r < len(nums)+1{
//         window := nums[l:r]
//         max := slices.Max(window)
//         result = append(result, max)
//         l++; r++;

//     }
//     return result
// }
