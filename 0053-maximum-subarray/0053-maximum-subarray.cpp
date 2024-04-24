class Solution {
public:
    int maxSubArray(vector<int>& nums) {

    
    int maxSum = nums[0];
    int currentSum = nums[0];

    for (int x = 1; x <= nums.size() - 1; x++) {
        currentSum = max(nums[x], currentSum + nums[x]);
        maxSum = max(currentSum, maxSum);
        
        }
        return maxSum;    
    }

    


    
};