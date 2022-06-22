# Stochastic Blockmodel    
## Binomial (without self-loops)  
- Likelihood function:  
$$ P(G|p,g)=\prod_{i<j}p_{g_i,g_j}^{A_{ij}}(1-p_{g_i,g_j})^{1-A_{ij}} $$  
$ A_{ij} $: Adjacency matrix of graph $G$.  
$ p_{rs} $: the probability of an existing edge from vertices in group $r$ to 
vertices in group $s$.  
$ g_i $: The group which vertex $i$ belongs to.  

## Poisson (with multiple edges and self-loops) 
- Likelihood function:  
$$ P $$
$$ P(G|\omega ,g)=\prod_{i<j}{{(\omega_{g_ig_j})^{A_{ij}}}\over{A_{ij}}!}\exp(-\omega_{g_ig_j}) \times \prod_i{{{1\over2}(\omega_{g_ig_i})^{A_{ii}/2}}\over{(A_{ii}/2})!}\exp(-{1\over2}\omega_{g_ig_i}) $$
$ A_{ij} $: Adjacency matrix of graph $G$.    
$ \omega_{rs} $: Expected edges from vertices in group $r$ to vertices in group $s$.  
$ g_i $: The group which vertex $i$ belongs to.  

## Degree-corrected Blockmodel  
