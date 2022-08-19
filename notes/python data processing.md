# Python Data Processing  

> Ref.
>
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

#### Different ways of using `np.random`  

1. Function  
   It uses `MT19937` as the default algorithm.

   ```python
   np.random.seed(408)
   print(np.random.rand(3))  
   # [0.49364422 0.83209827 0.987027  ]
   ```

2. Class (Legacy Random Generation)
   It gets the same with way 1, which is also the same result with MATLAB.  

   ```python
   rns = np.random.RandomState(seed=408)
   print(rns.random(3))
   # [0.49364422 0.83209827 0.987027  ]
   ```

3. Class (recommended)  
   It uses a new class `np.random.SeedSequence` to generate the state. However one can still get the same result with way 1&2 by set state manually.

   ```python
   from numpy.random import MT19937
   
   bg1 = MT19937(seed=408)
   rng1 = np.random.Generator(bg1)
   
   ss = np.random.SeedSequence(entropy=408) 
   bg2 = MT19937(ss)
   rng2 = np.random.Generator(bg2)

   # manually set the state 
   bg3 = MT19937()
   bg3.state = np.random.RandomState(408).get_state()
   rng3 = np.random.Generator(bg3)


   print(rng1.random(3))  # [0.72214204 0.15513132 0.48830953]
   print(rng2.random(3))  # [0.72214204 0.15513132 0.48830953]
   print(rng3.random(3))  # [0.49364422 0.83209827 0.987027  ]
   ```

## Pandas  

## Matplotlib
