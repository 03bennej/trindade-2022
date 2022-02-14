# Sample code to reproduce the 2d simulation results in "Evidence for a scale-dependent root-augmentation feedback and patchy invasion"

We solve the non-dimensionalised version of the equations given by:

<!-- Use https://latex.codecogs.com/ to generate images of equations -->

<!-- Latex code for first equation: \frac{\partial b_i}{\partial t} = g^i_b b_i (1-b_i) - \mu_i b_i + \delta_{b_i} \frac{w}{w+w_i^*}\phi_i * b_i -->

![](https://latex.codecogs.com/svg.image?\frac{\partial&space;b_i}{\partial&space;t}&space;=&space;g^i_b&space;b_i&space;(1-b_i)&space;-&space;\mu_i&space;b_i&space;&plus;&space;\delta_{b_i}&space;\frac{w}{w&plus;w_i^*}\phi_i&space;*&space;b_i,~~~i=1,2,)

<!-- Latex code for second equation: \frac{\partial w}{\partial t} = p - \nu \left(1 - \sum_{i=1}^{n} \rho_i b_i \right) w - w \sum_{i=1}^{n} g_w^i + \delta_w \Delta w) -->

![](https://latex.codecogs.com/svg.image?\frac{\partial&space;w}{\partial&space;t}&space;=&space;p&space;-&space;\nu&space;\left(1&space;-&space;\sum_{i=1}^{n}&space;\rho_i&space;b_i&space;\right)&space;w&space;-&space;w&space;\sum_{i=1}^{n}&space;g_w^i&space;&plus;&space;\delta_w&space;\Delta&space;w)

where

<!-- Latex code for b_i integral: g_{b}^i = \nu \lambda_i \int_\Omega g_i(\mathbf{x},\mathbf{x}',t) w(\mathbf{x}',t) d\mathbf{x}' -->

![](https://latex.codecogs.com/svg.image?g_{b}^i&space;=&space;\nu&space;\lambda_i&space;\int_\Omega&space;g_i(\mathbf{x},\mathbf{x}',t)&space;w(\mathbf{x}',t)&space;d\mathbf{x}')

<!-- Latex code for w integral: g_w = \gamma_i \int_\Omega g_i(\mathbf{x}',\mathbf{x},t) b(\mathbf{x}',t) d\mathbf{x}' -->

![](https://latex.codecogs.com/svg.image?g_{w}^i&space;=&space;\gamma_i&space;\int_\Omega&space;g_i(\mathbf{x}',\mathbf{x},t)&space;b(\mathbf{x}',t)&space;d\mathbf{x}')

and 

<!-- Latex code for root kernel: g_{i} = \frac{1}{2 \pi \sigma_{g_i}^2} \operatorname{exp}\left(-\frac{|\mathbf{X}-\mathbf{X}'|^2}{2 [\sigma_{g_i}(1+b_i(\mathbf{X},T)]^2)}\right) -->

![](https://latex.codecogs.com/svg.image?g_{i}&space;=&space;\frac{1}{2&space;\pi&space;\sigma_{g_i}^2}&space;\operatorname{exp}\left(-\frac{|\mathbf{X}-\mathbf{X}'|^2}{2&space;[\sigma_{g_i}(1&plus;b_i(\mathbf{X},T)]^2)}\right))

<!-- Latex code for dispersal kernel: \phi_{i} = \frac{1}{2 \pi} \left[ \frac{\sigma_{d_i}}{\left(|\mathbf{x}-\mathbf{x}'|+\sigma_{d_i}^2 \right)^{3/2}} \right] -->

![](https://latex.codecogs.com/svg.image?\phi_{i}&space;=&space;\frac{1}{2&space;\pi}&space;\left[&space;\frac{\sigma_{d_i}}{\left(|\mathbf{x}-\mathbf{x}'|&plus;\sigma_{d_i}^2&space;\right)^{3/2}}&space;\right])

The relationship between the non-dimensionalised parameters given here, and the dimensional parameters given in the paper are:


