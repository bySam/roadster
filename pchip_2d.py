#Wed Mar 16 15:04:11 2022 +0100, 601cd27
from scipy import interpolate
import numpy as np 

def pchip_2d(x,y,zz,xx_eval,yy_eval):
    """
    Two-dimensional pchip interpolation
    Parameters:
      x:  1D array with strictly monotonic equally spaced x-values
      y:  1D array with strictly monotonic equally spaced y-values
      zz: 2D array with function values at all combinations of 
          x,y values. 
      xx_eval, yy_eval: Points where the function should be 
          evaluated

      The input should satisfy x.size == zz.shape[1] and 
      y.size == zz.shape[0]
    """
    xx_eval = np.atleast_2d(xx_eval)
    yy_eval = np.atleast_2d(yy_eval)
    dx  = interpolate.pchip_interpolate(x, zz, x, der=1, axis=1)
    dy  = interpolate.pchip_interpolate(y, zz, y, der=1, axis=0)
    dxy = (interpolate.pchip_interpolate(x, dy, x, der=1, axis=1) +
           interpolate.pchip_interpolate(y, dx, y, der=1, axis=0)) / 2
    # Get xind
    xind = np.zeros(xx_eval.shape, dtype='i')
    for row in range(xx_eval.shape[0]):
        for col in range(xx_eval.shape[1]):
            ind = 0
            while ind < x.size-2 and x[ind+1] <= xx_eval[row][col]:
                ind = ind+1
            xind[row][col] = ind
    # Get yind
    yind = np.zeros(yy_eval.shape, dtype='i')
    for row in range(yy_eval.shape[0]):
        for col in range(yy_eval.shape[1]):
            ind = 0
            while ind < y.size-2 and y[ind+1] <= yy_eval[row][col]:
                ind = ind+1
            yind[row][col] = ind
    hx = x[1]-x[0]
    hy = y[1]-y[0]
    tx = (xx_eval - x[xind])/hx
    ty = (yy_eval - y[yind])/hy
    t2 = np.multiply(tx,tx)
    t3 = np.multiply(tx,t2)
    xb11 = 2*t3-3*t2+1
    xb21 = hx*(t3-2*t2+tx)
    xb12 = -2*t3+3*t2
    xb22 = hx*(t3-t2)
    t2 = np.multiply(ty,ty)
    t3 = np.multiply(ty,t2)
    yb11 = 2*t3-3*t2+1
    yb21 = hy*(t3-2*t2+ty)
    yb12 = -2*t3+3*t2
    yb22 = hy*(t3-t2)

    zz_eval = np.zeros(xx_eval.shape)
    # i,j = 1,1
    z_select   = np.zeros(yind.shape)
    dx_select  = np.zeros(yind.shape)
    dy_select  = np.zeros(yind.shape)
    dxy_select = np.zeros(yind.shape)
    for row in range(yind.shape[0]):
        for col in range(yind.shape[1]):
            z_select[row][col]   += zz[yind[row][col]][xind[row][col]]
            dx_select[row][col]  += dx[yind[row][col]][xind[row][col]]
            dy_select[row][col]  += dy[yind[row][col]][xind[row][col]]
            dxy_select[row][col] += dxy[yind[row][col]][xind[row][col]]
    zz_eval += np.multiply(np.multiply(xb11,yb11),z_select)
    zz_eval += np.multiply(np.multiply(xb21,yb11),dx_select)
    zz_eval += np.multiply(np.multiply(xb11,yb21),dy_select)
    zz_eval += np.multiply(np.multiply(xb21,yb21),dxy_select)
    # i,j = 1,2
    z_select   = np.zeros(yind.shape)
    dx_select  = np.zeros(yind.shape)
    dy_select  = np.zeros(yind.shape)
    dxy_select = np.zeros(yind.shape)
    for row in range(yind.shape[0]):
        for col in range(yind.shape[1]):
            z_select[row][col]   += zz[yind[row][col]+1][xind[row][col]]
            dx_select[row][col]  += dx[yind[row][col]+1][xind[row][col]]
            dy_select[row][col]  += dy[yind[row][col]+1][xind[row][col]]
            dxy_select[row][col] += dxy[yind[row][col]+1][xind[row][col]]
    zz_eval += np.multiply(np.multiply(xb11,yb12),z_select)
    zz_eval += np.multiply(np.multiply(xb21,yb12),dx_select)
    zz_eval += np.multiply(np.multiply(xb11,yb22),dy_select)
    zz_eval += np.multiply(np.multiply(xb21,yb22),dxy_select)
    # i,j = 2,1
    z_select   = np.zeros(yind.shape)
    dx_select  = np.zeros(yind.shape)
    dy_select  = np.zeros(yind.shape)
    dxy_select = np.zeros(yind.shape)
    for row in range(yind.shape[0]):
        for col in range(yind.shape[1]):
            z_select[row][col]   += zz[yind[row][col]][xind[row][col]+1]
            dx_select[row][col]  += dx[yind[row][col]][xind[row][col]+1]
            dy_select[row][col]  += dy[yind[row][col]][xind[row][col]+1]
            dxy_select[row][col] += dxy[yind[row][col]][xind[row][col]+1]
    zz_eval += np.multiply(np.multiply(xb12,yb11),z_select)
    zz_eval += np.multiply(np.multiply(xb22,yb11),dx_select)
    zz_eval += np.multiply(np.multiply(xb12,yb21),dy_select)
    zz_eval += np.multiply(np.multiply(xb22,yb21),dxy_select)
    # i,j = 2,2
    z_select   = np.zeros(yind.shape)
    dx_select  = np.zeros(yind.shape)
    dy_select  = np.zeros(yind.shape)
    dxy_select = np.zeros(yind.shape)
    for row in range(yind.shape[0]):
        for col in range(yind.shape[1]):
            z_select[row][col]   += zz[yind[row][col]+1][xind[row][col]+1]
            dx_select[row][col]  += dx[yind[row][col]+1][xind[row][col]+1]
            dy_select[row][col]  += dy[yind[row][col]+1][xind[row][col]+1]
            dxy_select[row][col] += dxy[yind[row][col]+1][xind[row][col]+1]
    zz_eval += np.multiply(np.multiply(xb12,yb12),z_select)
    zz_eval += np.multiply(np.multiply(xb22,yb12),dx_select)
    zz_eval += np.multiply(np.multiply(xb12,yb22),dy_select)
    zz_eval += np.multiply(np.multiply(xb22,yb22),dxy_select)
    return zz_eval
