# Two Sum IV

## Problem

- Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

## Link

[Click Here](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

## Insights

- Same complement search is required but this time, we need to traverse the tree and save the numbers and stop as soon as we find the complement
- **`is`** checks if two references point to the same object in the memory
- **`None`** is singleton meaning there only exists a sigle instance of it in memory
- **`==`** checks for equality between two values based on their cotent, or for custom logic over-ridden in **`__eq__`** method

```
class CustomClass:
    def __eq__(self, other):
        return True  # Overrides equality to always return True

obj = CustomClass()
print(obj == None)  # Output: True (based on __eq__)
print(obj is None)  # Output: False (identity check)

```

```
# Correct way
if root is None:
    print("Root is None")

# Works but not recommended
if root == None:
    print("Root is None")

```

- Always use **`is None`** (or **`is not None`**) when checking for None
