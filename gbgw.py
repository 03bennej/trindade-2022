"""

Approximate integral terms GB and GW as a linear combination of convolutions

Reference: A fast algorithm for convolution integrals with space and time variant kernels.
Erez Gilad, Jost von Hardenberg (2006)

@author: Jamie Bennett
"""

import cupy as cp

def initsigmac(smin, smax, Nsigma):
    sigma = cp.zeros(Nsigma).astype('float32')
    fact = (smax/smin)**(1/(Nsigma-1))
    for i in range(Nsigma):
        sigma[i]=smin*fact**i
    return sigma
  
def gfunc(b, w, Hf, phi, phil, nx, ny, Nl):
    wf = cp.fft.fft2(w)
    z1 = cp.zeros((nx, ny)).astype('float32')
    z2 = cp.zeros((nx, ny)).astype('float32')
    ab = cp.zeros((nx, ny)).astype('float32')
    for l in range(0, Nl):
        alphal = 2 * phi**2 / (phi**2+(phil**2)[l])
        for j in range(0, Nl):
            if j==l:
                continue
            else:
                alphal *= (phi**2 - phil[j]**2) * (phil[l]**2 + phil[j]**2) \
                / ((phil[l]**2 - phil[j]**2)*(phi**2 + phil[j]**2))  
        ab = cp.fft.fft2(alphal * b)
        cf = cp.real(cp.fft.ifft2(wf * Hf[l,:,:]))
        z1 += alphal * cf[:, :]
        z2 += cp.real(cp.fft.ifft2(ab * Hf[l,:,:]))
    return z1, z2
