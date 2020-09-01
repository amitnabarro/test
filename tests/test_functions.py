#!/usr/bin/env python
# encoding: utf-8

from src.main import is_palindrome, longest_substring_length

def test_palindrome_method():
    assert is_palindrome('one') is False
    assert is_palindrome('kayak') is True

def test_longest_substring():
    assert longest_substring_length('aaaaaaaaa') == 1
    assert longest_substring_length('abcdaacc') == 4