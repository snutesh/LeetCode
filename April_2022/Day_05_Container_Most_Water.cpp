class Solution {
public:
    int maxArea(vector<int>& height) {
        int left=0, right=height.size()-1, max_area=0, area=0, h=0, w=0;
        while(left<right)
        {
            h = min(height[left],height[right]);
            w = right-left;
            area = h*w;
            max_area = max(max_area,area);
            
            if(height[left]>height[right]) right--;
            else if(height[left]<height[right]) left++;
            else {
                left++;
                right--;
            }
        }
        return max_area;
    }
};