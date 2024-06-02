This morning I tried to understand the Montgomery modular reduction algorithm. Frankly put: I still don't succeed. But I invented this recursive modular division algorithm, that solely uses division and modulus of two's next power, while furthermore only multiplication and subtraction. It's likely vast weakness again't Montgomery's solution must lie in the indefinite runtime, that cmay very well be characteristic to the numbers being crunched and thus leak information if applied for cryptography in form of a side channel... :/

Then I found out it can easily be described in a loop too.

testing.txt is the output of loop_mod.py: it wasn't easy to find a test case, where the subtraction in the end needs to be performed.
