class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        #include <unordered_map>
        unordered_map<int, int> hashmap;

        for (int i = 0; i < nums.size(); i++)
        {
            int val = target - nums[i];
            if (hashmap.find(val) != hashmap.end())
            {
                return {hashmap[val], i};
            }
            hashmap[nums[i]] = i;
        }
    }
};
