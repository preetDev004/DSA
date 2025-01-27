// Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

package leetcode

import (
	"math"
)

func maxProfit(prices []int) int {
    profit := 0
    minPrice := math.MaxInt32

    for _, currPrice := range prices{
        minPrice = min(currPrice, minPrice)
        profit = max(profit, currPrice - minPrice)
    }
    return profit
}

// Two Pointers in efficient way
// func maxProfit(prices []int) int {
//     buyDay, sellDay := 0, 1
//     profit := 0

//     for (sellDay < len(prices)){
//         fmt.Print(buyDay, sellDay)
//         buyPrice, sellPrice := prices[buyDay], prices[sellDay]
//         if (buyPrice < sellPrice){
//             currentProfit := sellPrice - buyPrice
//             if (currentProfit > profit){
//                 profit = currentProfit
//             }
            
//         } else {
//             buyDay = sellDay
//         }
//         sellDay++
        
//     }
//     return profit
// }