
# Scale Dot Product Attention
## Attention(Q, K, V)
- How much each query (Q) should pay attention to each key (K). Through Softmax, it transforms the vector of row numerical scores into probability distribution and utilizes those distribution to take a weighted sum of the values. In other words, Given how much I care, what information do I actually take?---> weighted suem over Values (V)

- Query: What am I looking for?
- Key: What do I represent?
- Value: What information do I carry?

### Step 1: Compute raw attention scores.
- QK^T -> nxn matrix shape for compatibility scores
row-i: how query Qi compares to all keys.
Entry(i,j): dot product Qi.Kj
Note: Paper emphasizes that this is a compatibility check between Q and K

### Step 2: Scale raw attention scores.
- Why scale? 
    - Dot products increase with dimension causing the softmax to saturate and produce tiny gradients.
- Scaling prevents softmax saturation  and stabilizes training process.

### Step 3: Softmax to get attention weights.
- Each row becomes a probability distribution over all positions
    - High scores -> High weight
    - Low scores -> Low weight
- All weights sum up to 1.0

### Step 4: Weighted sum of values softmax()V
Each output is a mixture of V vectors weighted by how relevant they are to the Query. Therefore, creating a weighted combinations of values.
- Fro softmax output, Given how much I care, what information do I need (weighted sum over V)

The following exercise depics the entire process of "Scaled Dot Product Attention."
(example)[www.me.com]
