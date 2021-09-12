![binaryGap](./images/binary_gap.png)
# Binary Gap
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

In this tutorial we will write a python function which, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

## Algorithm
We propose to follow this simplistic steps in order to reach our goal.
Once we pass down the positive integer N to our function.
```
    1. We will convert it into a binary string
    2. Check if it contains at least 2 '1' and 1 '0'
    3. If yes
        3.1. Loop through the string of binaries
        3.2. If one is encountered we save its position
        3.3. We count the '0' (zeros)
        3.4. Once we encounter another '1' we append the length of zeros counted
        3.5. We update the counter zero
        3.6. We continue the counting from where we left (position was saved)
    4. if not
        4.1 we return 0
    5. return the longest binary gap encountered
```

## Test
We will test with N being an integer within the range [9, 15, 32, 1041].

# To find out more visit my [website](https://jmndao.herokuapp.com/jCode/613e0dcbf4f07000047057e3)
