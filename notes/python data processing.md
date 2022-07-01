# Python Data Processing  
> Ref.
>- [Numpy documentation](https://numpy.org/doc/stable/index.html)

## Python  
- `slice()`
- `map()`
- `lambda`
- `yield`  
- compare `concurrent.futures` & `multiprocessing`  


## Numpy  
### Routines  
- `numpy.array`  
- `numpy.asarray`  
Convert the input to an array without copy.
- `numpy.where`  
It returns the indices of the condition or the `x` & `y` given.
```python
>>> a = np.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.where(a < 5)
(array([0, 1, 2, 3, 4], dtype=int64),)
>>> np.where(a < 5, a, 10*a)
array([ 0,  1,  2,  3,  4, 50, 60, 70, 80, 90])
```
- `numpy.nonzero`  
`numpy.where` with only condition is the same with `numpy.nonzero`.  
```python
>>> a = np.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> (a < 5).nonzero()
(array([0, 1, 2, 3, 4], dtype=int64),)
```  
- numpy.transpose  
```python
>>> x = np.array([[3, 0, 0], [0, 4, 0], [5, 6, 0]])
>>> x
array([[3, 0, 0],
       [0, 4, 0],
       [5, 6, 0]])
>>> np.nonzero(x)
(array([0, 1, 2, 2]), array([0, 1, 0, 1]))
>>> np.transpose(np.nonzero(x))
array([[0, 0],
       [1, 1],
       [2, 0],
       [2, 1]])
```
- `numpy.isin`  



## Pandas  

## Matplotlib

  