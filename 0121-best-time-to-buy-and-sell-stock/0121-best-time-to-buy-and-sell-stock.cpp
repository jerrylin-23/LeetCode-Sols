class Solution {
public:
    int maxProfit(const std::vector<int>& prices) {
        if (prices.empty()) return 0; // Handle edge case where prices vector might be empty

        int minPrice = prices[0];
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;  // Update the minimum price found so far
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;  // Update the maximum profit if current profit is higher
            }
        }
        return maxProfit;
    }
};