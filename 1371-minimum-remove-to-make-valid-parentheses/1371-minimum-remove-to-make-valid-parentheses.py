from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # return self.ans3(s)
        return ans25(s)

    def ans1(self, s: str) -> str:
        # my atempt - very inefficient
        a = deque()
        b = deque()
        ans = []

        for i, c in enumerate(s):

            if a and c == ")" and a[-1] == "(":
                a.pop()
                b.pop()
                continue
            elif c == "(" or c == ")":
                a.append(c)
                b.append(i)

        if len(a) == 0:
            return s

        # for i,v in enumerate(b):
        # if i>=1:
        #     # v=v-b[i-1]
        #     v=v-1
        # s = s[:v] + s[v+1:]
        # s[i] = '.'
        for i, v in enumerate(s):

            if i not in b:
                ans.append(v)

        print(ans)

        return "".join(ans)

    def ans2(self, s: str) -> str:
        """My attempt at a more efficient solution - copy of ans3"""
        a = []
        x = list(s)

        for i, v in enumerate(x):

            if v == "(":
                a.append(i)
            if v == ")":
                if a:
                    a.pop()
                else:
                    x[i] = ""

        while a:
            i = a.pop()
            x[i] = ""

        return "".join(x)

    def ans3(self, s: str) -> str:
        """60 ms ans from LC"""

        if not s:
            return None

        stack = []
        char_array = list(s)

        for idx, char in enumerate(s):
            if char == ")":
                if stack:
                    stack.pop()
                else:
                    char_array[idx] = ""
            elif char == "(":
                stack.append(idx)

        while stack:
            idx = stack.pop()
            char_array[idx] = ""

        return "".join(char_array)


def ans25(s):
    """TC = n (4 loops), SC ="""
    stack = deque()
    set_brac = set()

    for i, c in enumerate(s):  # n
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                set_brac.add(i)

    invalid_idx = set_brac.union(set(stack))  # n    #important

    ans_list = []
    for i, c in enumerate(s):  # n
        if i not in invalid_idx:
            ans_list.append(c)

    return "".join(ans_list)  # n


"""
"lee(t(c)o)de)"
"a)b(c)d"
"))(("
"""
