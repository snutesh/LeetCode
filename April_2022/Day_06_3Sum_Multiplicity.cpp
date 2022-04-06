class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        int n = arr.size(), res = 0;
        unordered_map<int, int> map;
        for(int i=0; i<n; i++)
        {
            res = (res + map[target - arr[i]]) % 1000000007;
            for(int j=0; j<i; j++) map[arr[i] + arr[j]]++;
        }
        return res;
    }
};