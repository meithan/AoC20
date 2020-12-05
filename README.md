# AoC20

My solutions for [Advent of Code 2020](https://adventofcode.com/2020). In Python 3.

I'll be updating this as a sort of mini blog whenever I can, commenting on the daily problems.

You can also check out our fancy [custom private leaderboard](https://meithan.net/AoC20/), with medals awarded to the fastest solvers. See (and download/fork!) the project [here](https://github.com/meithan/AoCBoard).

___

**Day 5**: [Binary Boarding](https://adventofcode.com/2020/day/5)

28m 50s (#5221) / 33m 28s (#4336) - [code](https://github.com/meithan/AoC20/blob/main/day05.py)

It is straightforward to simply code the [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) process described in the problem. Careful with a possible [off-by-one error](https://en.wikipedia.org/wiki/Off-by-one_error) in how the bounds are updated.

However a smarter solution is realizing that this process is really just [counting in binary](https://en.wikipedia.org/wiki/Binary_number#Counting_in_binary). Each bit represents a partition into halves, with the rightmost bits corresponding to larger partitions. For instance, for the left-right column selection we have:

<pre>      L--             L--
  LL-     LR-     RL-     RR-
LLL LLR LRL LRR RLL RLR RRL RRR
000 001 010 011 100 101 110 111
 0   1   2   3   4   5   6   7</pre>

So simply replacing L by 0 and R by 1 (and F by 0 and B by 1 for the rows), and converting the resulting binary number into decimal also (e.g. `int("0101100", 2)`) yields the correct row or column.

I started this one about 20 minutes late, so I only got 2nd place on our [private leaderboard](https://meithan.net/AoC20). Oh well.

___

**Day 4**: [Passport Processing](https://adventofcode.com/2020/day/4)

7m 31s (#759) / 22m 29s (#579) - [code](https://github.com/meithan/AoC20/blob/main/day04.py)

The kind of string matching problem for which [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) ("regexes") were invented (and Python has a nice [regex module](https://docs.python.org/3/library/re.html)). It was a nice little regex practice; I did have to look a couple of things up on the web. [regexr](https://regexr.com/) is an incredibly useful resource for that!

___

**Day 3**: [Toboggan Trajectory](https://adventofcode.com/2020/day/3)

4m 23s (#483) / 6m 39s (#295) - [code](https://github.com/meithan/AoC20/blob/main/day03.py)

Another easy one. Careful with mixing up the meaning of rows and column in these arrays. And there's no need to actually extend the "forest" to the right, one can simply take the x coordinate modulo the number of columns (using the [modulo operator](https://python-reference.readthedocs.io/en/latest/docs/operators/modulus.html) `%`) to effectively make the array wrap around to the right.

Not fast enough to make the top 100 on either star :/.
___

**Day 2**: [Password Philosophy](https://adventofcode.com/2020/day/2)

2m 47s (#130) / 4m 02s (**#69!**) - [code](https://github.com/meithan/AoC20/blob/main/day02.py)

An easy one ... and I made the top 100 for the second star! Which put me on the global leaderboard! Yay! These are my first ever leaderboard points. And probably the only time I'll be on the global leaderboard (keeping expections low here).

Python's great string manipulation methods (like [split](https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split) and [strip](https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip)) contributed to coding the solution quickly. Also note that the bit-wise [xor](https://en.wikipedia.org/wiki/Exclusive_or) operator `^` acts as a *logical* xor when applied to booleans (a not very well documented feature) -- much shorter than writing the same using `and`, `or` and `not`.

___

**Day 1**: [Report Repair](https://adventofcode.com/2020/day/1)

7m 08s (#293) / 8m 06s (#283) - [code](https://github.com/meithan/AoC20/blob/main/day01.py)

I coded the solution to Part 1 in just 2 minutes ... But everyone submitting at the same time [overloaded the AWS instances](https://www.reddit.com/r/adventofcode/comments/k4ejjz/2020_day_1_unlock_crash_postmortem/) AoC runs on! So I could only submit my answer to Part 1 (and unlock Part 2) after waiting for several minutes. As a result [Eric Wastl](http://was.tl/), the creator of AoC, invalidated the leaderboard for this puzzle.

Day 1 is always just a warm-up. The input was short enough that a brute-force check of all pairs and triples looking for the combinations adding up to 2020 did the job. Python lets us do this without using array indices, instead iterating over the elements directly. Isn't that idiomatic!

*A more efficient solution*

This solution works in a reasonable time because the list of numbers is short (200). But if the list had a million numbers it would be a different story. The current brute-force check-all-combinations is O(n^2) for Part 1 and O(n^3) for Part 2. Can we do better?

Sure! Here's a [faster solution](https://github.com/meithan/AoC20/blob/main/day01_fast.py).

On a first pass we load all the numbers in a Python [set](https://docs.python.org/3/library/stdtypes.html#set). This is a data structure that stores items in no particular order (unlike a list) and implements a [hash table](https://en.wikipedia.org/wiki/Hash_table) for quick lookups. The upshot is that asking whether some item is contained or not in the set is an O(1) operation (on average) -- that is, the time it takes does not grow with the number of items in the set, so it doesn't matter if it has 200 or 1 million items in it. Using a list or tuple you have to check all the elements one by one, and that is O(n). Even if you did binary search in a previously sorted list that would be O(log(n)) -- nothing beats O(1).

Then, on a second pass, for every number x in the list we check whether y = 2020 - x is in the set. If it is, then x + y = x + (2020 - x) = 2020 and we've found the answer. If the set lookups are O(1) then this second pass is O(n). Adding that to the O(n) of the first pass, the total running time is O(2*n) ~ O(n). A much more efficient algorithm than brute-force!

For Part 2 we need to iterate twice over the numbers, instead of thrice, and then leverage the set. For every pair of numbers x and y (with x != y), we ask whether z = 2020 - x - y is in the set. If it is, then we have our answer. This solution is O(n^2) instead of O(n^3). Still a great speed-up if the list is large!
