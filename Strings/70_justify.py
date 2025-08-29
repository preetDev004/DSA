from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, chars = [], 0
        i = 0
        
        while i < len(words):
            # no space in line
            if chars + len(line) + len(words[i]) > maxWidth:
                extra_spaces = maxWidth - chars
                spaces = extra_spaces // max(1, len(line) - 1)
                reminder = extra_spaces % max(1, len(line) - 1) # if odd spaces

                # at least one sapce is needed
                for j in range(max(1, len(line)-1)):
                    line[j] += ' ' * spaces
                    if reminder:
                        line[j] += ' '
                        reminder -= 1

                res.append(''.join(line))
                line, chars = [], 0

            # space in line (add word move to the next word)
            line.append(words[i])
            chars += len(words[i])
            i += 1

        # last line needs to be handle
        last_line = ' '.join(line)
        chars = len(last_line)
        res.append(last_line + (' ' *  (maxWidth - chars)))

        return res