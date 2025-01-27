// problem link: https://leetcode.com/problems/container-with-most-water

package leetcode

func maxArea(height []int) int {
    left, right := 0, len(height) - 1 
    max := 0

    for (left < right){
        w, h := right-left, 0
        if (height[left] < height[right]){
            h = height[left]
            left++
        } else {
            h = height[right]
            right--
        }

        if w*h > max{
            max = w*h
        }
    }
    return max
    
}