# Python Data Processing  
## Python  

## Numpy  
### Routines  
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
- `numpy.isin`  



## Pandas  

## Matplotlib

  