class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> Result;
        set<vector<int>> s;
        for (int i = 0; i < nums.size() ; i++ ) {
            int m = i + 1;
            int j = nums.size() - 1;
            while (m < j) {
                int sum = nums[i] + nums[m] + nums[j];
                if (sum == 0){
                    s.insert({nums[i],nums[m],nums[j]});
                    m++;
                    j--;
                }
                else if (sum < 0) {
                    m++;
                }
                else{
                      j--;
                }
            }

        }
        for (auto allTriplets : s) 
            Result.push_back(allTriplets);
        return Result;
        

    }
};