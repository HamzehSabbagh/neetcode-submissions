class Solution {
public:
    bool isAnagram(string s, string t) {
        #include <unordered_map>

        unordered_map <char, int> hashmap;

        if ( s.length() < t.length() || t.length() < s.length())
        {
            return false;
        }
        for (int i = 0; i < s.length(); i++)
        {
            if (hashmap.find(s[i]) == hashmap.end())
            {
                hashmap[s[i]] = 1;
            }
            else
            {
                hashmap[s[i]] += 1;
            }
        }
        for (int i = 0; i < t.length(); i++)
        {
            if (hashmap.find(t[i]) == hashmap.end() or hashmap[t[i]] == 0)
            {
                return false;
            }
            else
            {
                hashmap[t[i]] -= 1;
            }
        }

        return true;
    }
};
