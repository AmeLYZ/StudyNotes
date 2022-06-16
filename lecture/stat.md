# 1. Linear Regression  
$$ y=\beta X+\epsilon$$
## Estimation of the Parameter  
### BLUE: Best Linear Unbiased Estimator  
- Unbiasedness  
- "Best", Efficiency  
- Weak consistency  

## Assumption in the Classical Linear Regression
- Linear dependence between $y$ and $x$.  
- Independence of the column vectors of $X$  
$$ rank[X]=k $$
- Exogeneity  
$$ E[\epsilon|X]=0 $$  
- Spherical disturbances  
$$ E[\epsilon\epsilon^T|X]=\sigma{^2_\epsilon}I_n$$  
- The stochastic disturbances $ \epsilon $ are assumed to be i.i.d.(independent and identically distributed)  
- Normality of $ \epsilon $  
$$ {\epsilon|X}\sim{i.i.d.N(0,\sigma{^2_\epsilon}I_n)} $$  
### Multicollinearity  
Multicollinearity occurs when an explanatory variable is predictable with another explanatory variable with a linear model.  
- perfect multicollinearity  
   - $ rank[X]<k $  
   - Neither $ (X^TX)^{-1} $ nor $ \hat{\beta}_{OLS}=(X^TX)^{-1}X^Ty $ exists.  
   - One of the correlated variables should be dropped.  
- not perfect multicollinearity  
   - (removal is not necessary)
   - Take largersample size  
   - Add additional information or restriction to the model  

## Bias  
### Factors Causing the Bias  
- Measurement error  
- Missing data  
- Outlier  

## Maximum Likelihood Method  
It's alternative to least squares.  
The assumption is $ f(\epsilon_i)={{1}\over{\sqrt{2\pi\sigma{^2_\epsilon}}}}e^{-{{1}\over{2\sigma{^2_\epsilon}}}\epsilon{^2_i}} $, in which $ \epsilon_i $ is the error term in the linear classical regression model.  
- Likelihood function:  
$$ L(\beta,\sigma{^2_\epsilon}|\epsilon)=\Pi{^n_{i=1}}{{1}\over{\sqrt{2\pi\sigma{^2_\epsilon}}}}e^{-{{1}\over{2\sigma{^2_\epsilon}}}\epsilon{^2_i}}=\Pi{^n_{i=1}}{{1}\over{\sqrt{2\pi\sigma{^2_\epsilon}}}}e^{-{{1}\over{2\sigma{^2_\epsilon}}}(y_i-\Sigma_jx_{ij}\beta_j)^2} $$
- Log-likelihood:  
$$ l(\beta,\sigma{^2_\epsilon})=const.-{{n}\over{2}}\log(\sigma{^2_\epsilon})-(y-X\beta)^T(y-X\beta)/(2\sigma{^2_\epsilon}) $$  
- Fitst order condition for the log-likelihood:  
$$ s(\beta)={{\partial l}\over{\partial\beta}}=-{{1}\over{\sigma{^2_\epsilon}}}(X^Ty-X^TX\beta)=0 $$  
$$ s(\sigma{^2_\epsilon})=-{{{n}\over{2\sigma{^2_\epsilon}}}}+{{(y-X\beta)^T(y-X\beta)}\over{2\sigma{^4_\epsilon}}}=0 $$
- ML estimator:  
$$ \hat \beta_{ML}=(X^TX)^{-1}X^Ty$$  
$$ \hat \sigma{^2_{\epsilon,ML}}={{e^Te}\over{n}}$$

### Likelihood Ratio Test  
$$ \lambda={{L(\theta_0)}\over{L(\hat \theta_{ML})}}={{L(\theta_0)}\over{L(\hat \theta)}} $$  
- Likelihood ratio test:  
$$ LR=-2\ln(\lambda)=-2(l(\theta_0)-l(\hat \theta_0)) $$
   - Property: $ LR\sim\chi^2(k) $


## Model Selection  
### Coefficient of Determination: $ R^2 $  
- Definition  
$$ R^2=1-{{SSR}\over{TSS}} $$ 
   - $ TSS=(y-\bar{y})^T(y-\bar{y})=(X\hat{\beta}+e)^T(X\hat{\beta}+e)=\hat{\beta}^TX^TX\hat{\beta}+e^Te $: total sum of squares  
   - $ SSR=e^Te $: squared sum of residual  
   - $ SSE=\hat{\beta}^TX^TX\hat{\beta}=TSS-SSR $: explained sum of squares
- $ 0 \leq R^2 \leq 1 $  
   - $ 1 $: Fitted model explains all variability in $ y $  
   - $ 0 $: No linear relationship

### Adjusted $ R^2 $  
$ R^2 $ increases if number of explanatory variables $ k $ increases. However, simpler model is better.  
- Definition  
$$ \bar{R}^2 = 1-{{n-1}\over{n-(k-1)}}(1-R^2)$$  

### Other Measures  
- AIC(Akaike Information Criterion)  
$$ AIC=2k-2\ln(\hat{L})$$  
   - $ \hat{L} $: the maximized likelihoos function
- BIC(Bayesian Information Criterion)  
$$ BIC=k\ln(n)-2\ln(\hat{L})$$

# 2. Hypothesis Testing
## Null Hypothesis  
An unknown parameter takes a certain value.  
Ususlly we want to reject null hypothesis.  

## Alternative Hypothesis  
A hypothesis which holds if the null hypothesis is rejected.  

## One and Two-tailed Tests  
### Two-tailed Test  
If the estimated value $ x $ is below or above the critical values, the null hypothesis that the parameter $ x $ takes a certain value $ \mu $ is rejected. The alternative hypothesis is $ x\neq\mu $ .  

### One-Tailed Test  
Altlernative hypothesis is $ x>\mu $ or $ x<\mu $ .  

### Sighnificanve Level: $\alpha$  

## $t$-test  
If the variance of the disturbances is known, standardized estimated values follow the normal distribution $ {{\widehat{\beta}_i-\beta_i}\over{\sigma_{\beta_i}}}\sim{N(0,1)} $ .  
If the variance is unknown, $ test={{\widehat{\beta}_i-\beta_i}\over{s_{\widehat{\beta}_i}}}={{{\widehat{\beta}_i-\beta_i}\over{\sigma_{\beta_i}}}\over{{s_{\beta_i}}\over{\sigma_{\beta_i}}}}\sim{t(n-k)} $ (**$ t $-destribution** with $ n-k $ degrees of freedom).  

## F-
asddhufhuskljjldfskjfjsddsfaas
