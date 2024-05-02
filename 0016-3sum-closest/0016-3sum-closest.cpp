class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        vector<int> triplet;
        int close = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < nums.size(); i++) {
            int m = i + 1;
            int j = nums.size() - 1;
            while (m < j) {
                int sum = nums[i] + nums[m] + nums[j];
                if (abs(target - close) > abs(target - sum)) {
                    close = sum;
                    
                }
                if (sum > target) {
                    j--;
                }
                else {
                    m++;
                }
            }
        }
        return close;
    }
};