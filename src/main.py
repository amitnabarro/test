#!/usr/bin/env python
# encoding: utf-8


def is_palindrome(s:str) -> bool:
    return s == s[::-1]

def longest_substring_length(s) -> int:
    if len(s) == 0:
        return 0

    used = {}
    max_length = 0
    start = 0

    for i in range(len(s)):
        if s[i] in used and start <= used[s[i]]:
            start = used[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        used[s[i]] = i
    
    return max_length

def run() -> None:
    print(is_palindrome('hello'))
    print(is_palindrome('refer'))

    print( longest_substring_length('abcabcbb') )
    print( longest_substring_length('bbbbbbb') )


if __name__ == "__main__":
    run()