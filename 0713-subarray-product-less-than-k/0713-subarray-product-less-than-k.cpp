class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
      
        if (k <= 1) {
            return 0;
        }
        int count = 0;
        int product = 1;
        int left = 0;
        for (int i = 0; i < nums.size(); i++) {
            product *= nums[i];
            while (product >= k) {
                    product /= nums[left++];
            }
            count += (i - left + 1);
        }
        return count;
    }
};