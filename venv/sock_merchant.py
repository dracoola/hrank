#!/bin/python3
"""
Sock Merchant
PracticeInterview Preparation KitWarm-up ChallengesSock Merchant
https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers describing the colors  of the socks in the pile.

Constraints

 where
Output Format

Return the total number of matching pairs of socks that John can sell.

Sample Input

9
10 20 20 10 10 30 50 10 20
Sample Output

3
Explanation

John can match three pairs of socks.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    my_hash = {}
    num_pairs = 0

    for indx in range(n):   # instead of range(arrlength) which arrlength == n  anyhow
        print(indx, ar[indx])
        if ar[indx] in my_hash:
            my_hash[ar[indx]] += 1
            if my_hash[ar[indx]] % 2 == 0:
                num_pairs += 1
        else:
            my_hash[ar[indx]] = 1

    #print(my_hash)
    #print("Pairs", num_pairs)
    return num_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
my_n = 9
my_array = "10 20 20 10 10 30 50 10 20"
ar = list(map(int, my_array.rstrip().split()))
print(my_array)
print(ar)

sockMerchant(my_n, ar)
'''
