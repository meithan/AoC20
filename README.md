# AoC20

My solutions for [Advent of Code 2020](https://adventofcode.com/2020). In Python 3.

I'll be updating this as a sort of mini blog whenever I can, commenting on the daily problems.

You can also check out our fancy [custom private leaderboard](https://meithan.net/AoC20/), with medals awarded to the fastest solvers. See (and download/fork!) the project [here](https://github.com/meithan/AoCBoard).
___

**Day 3**: Toboggan Trajectory

4m 23s (#483) / 6m 39s (#295) - [code](https://github.com/meithan/AoC20/blob/main/day03.py)

Another easy one. Careful with mixing up the meaning of rows and column in these arrays. And there's no need to actually extend the "forest" to the right, one can simply take the x coordinate modulo the number of columns (using the [modulo operator](https://python-reference.readthedocs.io/en/latest/docs/operators/modulus.html) `%`) to effectively make the array wrap around to the right.

Not fast enough to make the top 100 on either star :/.
___

**Day 2**: Password Philosophy

2m 47s (#130) / 4m 02s (**#69!**) - [code](https://github.com/meithan/AoC20/blob/main/day02.py)

An easy one ... and I made the top 100 for the second star! Which put me on the global leaderboard! Yay! These are my first ever leaderboard points. And probably the only time I'll be on the global leaderboard (keeping expections low here).

Python's great string manipulation methods (like [split](https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split) and [strip](https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip)) contributed to coding the solution quickly. Also note that the bit-wise [xor](https://en.wikipedia.org/wiki/Exclusive_or) operator `^` acts as a *logical* xor when applied to booleans (a not very well documented feature) -- much shorter than writing the same using `and`, `or` and `not`.

___

**Day 1**: Report Repair

7m 08s (#293) / 8m 06s (#283) - [code](https://github.com/meithan/AoC20/blob/main/day01.py)

I coded the solution to Part 1 in just 2 minutes ... But everyone submitting at the same time [overloaded the AWS instances](https://www.reddit.com/r/adventofcode/comments/k4ejjz/2020_day_1_unlock_crash_postmortem/) AoC runs on! So I could only submit my answer to Part 1 (and unlock Part 2) after waiting for several minutes. As a result [Eric Wastl](http://was.tl/), the creator of AoC, invalidated the leaderboard for this puzzle.

Day 1 is always just a warm-up. The input was short enough that a brute-force check of all pairs and triples looking for the combinations adding up to 2020 did the job. Python lets us do this without using array indices, instead iterating over the elements directly. Isn't that idiomatic!
