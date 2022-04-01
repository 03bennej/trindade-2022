# GPU implementation of our algorithm to solve the integro-partial differential equations described in "Evidence for a scale-dependent root-augmentation feedback and patchy invasion"

**Description of files**

- guilandina-invasion.ipynb is a Jupyter notebook demoing our numerical solution. Along with the algorithm, it contains a full description of the equations solved.
- gbgw.py is a helper function that implements a fast convolution approximation for the tricky integral terms arising due to the modelling of non-local water uptake by plants. 
- ic-fig7.npz contains the initial condition used in Fig. 7 of our paper.

We do not claim the implementation in this repo is the most efficient by any means, but it significantly speeded up our computation compared to equivalent CPU implementations of the same algorithm.
