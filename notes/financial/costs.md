

It seems like we are gonna need some a100 gpus. They cost about $10k each.

Most GPT's are trained using 8 a100's. That's about $80k. 

Lets say that it is more like $100k for installation and taxes.

So, we have an up front cost of $100k. 

In order to pay that off, we would need to have:

$50/month * 12 months in year = $600 per month per user

$100,000 / $600 == 166 users

I feel like that is pretty reasonable, if we actually have a good product. Goal is to make this thing $10/month. Like a Spotify or Netflix subscription, but much more useful.


# https://www.semianalysis.com/p/the-inference-cost-of-search-disruption
ChatGPT Costs
Estimating ChatGPT costs is a tricky proposition due to several unknown variables. We built a cost model indicating that ChatGPT costs $694,444 per day to operate in compute hardware costs. OpenAI requires ~3,617 HGX A100 servers (28,936 GPUs) to serve Chat GPT. We estimate the cost per query to be 0.36 cents.

Our model is built from the ground up on a per-inference basis, but it lines up with Sam Altman’s tweet and an interview he did recently. We assume that OpenAI used a GPT-3 dense model architecture with a size of 175 billion parameters, hidden dimension of 16k, sequence length of 4k, average tokens per response of 2k, 15 responses per user, 13 million daily active users, FLOPS utilization rates 2x higher than FasterTransformer at <2000ms latency, int8 quantization, 50% hardware utilization rates due to purely idle time, and $1 cost per GPU hour.