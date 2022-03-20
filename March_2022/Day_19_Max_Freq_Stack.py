# class FreqStack:

#     def __init__(self):
#         self.stack = []
#         self.count = {}

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if val in self.count:
#             self.count[val] += 1
#         else:
#             self.count[val] = 1
#         # print(self.stack)
#         # print(self.count)

#     def pop(self) -> int:
#         # value = max(self.count, key = self.count.get)
#         max_keys = [key for key, value in self.count.items() if value == max(self.count.values())]
#         print(max_keys)
#         i = len(self.stack)
#         while(i>0):
#             i-=1
#             if self.stack[i] in max_keys:
#                 break
#         value = self.stack.pop(i)
#         self.count[value] -= 1
#         return value
# =======================================================================
# Above Code works but gives TLE
# =======================================================================
class FreqStack:

    def __init__(self):
        self.stack = defaultdict(list)
        self.count = defaultdict(int)
        self.max_ = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.max_ = max(self.max_, self.count[val])
        self.stack[self.count[val]].append(val)

    def pop(self) -> int:
        val = self.stack[self.max_].pop()
        self.count[val] -= 1
        if not self.stack[self.max_]:
            self.max_ -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()