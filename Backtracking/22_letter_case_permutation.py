from typing import List

def letter_case_permutation(s: str) -> List[str]:
    def backtrack(i, path):
        if i == len(s):
            res.append(path)
            return
        
        if s[i].isalpha():
            backtrack(i+1, path + s[i].lower())
            backtrack(i+1, path + s[i].upper())
        else:
            backtrack(i+1, path + s[i])
        
    res = []
    backtrack(0, "")
    return res


print(letter_case_permutation("a1b2"))