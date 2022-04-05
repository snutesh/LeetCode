class Solution {
public:
    void reverseString(vector<char>& s) {
        int first = 0;
        int last = s.size()-1;
        char c;
        for(int i = 0; i<s.size()/2; i++)
        {
            c = s[first];
            s[first] = s[last];
            s[last] = c;
            last--;
            first++;
        }
    }
};