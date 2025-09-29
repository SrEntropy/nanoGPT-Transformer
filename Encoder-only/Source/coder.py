
#Token embedding
import math
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

#Vocabulary
vocab = {
    "dragon":0,
    "🧠": 1,
    "fire":2,
    "payload":3,
    "<PAD>":4
}

vocab_size = len(vocab)
d_model = 64 ##Tune it if needed

embedding_layer = nn.Embedding(vocab_size, d_model)

#Step2: Positional Encoding
'''Attention does not care about order. 
Use sine or cosine function
to inject positional information with an unique signature.'''

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_length = 500):
        super().__init__()
        
        pe = torch.zeros(max_length, d_model)
        position = torch.arange(0, max_length).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model,2) *(-math.log(10000.0)/d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.pe = pe.unsqueeze(0) # shape: [1,max_length, d_model]

    def forward(self, x):
        # x shape: [batch_size,seq_len, embedding_dim]
        return x + self.pe[:, :x.size(1)].to(x.device)


#Step 3: Scaled Dot-Product Attention 
'''This is the core operation
    Attention(Q,K,V)=Softmax((QK^T)/(sqroot(dk)))V
    Where:
    Q = XW^Q
    K = XW^K 
    V = XW^V
    Each token queries all others, scores them , 
    and blends their values'''

#Step 4: Multi-Head Attention 
'''Instead of one attention calculation, 
    we run multiple in parallel
    MultiHead(Q,K,V) = Concat(head1,..,headh)Q^O
    Each head learns to focus on different aspects of the input'''

#Step 5: Feedforward Network 
'''A simple two-layer MLP
    FFN(x) = ReLU(xW1 += b1)W2+b2
    This adds non-linearity and depth'''

#Step 6: Residual + LayerNorm
'''Each sublayer is wrapped like this
 LayerNorm (X+Sublayer(x))
 This helps grediants flow and stabilizes training'''

#Step 2: 
''''''

#Step 2: 
''''''

#Sample input
tokens = torch.tensor([[0, 1, 2, 3]]) #shape: [1,4], batch size of q sequence : [batch_size, seq_len, embedding_len]
embedded = embedding_layer(tokens)      #shape: [1,4,64]
#Apply positional encoding
pos_encoding = PositionalEncoding(d_model) #d_model:64
x = pos_encoding(embedded) #Shape: [1,4,64]

pe_matrix = pos_encoding.pe[0]
plt.figure(figsize=(10,6))
plt.imshow(pe_matrix[:100].numpy(), cmap='viridis', aspect='auto')
plt.title("Positional Encoding Heatmap")
plt.xlabel("Embedding Dimension")
plt.ylabel("Token Position")
plt.colorbar()
plt.savefig("PosEmbeddings.png")

