# Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

**Note:**
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



# Solution 1:

The official solution is pop from a list

```cpp
//pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;
```



# Solution 2:

Reverse a string, The condition check can be optimised further, see bit length solution