# -*- coding: utf-8 -*-
"""
Proudly an MIT 6.0001 grad and an MIT 6.0002 student
Thank you very much Eric Grimson, John Guttag and Ana Bell for being my teacher!
I have wanted to sit a unit from MIT since 2011, having purchased in 2011 Structure and Interpretation of Computer Programs (taught in LISP), the 1970s/80s rendition of MIT's 6.0001
And in 2014 I was on the 6.0001 OCW site to pick up `How to think like a Computer Scientist in Python` which taught me the basics of function calls and iteration
Very proudly had the world's #1 ranked Uni/College (QS) to learn to code
Charles Truscott, Byron Bay NSW, 2481

Reduction to lists of len(1)/len(2) worked out fine, don't know how I managed not to need to modulus even modulus odd lengthed lists, did this in my head, now to merge the lists and create a tabularisation after the ordering principle is applied, maybe not less than or greater than but a memo/table for what the maximum pairwise product of the two numbers is

5:20 A.M. NSW AEST Byron Bay Australia

10/10/2022, just under three days until October 13th, beginning of 6.002x via edX.org
[47]
[77, 35]
[64]
[3, 49]
[41]
[48, 32]
[60, 55]
[81]
[6, 67]
[57]
[2, 39]
[43]
[51, 5]
[43, 88]
[69]
[42, 3]
[45]
[60, 68]
[5]
[25, 10]
[70, 50]
[53]
[6, 53]
[37]
[19, 46]
[12]
[15, 59]
[5]
[29, 49]
[12]
[23, 31]
[10]
[49, 36]
[2]
[20, 2]
[8, 29]
[33]
[41, 36]
[35]
[16, 31]
[34]
[2, 9]
[6]
[33, 12]
[8]
[10, 19]
[20]
[21, 4]
[12]
[9, 15]
[4, 24]
[20]
[20, 12]
[1]
[12, 16]
[7]
[14, 2]
[12]
[8, 7]
Charles Truscott Byron Bay NSW 2481 Australia
Now need ordering identity. Certified in Python Computer Programming from MIT.
QS Globally/World Ranked #1 Higher Education Institution

[Program finished]

"""
import random

def merge_order(P=[], Q=[], R=[], S=[]):
    if len(P) > 2:
        R.append(P[:len(P)//2])
        R.append(P[len(P)//2:])
        merge_order(P[:len(P)//2], P[len(P)//2:], [], [])
    if len(Q) > 2:
        R.append(Q[:len(Q)//2])
        R.append(Q[len(Q)//2:])
        merge_order(Q[:len(Q)//2], Q[len(Q)//2:], [], [])
#    print(R)
    for x in R:
        if len(x) == 1 or len(x) == 2:
            print(x)
        

def main():
    merge_order(list(int(random.randint(1, x)) for x in range(100, 9, -1)), [], [], [])
    print("Charles Truscott Byron Bay NSW 2481 Australia")
    print("Now need ordering identity. Certified in Python Computer Programming from MIT.")
    print("QS Globally/World Ranked #1 Higher Education Institution")
if __name__ == "__main__": main()