#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hashset;
        int length = nums.size();
        for(int i = 0; i < length; i++)
        {
            if(hashset.count(nums[i]) == 0)
            {
                hashset.insert(nums[i]);
            }
            else
            {
                return true;
            }
        }
        return false;
    }
};