class Solution {
public:
    int lastStoneWeight(vector<int>& v) {
        while(v.size()>1){
            int max_a=0, max_b=0, a_it=0, b_it=0;
            for(int i=0; i<v.size(); i++){
                if(v[i]>max_a){
                    max_a = v[i];
                    a_it = i;
                }
            } v.erase(v.begin()+a_it);
            for(int i=0; i<v.size(); i++){
                if(v[i]>max_b){
                    max_b = v[i];
                    b_it = i;
                }
            } v.erase(v.begin()+b_it);
            v.push_back(max_a - max_b);
        }
        return v[0];
    }
};