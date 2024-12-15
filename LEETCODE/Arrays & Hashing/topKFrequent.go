// problem link: https://leetcode.com/problems/top-k-frequent-elements/description/

package leetcode

func topKFrequent(nums []int, k int) []int {
	freqMap := make(map[int]int)
	for _, num := range nums {
		freqMap[num]++
	}
	freqNums := make([][]int, len(freqMap))

	for num, freq := range freqMap {
		freqNums[freq] = append(freqNums[freq], num)
	}

	var result []int
	for i := len(freqNums) - 1; i >= 0; i-- {
		result = append(result, freqNums[i]...)
		if len(result) >= k{
			return result
		} 
	}

	return result
}
