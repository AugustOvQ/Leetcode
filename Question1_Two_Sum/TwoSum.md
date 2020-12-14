# Two Sum

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly\* one solution**, and you may not use the *same* element twice.

## Example

target = 9

arr = [*2*, 15, 11, *7*]

## Solution 1: Brute force

A nested for loop

### Complexity

Time: n * (n-1) = O(n^2^)
Space: 1 = O(1)

## Solution 2: Hash-map

fun through 0 to n, and store the complement of each entry

go through 0 to n again, check if the entry is in the complement

### Complexity

Time: O(n)

Space: O(n)

## Notes

In real world application, we care about memory, not storage space

Try to be comfortable to use `enumerate` as it's sometime out of comfort zone for newbies. `enumerate` comes handy in a lot of problems (I mean if you want to have a cleaner code of course). If I had to choose three built in functions/methods that I wasn't comfortable with at the start and have found them super helpful, I'd probably say `enumerate`, `zip` and `set`.

## Extra Notes

