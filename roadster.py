#Wed Mar 16 15:04:11 2022 +0100, 601cd27
# Sammy Jonsson, Nikolai Bakken, Aron Wristel
import numpy as np
from scipy import interpolate
import matplotlib

def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
# c(v) = a1v−1 +a2 +a3v+a4v2
# 546.8 50.31 0.2584 0.008210
def consumption(v):
    #route = load_route(speed_ana.npz)
    t = 546.8/v + 50.31 + 0.2584*v + 0.008210*v*v # koeffecienterna från modellen i roadster.pdf
    return t

### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

def trapets (a,b,n,fx):
    h = (b-a )/n
    T = h *(np.sum(fx) - (fx[0]+fx[-1])/2)
    return T

### PART 2A ###
def time_to_destination(x, route, n):
    fx = 1/velocity(np.linspace (0,x,n+1), route) 
    a = trapets(0, x, n, fx)
    return a

    
### PART 2B ###
def total_consumption(x, route, n):
    return trapets(0, x, n, consumption(velocity(np.linspace(0,x,n+1), route)))

### PART 3A ###
def distance(T, route):
    dist, speed = load_route(route)
    n = 80000
    tol = 10**(-4)
    x = T*(sum(speed)/len(speed))
    dx = 2 * tol
    while (np.abs(dx) > tol):
        x = x + dx
        dx = -(time_to_destination(x, route, n)-T)/(1/velocity(x, route))
    return x

def reach(C, route):
    dist, speed = load_route(route)
    n = 80000
    if C >= total_consumption(dist[-1], route, n):
        return dist[-1]
    x = dist[-1]/2
    tol = 10**(-4)
    dx = 2 * tol
    while (abs(dx) > tol):
        x = x + dx
        dx = -(total_consumption(x, route, n)-C)/consumption(velocity(x, route))
    return x
