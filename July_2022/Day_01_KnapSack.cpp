bool sortcol(const vector<int>& v1, const vector<int>& v2)
{
    return v1[1] > v2[1];
}
class Solution {
public:
    
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        int ans=0;
        sort(boxTypes.begin(), boxTypes.end(), sortcol);
        for(int i=0; i<boxTypes.size(); i++){
            if(truckSize == 0) break;
            if(boxTypes[i][0]>truckSize){
                ans = ans + truckSize*boxTypes[i][1];
                truckSize = 0;
            }
            else {
                ans = ans + boxTypes[i][0]*boxTypes[i][1];
                truckSize = truckSize - boxTypes[i][0];
            }
        }
        return ans;
    }
};