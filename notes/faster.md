# https://bair.berkeley.edu/blog/2020/03/05/compress/

when training Transformer models on a budget, you want to drastically increase model size but stop training very early.

We also recommend increasing model size, not batch size.

the total cost of inference is much larger than the cost of training for most real-world applications.

Thus, one can get the best of both worlds by training very large models and then heavily compressing them.