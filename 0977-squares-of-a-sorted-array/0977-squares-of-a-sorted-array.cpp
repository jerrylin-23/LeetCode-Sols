class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> Sorted(n);
        int left = 0;
        int right = nums.size() - 1;
        int pos = n - 1;
        while (left <= right) {
            if (abs(nums[left]) > abs(nums[right])) {
                Sorted[pos] = nums[left] * nums[left];
                pos--;
                left++;
            }
            else {
                Sorted[pos] = nums[right] * nums[right];
                pos--;
                right--;
            }
                

            
        }
        return Sorted;

    }
};
