class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0;
        int end = size(s) - 1;
        while (start <= end) {
            if (!isalnum (s[start])) {
                start++;
                continue; 
            }
            if (!isalnum(s[end])){ 
                end--;
                continue;
            }
            if ((tolower(s[start])!=(tolower(s[end])))) {
                return false;
            }
            else {
                start++;
                end--;
            }
            
        }
        return true;
    }
};