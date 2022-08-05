# Review of Linear Algebra  

This is a simple review of linear algebra.

## 1. Vector

There are different points of view explaining the vector.  

$$ \vec{v}=\begin{bmatrix} -1 \\ 2 \\ \end{bmatrix} $$

- Computer Science
   Vectors are **ordered lists of attributes**. The length of each vector is **the dimension** of the attributes.
- Physics
   Vectors are arrows pointing in space. **The length** and **the direction** defines a vector.
- Mathematics
   Combination of the above. First we should think about **an arrow** in a coordinate  system with **the tail sitting at the origin**.

## 2. Basis Vectors & Linear Combinations

- **The basis** of a vector space is a set of **linearly independent** vectors that **span** the full space. The vectors in that set are called **basis vectors**.
  - Linearly independency make sure that the set of vectors is with a minimum amount.
  - Span of vectors describes the result of linear combination by the basis is full of the space.  

  $\hat{\boldsymbol{i}}$(the unit vector in the x-direction) together with $\hat{\boldsymbol{j}}$(the unit vector in the y-direction) is a set of basis vectors. With the help of basis vectors, we can think of vectors as **a scaler** for the basis vectors.
  $$ \vec{v}=\begin{bmatrix} -1 \\ 2 \\ \end{bmatrix} = -1\hat{\boldsymbol{i}}+2\hat{\boldsymbol{j}} $$

- **Linear combination** is the combination(scaling) of chosen basis vectors. The word linear comes from the result in which, if you only change one of the basis vectors, the result gives out a set of vectors pointing on a strait line.

## 3. Matrices as Linear Transformation

- **Linear transformation** makes the grid lines(of the coordinate system) **parallel** and **evenly spaced**. By changing the value of $\hat{\boldsymbol{i}}$ and $\hat{\boldsymbol{j}}$ we can get coordinates of any vector after linear transformation.
  - rotation
  - shear
  - change of the basis vectors
  - ...

  Suppose we have a transformation $\hat{\boldsymbol{i}}$ changes from $\begin{bmatrix} 1 \\ 0 \\ \end {bmatrix}$ to $\begin{bmatrix} 1 \\ -2 \\ \end {bmatrix}$, and $\hat{\boldsymbol{j}}$ changes from $\begin{bmatrix} 0 \\ 1 \\ \end {bmatrix}$ to $\begin{bmatrix} 3 \\ 0 \\ \end {bmatrix}$. Then the original vector can be written in this formula:  
  $$
  \vec{v}=
  \begin{bmatrix} x \\ y \\ \end{bmatrix}=
  x\hat{\boldsymbol{i}}+y\hat{\boldsymbol{j}}=
  x\begin{bmatrix} 1 \\ 0 \\ \end {bmatrix}+y\begin{bmatrix} 0 \\ 1 \\ \end {bmatrix}
  $$  
  The vector after linear transformation, which is still **scaling of the basis vectors**, can be written in this formula:
  $$
  \vec{v'}=
  x\begin{bmatrix} 1 \\ -2 \\ \end {bmatrix}+y\begin{bmatrix} 3 \\ 0 \\ \end {bmatrix}=
  \begin{bmatrix} 1x+3y \\ -2x+0y \\ \end {bmatrix}=
  \begin{bmatrix} 1&3 \\ -2&0 \\ \end{bmatrix}\begin{bmatrix} x \\ y \\ \end{bmatrix}
  $$
  In this way, we can define a linear transformation by **matrix multiplication** giving a $2\times2$ **matrix**.
- **Matrix** is a set of vectors deciding where the vector is after the linear transformation.
- In more general cases, if we have a matrix $ \begin{bmatrix} a&b \\ c&d \\ \end{bmatrix}$ and a vector $ \begin{bmatrix} x \\ y \\ \end{bmatrix}$, then the **matrix multiplication** can be written by:
$$
\begin{bmatrix} a&b \\ c&d \\ \end{bmatrix}\begin{bmatrix} x \\ y \\ \end{bmatrix}=
\underbrace{x\begin{bmatrix} a \\ c \\ \end{bmatrix}+y\begin{bmatrix} b \\ d \\ \end{bmatrix}}_{\text{where the intuition is}}=
\begin{bmatrix} ax+by \\ cx+dy \\ \end{bmatrix}
$$

## 4. Matrix Multiplication as Combinations of Linear Transformation

Let's consider two linear transformations, in which we first rotate the plane 90° counterclockwise, then apply a shear.  
$$
\vec{v'}=
\underbrace{\begin{bmatrix} 1&1 \\ 0&1 \\ \end{bmatrix}}_{\text{shear}}\underbrace{\begin{bmatrix} 0&-1 \\ 1&0 \\ \end{bmatrix}}_{\text{rotation}}\begin{bmatrix} x \\ y \\ \end{bmatrix}=
\underbrace{\begin{bmatrix} 1&-1 \\ 1&0 \\ \end{bmatrix}}_{\text{combination}}\begin{bmatrix} x \\ y \\ \end{bmatrix}
$$
To apply the combination is equal to apply the rotation first and the shear then. Here we can find out:
$$
\begin{bmatrix} 1&1 \\ 0&1 \\ \end{bmatrix}\begin{bmatrix} 0&-1 \\ 1&0 \\ \end{bmatrix}=
\begin{bmatrix} 1&-1 \\ 1&0 \\ \end{bmatrix}
$$
More generally, we consider a combination of two linear transformations $M_1$ and $M_2$.
$$
\underbrace{\begin{bmatrix} a&b \\ c&d \\ \end{bmatrix}}_{M_2}\underbrace{\begin{bmatrix} e&f \\ g&h \\ \end{bmatrix}}_{M_1}
$$
Let's recall the knowledge of linear transformation, which is to change the basis and to scale the basis vectors with the same scaler. We focus on the basis vectors after $M_1$. $\hat{\boldsymbol{i}}$ lies in $\begin{bmatrix} e \\ g \\ \end{bmatrix}$ and $\hat{\boldsymbol{j}}$ lies in $\begin{bmatrix} f \\ h \\ \end{bmatrix}$. Then we do $M_2$ to the basis vectors:
$$
\hat{\boldsymbol{i}} \longrightarrow
\begin{bmatrix} a&b \\ c&d \\ \end{bmatrix}\begin{bmatrix} e \\ g \\ \end{bmatrix}=
\begin{bmatrix} ae+bg \\ ce+dg \\ \end{bmatrix}
$$

$$
\hat{\boldsymbol{j}} \longrightarrow
\begin{bmatrix} a&b \\ c&d \\ \end{bmatrix}\begin{bmatrix} f \\ h \\ \end{bmatrix}=
\begin{bmatrix} af+bh \\ cf+dh \\ \end{bmatrix}
$$ 
One we get the basis vectors, we can do the combination of linear transformations through **matrix multiplication**:
$$
\underbrace{\begin{bmatrix} a&b \\ c&d \\ \end{bmatrix}}_{M_2}\underbrace{\begin{bmatrix} e&f \\ g&h \\ \end{bmatrix}}_{M_1}=
\underbrace{\begin{bmatrix} ae+bg&af+bh \\ ce+dg&cf+dh \\ \end{bmatrix}}_{\text{combination of } M_1 \text{ and }M_2}
$$

## References

- [Essence of linear algebra - YouTube](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
