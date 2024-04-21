class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;

        for (string& str : strs){
            string count(26,0);

            for (char x : str){
                count [x - 'a']++;
            }
            groups[count].push_back(str);
        }
        vector<vector<string>> result;
        for (auto& group : groups) {
            result.push_back(group.second);
        }

        return result;
    }
};