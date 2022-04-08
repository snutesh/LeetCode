class KthLargest {
public:
    priority_queue <int, vector<int>, greater<int>> pq;
    int K;
    KthLargest(int k, vector<int>& nums) {
        K = k;
        for(int i=0; i<nums.size(); i++)
        {
            pq.push(nums[i]);
        }
    }
    
    int add(int val) {
        pq.push(val);
        int N = pq.size();
        for(int i=0; i<(N-K); i++)
        {
            pq.pop();
        }
        return pq.top();
    }
};