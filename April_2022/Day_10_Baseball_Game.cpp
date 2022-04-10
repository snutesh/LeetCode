class Solution {
public:
    int calPoints(vector<string>& ops) {
        stack<int> stack; int a, b, sum = 0;

        for(auto value : ops)
        {
            if(value=="C")
            {
                stack.pop();
            }
            else if(value=="D")
            {
                stack.push(stack.top()*2);
            }
            else if(value=="+")
            {
                a = stack.top();
                stack.pop();
                b = a + stack.top();
                stack.push(a);
                stack.push(b);
            }
            else
            {
                stack.push(stoi(value));
            }
        }

        while(!stack.empty())
        {
            sum+=stack.top();
            stack.pop();
        }

        return sum;
    }
};