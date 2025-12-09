# https://leetcode.com/problems/longest-common-prefix/description/

strs = ["flower","flow","flight"]
strs = ["flower","alow","blight"]
strs = ["flower","flow","flowht"]

# We stop at smallest word because prefix can never be greater than smallest word
# i = 0 --> i = len(smallest word)
# "flower"
# "flow"
# "flight"

# We keep growing our prefix, till character at the index matches
# in above example, this means we go till i = 2

# we start with assuming all characters at the index i, do not match : False
# Outcome: We want to prove that all characters matched
# when we will do one comparison:
#.    Outcome 1: True (match) --> We cannot convert False to True
#     Outcome 2: False (match). -> 

prefix_str = ""

first_word = strs[0]


for i in range(len(first_word)):
    check_for_all = True
    for current_word in strs[1:]:
        similarity_check = False        
        if i == len(current_word):
            check_for_all = False
            break
        if first_word[i] != current_word[i]:
            check_for_all = False
            break
    
    if check_for_all:
        prefix_str += first_word[i]
    else:
        break

print(prefix_str)