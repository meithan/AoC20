# AoC20

My solutions for [Advent of Code 2020](https://adventofcode.com/2020). In Python 3.

I'll be updating this as a sort of mini blog whenever I can, commenting on the daily problems.

You can also check out our fancy [custom private leaderboard](https://meithan.net/AoC20/), with medals awarded to the fastest solvers. See (and download/fork!) the project [here](https://github.com/meithan/AoCBoard).

Go to day: [1](#day1) - [2](#day2) - [3](#day3) - [4](#day4) - [5](#day5) - [6](#day6) - [7](#day7) - [8](#day8) - [9](#day9) - [10](#day10)

___

**Day 10**: [Adapter Array](https://adventofcode.com/2020/day/10)<a name="day10"></a>

9m 16s (#1955) / 53m 35s (#2905) - [code](https://github.com/meithan/AoC20/blob/main/day10.py)

Ah, the first problem where the naive brute-force solution won't work. I've been waiting for you.

Part 1 was straightforward. But again I got snatched the gold medal by coding too slow. It was like 10 lines of code! Anyway.

Part 2 is where things got interesting. The outlet, adapters and device can be understood as a directed graph: there's an edge from a to b if 1 <= joltage(b) - joltage(a) <= 3. Then, the problem was basically to count the number of simple paths from the start node (the outlet) to the end node (the device).

The [branching factor](https://en.wikipedia.org/wiki/Branching_factor) isn't too big --at most 3 nodes are reachable from any given node-- and the number of adapters in my input (96) was not huge. So, despite the warning in the problem statement that there could be trillions of paths, I decided to try the naive brute-force approach anyway: a [traversal](https://en.wikipedia.org/wiki/Graph_traversal) of the graph from start to end, branching the partial paths when there were multiple options.

After coding it and checking it worked with the given test inputs, I ran it on the actual input ... A couple minutes later it was still running and the program was beginning to eat up my RAM, storing all the partial paths. [Turns out](https://cs.stackexchange.com/questions/423/how-hard-is-counting-the-number-of-simple-paths-between-two-nodes-in-a-directed) that this problem is [#P-complete](https://en.wikipedia.org/wiki/%E2%99%AFP-complete), the counting-problem analog of [NP-complete](https://en.wikipedia.org/wiki/NP-completeness).

Then I noticed something in the graph I had drawn on paper with the smaller test input: when two consecutive adapters are separated by a value of 3, there can only be ONE path between them. These 'transitions' separate parts of the graph into independent sub-problems, and counting the number of paths in each sub-problem is enough to get the global number of paths.

For instance, for the first test input, the list of adapters, including the outlet and device, is:

  ``[0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]``

and the transition points are at 1->4, 7->10, 12->15, 16->19 and 19->22; all paths must pass through these and there is only a single path between them. Hence, the sub-problems to be solved are:

  ``[0, 1] [4, 5, 6, 7] [10, 11, 12] [15, 16] [19] [22]``

Thus, we compute the number of paths within each sub-problem --which are,
hopefully, much smaller than the whole problem, which turned out to the case-- and multiply the results together. Then that is the answer. This is a [divide-and-conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm) strategy.

After checking that this also worked for the second, larger test input, I tried the actual input. And lo and behold, in a fraction of a second all the sub-problems were solved and the final answer was correct! Yay! The largest sub-problem in the input turned out to have only 5 nodes, so solving them all by brute-force traversal was very fast.

*A more direct mathematical solution*

After solving the problem I investigated what solutions there were to the general problem, as this is graph theory problem that most certainly been studied extensively. And I did find an "analytical" solution that exploits a [property of the adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix#Matrix_powers) that I dimly recalled:

> "If A is the adjacency matrix of the directed or undirected graph G, then the matrix A^n (i.e., the matrix product of n copies of A) has an interesting interpretation: the element (i, j) gives the number of (directed or undirected) walks of length n from vertex i to vertex j."

Thus, one can construct the adjacency matrix of the graph of adapters, compute the successive A^k for k in [1,N] (using numpy's [matmul](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)), and in simply accumulate the values of A^k_{1,N}, since that would be the number of k-length paths between the first and last nodes. And, sure enough, this [works too](https://github.com/meithan/AoC20/blob/main/day10_alt.py).

___

**Day 9**: [Encoding Error](https://adventofcode.com/2020/day/9)<a name="day9"></a>

13m 0s (#3161) / 26m 23s (#3470) - [code](https://github.com/meithan/AoC20/blob/main/day09.py)

Another problem with a straightforward brute force solution. But I wasted too much time obsessing on optimizing and over-complicating stuff (I used a deque!), so I got pushed to 3rd place in our private leaderboard. Darn. You know what [they say](https://softwareengineering.stackexchange.com/questions/80084/is-premature-optimization-really-the-root-of-all-evil): "premature optimization is the root of all evil".

For Part 1 one keeps track of the current 25 numbers (I used a [deque](https://en.wikipedia.org/wiki/Double-ended_queue) from [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque), which is totally unnecesary), computes the sums of all pairs (I used [itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product), but in fact the strictly correct way would be [itertools.combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations) -- I was lucky this didn't result in an incorrect answer!), and checks if the next number is in the sums.

For Part 2 the brute-force solution is to check the sums of all consecutive pairs, then all consecutive triplets, and so on, until one finds the answer. I optimized the code so it wasn't necessary to sum all numbers in a group every time, since consecutive groups only differ by the first and last element.

___

**Day 8**: [Handheld Halting](https://adventofcode.com/2020/day/8)<a name="day8"></a>

5m 7s (#462) / 11m 33s (#413) - [code](https://github.com/meithan/AoC20/blob/main/day08.py)

Pretty straightforward. The program exits if we come back to a previously executed instruction; this *will* result in an infinite loop since the effect of the instructions does not depend on the value of the accumulator.

For Part 2 we simply execute modified versions of the program, changing one jmp or nop instruction at a time, and stop when execution leads to normal program termination.

___

**Day 7**: [Handy Haversacks](https://adventofcode.com/2020/day/7)<a name="day7"></a>

26m 22s (#1979) / 54m 55s (#2907) - [code](https://github.com/meithan/AoC20/blob/main/day07.py)

This one was a bit more difficult than previous problems. The relationships between the bag types (color), i.e. which bags hold which bags, can be represented as a weighted [directed graph](https://en.wikipedia.org/wiki/Directed_graph). For the test input provided in the problem statement this looks like this (plotted with [networkx](https://networkx.org/), code [here](https://github.com/meithan/AoC20/blob/main/day07_viz.py)):

![graph](day07_test1.png)

Directed edges point from a bag type to the bag types it contains, and weights indicate the number of contained bags of that type.

The Bag class represents a bag type, as uniquely identified by its color. Its "contents" are the bag types it contains (a dict having the bag type objects as keys and the number of such bags as value). We also keep track of its "parents", i.e. bag types that can contain this bag type (which can be multiple; hence, this is not a [tree](https://en.wikipedia.org/wiki/Tree_(data_structure))).

Then it's just a matter of "walking" this graph, starting from the shiny gold bag type. In Part 1, we walk "up" the graph, successively following the parents until no more parents are left to follow. We count how many *unique* bag types are encountered in the process (as it's possible to reach a bag type via multiple paths).

For Part 2, we compute the total number of contained bags [recursively](https://en.wikipedia.org/wiki/Recursion_(computer_science)) starting from the shiny gold bag. The number of total contained bags for any bag type is equal to the number of directly contained bag types plus the number of each contained bag type times the total number of contained bags in *that* bag type. For instance, in the example the total contained bags for the shiny gold type is given by:

``total_contained_bags(shiny gold) = 1 (dark olive) + 1 x total_contained_bags(dark olive) + 2 (vibrant plum) + 2 x total_contained_bags(vibrant plum)``

Hence the calculation naturally recurses, walking "down" the graph following the contained bags until all reachable bags with no more contained bags are accounted for. Since there are no cycles (hopefully) this process should terminate.

It wasn't really a complicated problem, just a bit more involved than the previous ones. Knowing AoC, I was initially worried about the phrase "be sure to count all of the bags, even if the nesting becomes topologically impractical". It could mean that the graph contained cycles or some other twist. But in the end it did not.

I'm not happy with my solution times. I even lost one of the gold medals.

___

**Day 6**: [Custom Customs](https://adventofcode.com/2020/day/6)<a name="day6"></a>

4m 5s (#595) / 13m 11s (#2022) - [code](https://github.com/meithan/AoC20/blob/main/day06.py)

This problem basically is about computing set [unions](https://en.wikipedia.org/wiki/Union_(set_theory)) and [intersections](https://en.wikipedia.org/wiki/Intersection_(set_theory)). In my original solution I did this manually. Too late I remembered that Python sets actually support these [operations](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)! Naturally, | is the union operator and & is the intersection operator. Could've saved me some time.

___

**Day 5**: [Binary Boarding](https://adventofcode.com/2020/day/5)<a name="day5"></a>

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

**Day 4**: [Passport Processing](https://adventofcode.com/2020/day/4)<a name="day4"></a>

7m 31s (#759) / 22m 29s (#579) - [code](https://github.com/meithan/AoC20/blob/main/day04.py)

The kind of string matching problem for which [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) ("regexes") were invented (and Python has a nice [regex module](https://docs.python.org/3/library/re.html)). It was a nice little regex practice; I did have to look a couple of things up on the web. [regexr](https://regexr.com/) is an incredibly useful resource for that!

___

**Day 3**: [Toboggan Trajectory](https://adventofcode.com/2020/day/3)<a name="day3"></a>

4m 23s (#483) / 6m 39s (#295) - [code](https://github.com/meithan/AoC20/blob/main/day03.py)

Another easy one. Careful with mixing up the meaning of rows and column in these arrays. And there's no need to actually extend the "forest" to the right, one can simply take the x coordinate modulo the number of columns (using the [modulo operator](https://python-reference.readthedocs.io/en/latest/docs/operators/modulus.html) `%`) to effectively make the array wrap around to the right.

Not fast enough to make the top 100 on either star :/.
___

**Day 2**: [Password Philosophy](https://adventofcode.com/2020/day/2)<a name="day2"></a>

2m 47s (#130) / 4m 02s (**#69!**) - [code](https://github.com/meithan/AoC20/blob/main/day02.py)

An easy one ... and I made the top 100 for the second star! Which put me on the global leaderboard! Yay! These are my first ever leaderboard points. And probably the only time I'll be on the global leaderboard (keeping expections low here).

Python's great string manipulation methods (like [split](https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split) and [strip](https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip)) contributed to coding the solution quickly. Also note that the bit-wise [xor](https://en.wikipedia.org/wiki/Exclusive_or) operator `^` acts as a *logical* xor when applied to booleans (a not very well documented feature) -- much shorter than writing the same using `and`, `or` and `not`.

___

**Day 1**: [Report Repair](https://adventofcode.com/2020/day/1)<a name="day1"></a>

7m 08s (#293) / 8m 06s (#283) - [code](https://github.com/meithan/AoC20/blob/main/day01.py)

I coded the solution to Part 1 in just 2 minutes ... But everyone submitting at the same time [overloaded the AWS instances](https://www.reddit.com/r/adventofcode/comments/k4ejjz/2020_day_1_unlock_crash_postmortem/) AoC runs on! So I could only submit my answer to Part 1 (and unlock Part 2) after waiting for several minutes. As a result [Eric Wastl](http://was.tl/), the creator of AoC, invalidated the leaderboard for this puzzle.

Day 1 is always just a warm-up. The input was short enough that a brute-force check of all pairs and triples looking for the combinations adding up to 2020 did the job. Python lets us do this without using array indices, instead iterating over the elements directly. Isn't that idiomatic!

*A more efficient solution*

This solution works in a reasonable time because the list of numbers is short (200). But if the list had a million numbers it would be a different story. The current brute-force check-all-combinations is O(n^2) for Part 1 and O(n^3) for Part 2. Can we do better?

Sure! Here's a [faster solution](https://github.com/meithan/AoC20/blob/main/day01_fast.py).

On a first pass we load all the numbers in a Python [set](https://docs.python.org/3/library/stdtypes.html#set). This is a data structure that stores items in no particular order (unlike a list) and implements a [hash table](https://en.wikipedia.org/wiki/Hash_table) for quick lookups. The upshot is that asking whether some item is contained or not in the set is an O(1) operation (on average) -- that is, the time it takes does not grow with the number of items in the set, so it doesn't matter if it has 200 or 1 million items in it. Using a list or tuple you have to check all the elements one by one, and that is O(n). Even if you did binary search in a previously sorted list that would be O(log(n)) -- nothing beats O(1).

Then, on a second pass, for every number x in the list we check whether y = 2020 - x is in the set. If it is, then x + y = x + (2020 - x) = 2020 and we've found the answer. If the set lookups are O(1) then this second pass is O(n). Adding that to the O(n) of the first pass, the total running time is O(2*n) ~ O(n). A much more efficient algorithm than brute-force!

For Part 2 we need to iterate twice over the numbers, instead of thrice, and then leverage the set. For every pair of numbers x and y (with x != y), we ask whether z = 2020 - x - y is in the set. If it is, then we have our answer. This solution is O(n^2) instead of O(n^3). Still a great speed-up if the list is large!
