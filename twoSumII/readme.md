# Two Sum II

## Problem Statement:

- Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

- Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

- The tests are generated such that there is exactly one solution. You may not use the same element twice.

- Your solution must use only constant extra space.

## Link:

[Click Here](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

## Insights

You need to store the original number which may be the complement of someother number, and not store the calculated complement, but the number, since the purpose is to find the number which is the complement.
