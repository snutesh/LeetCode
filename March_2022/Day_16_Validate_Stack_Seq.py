class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st=[]
        i=0
        for j in pushed:
            st.append(j)
            while len(st) >0 and st[len(st)-1] == popped[i] :
                st.pop()
                i+=1
        if len(st) == 0:
            return True
        else:
            return False