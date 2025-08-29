import re
from typing import List

# O(n + w) time
# O(n) space
def add_underscores(text: str, maxWidth: int) -> List[str]:
    words = []

    for word in re.sub(r"\s*-\s*", "-", text).split():
        if len(word) > maxWidth:
            parts = re.split(r'(-)', word, maxsplit=1)
            words.append(parts[0] + parts[1])
            words.append(parts[2])
        else:
            words.append(word)

    res = []
    line, chars = [], 0
    i = 0

    while i < len(words):
        # if line not complete or exceed the limit
        if chars + len(words[i]) + len(line) > maxWidth:
            res.append(fix_line(line, chars, maxWidth))
            line, chars = [], 0

        # if line has space for the word
        line.append(words[i])
        chars += len(words[i])
        i += 1
    
    res.append(fix_line(line, chars, maxWidth))

    return res


def fix_line(line, chars, maxWidth):
    extra_underscores = maxWidth - chars
    if len(line) == 1:
        underscores = extra_underscores // 2
        remainder = extra_underscores % 2
        line[0] = (
            ("_" * underscores) + line[0] + ("_" * underscores) + ("_" * remainder)
        )
    elif len(line) == 2:
        line[0] += "_" * extra_underscores
    else:
        underscores = extra_underscores // (len(line) - 1)
        remainder = extra_underscores % (len(line) - 1)
        j = 0
        while j < len(line) - 1:
            line[j] += "_" * underscores
            j += 1
        line[j] += "_" * remainder
    return "".join(line)


text1 = "cat is an animal and so is a dog"
text2 = "hello      world"
text3 = "Human"
text4 = "auto-complete is my go    -    to"


print(add_underscores(text1, 12))
print(add_underscores(text2, 8))
print(add_underscores(text3, 8))
print(add_underscores(text4, 8))
