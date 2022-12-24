"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

stringo = 'asdfadsf'


def solution(s):
    if len(s) % 2 != 0:
        s += '_'
    odd_index = [i for i in range(len(s)) if i % 2 == 0]
    done = []
    for i in odd_index:
        done.append([s[i:i+2]])
    return done


print(solution(stringo))