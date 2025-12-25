# https://leetcode.com/problems/valid-parentheses/description/


# Case 1 -> if we start with "(", output will be true only if ")" or "(" or "[" or "{"
# Case 2 -> False cases:
#           0th -> ")" "]" "}"
#           ( -> } ]  [ -> ) }  { -> ) ]
#          

class Solution:
    def isValid(self, s: str) -> bool:
        stack_contains_open_brackets = []

        bracket_pairs = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for i in s:
            if i in bracket_pairs:
                stack_contains_open_brackets.append(i)
            elif stack_contains_open_brackets:
                    last_opening_bracket = stack_contains_open_brackets.pop()
                    if i != bracket_pairs[last_opening_bracket]:
                        return False
            else:
                return False
        if stack_contains_open_brackets:
            return False

        return True
    
s = "])"

solution = Solution()
valid_parentheses = solution.isValid(s)
print(valid_parentheses)