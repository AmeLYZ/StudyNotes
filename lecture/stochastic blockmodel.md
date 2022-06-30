# Stochastic Blockmodel    
## Binomial (simple graph, without self-loops)  
- Likelihood function:  
$$ P(G|p,g)=\prod_{i<j}p_{g_i,g_j}^{A_{ij}}(1-p_{g_i,g_j})^{1-A_{ij}} $$  
$ A_{ij} $: Adjacency matrix of graph $G$.  
$ p_{rs} $: the probability of an existing edge from vertices in group $r$ to 
vertices in group $s$.  
$ g_i $: The group which vertex $i$ belongs to.  

## Poisson (with multiple edges and self-loops)  
This considers the graph with multiple edges and self-loops.  
- Likelihood function:  
$$ P(G|\omega ,g)=\prod_{i<j}{{(\omega_{g_ig_j})^{A_{ij}}}\over{A_{ij}}!}\exp(-\omega_{g_ig_j}) \times \prod_i{{({1\over2}\omega_{g_ig_i})^{A_{ii}/2}}\over{(A_{ii}/2})!}\exp(-{1\over2}\omega_{g_ig_i}) $$
$ A_{ij} $: Adjacency matrix of graph $G$.  
$ A_{ii} $: counts one self-loop edge for degree=2.  
$ \omega_{rs} $: Expected edges from vertices in group $r$ to vertices in group $s$.  
$ g_i $: The group which vertex $i$ belongs to.   

- Rewrite likelihood with $m_{rs}=\sum_{ij}A_{ij}\delta_{g_i,r}\delta_{g_j,s}$  
$ m_{rs} $: The total number of edges from group $r$ to group $s$.  
Kronecker delta: $ \delta_{ij} = \begin{cases} 0 & i \neq j \\ 1&i=j\end{cases} $

## Degree-corrected Blockmodel  
Degree-corrected Blockmodel considers the probability distribution as a parameter.
- Likelihood function  
$$ P(G|\theta, \omega, g)=\prod_{i<j}{{(\theta_i\theta_j\omega_{g_ig_j})^{A_{ij}}}\over{A_{ij}}!}\exp(-\theta_i\theta_j\omega_{g_ig_j}) \times \prod_i{{({1\over2}\theta_i^2\omega_{g_ig_i})^{A_{ii}/2}}\over{(A_{ii}/2})!}\exp(-{1\over2}\theta_i^2\omega_{g_ig_i}) $$  
$ \sum_i\theta_i\delta_{g_i,r}=1 $: The sum of $\theta$ for all nodes in group $r$ (which is $\delta_{g_i,r}$) equals to 1.  
  