class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        
        for (int i = 0; i <= matrix.size() - 1; i++) {
        int high = matrix[0].size() - 1;
        int low = 0;

        while (low <= high) {
           
            int middle = (high + low)/2;
            if (matrix[i][middle] == target){
                return true;
            }
            if (matrix[i][middle] < target ) {
                low = middle + 1 ;
            }
            if (matrix[i][middle] > target) {
                high = middle - 1;
            }
        }

       
        }
       return false; 
    }
    
};