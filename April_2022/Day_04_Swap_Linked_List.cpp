/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        int len = 0, c = 0;
        ListNode* temp = head;
        while(temp)
        {
            len++;
            temp = temp->next;
        }
        temp = head; ListNode* temp2 = head;
        for(int i=1; i<k; i++)
        {
            temp = temp->next;
        }
        for(int i=0; i<len-k; i++)
        {
            temp2 = temp2->next;
        }
        c = temp->val;
        temp->val = temp2->val;
        temp2->val = c;
        return head;
    }
};