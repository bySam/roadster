#Wed Mar 16 15:04:11 2022 +0100, 601cd27
# pytest.main(["-k","part1a"])
import numpy as np
import pytest
import roadster
import route_nyc

### PART 1A, CONSUMPTION ###
def test_part1a_A():
    ref_value_4 = 188.17496
    assert np.isclose(roadster.consumption(4), ref_value_4), 'consumption(4) not close to reference value' 

def test_part1a_B():
    ref_value_188p7 = 394.3069361506624
    assert np.isclose(roadster.consumption(188.7), ref_value_188p7), 'consumption(188.7) not close to reference value'  

def test_part1a_C():
    dist_array = np.array([0.1,23.7,48.53,201.3])
    ref_array  = np.array([5518.3359221,
                           84.11728485780591,
                           93.45328035557738,
                           437.7253386655241])        
    assert np.all(np.isclose(roadster.consumption(dist_array), ref_array)), 'consumption(np.array([0.1,23.7,48.53,201.3])) not close to reference array'  

### PART 1B, velocity ###
def test_part1b_A():
    ref_value_anna_21p4 = 103.58230081237032
    assert np.isclose(roadster.velocity(21.4,'speed_anna'), ref_value_anna_21p4), 'velocity(21.4) not close to reference value'

def test_part1b_B():
    ref_value_elsa_14p53 = 89.22383224404504
    assert np.isclose(roadster.velocity(14.53,'speed_elsa'), ref_value_elsa_14p53), 'velocity(14.53) not close to reference value'

def test_part1b_C():
    dist_array = np.array([0,2.3,4.53])
    ref_array_anna = np.array([5.0,51.20013042688889,78.3714678653808])    
    assert np.all(np.isclose(roadster.velocity(dist_array,'speed_anna.npz'), ref_array_anna)), 'velocity(np.array([0,2.3,4.53])) not close to reference value'

def test_part1b_D():
    dist_array = np.array([12.2,4.63,18.9,13.3])
    ref_array_elsa = np.array([74.98566466606418,75.96438722958086,
                               94.77994324905988,76.0864351123139])
    assert np.all(np.isclose(roadster.velocity(dist_array,'speed_elsa.npz'), ref_array_elsa)), 'velocity(np.array(...)) not close to reference value'

# Check that error handling works    
def test_part1b_E():
    dist_array = np.array([3.9,-0.1,2.3,4.53])
    # This input should result in AssertionError due to negative
    # value in input array.
    with pytest.raises(AssertionError):
        roadster.velocity(dist_array,'speed_anna.npz')

def test_part1b_F():
    route = 'speed_anna.npz'
    distance_km, _ = roadster.load_route(route)
    dist_array = np.array([3.9,2.3,distance_km[-1]+1, 4.53])    
    # This input should result in AssertionError due to value in input
    # array greater than route length.
    with pytest.raises(AssertionError):
        roadster.velocity(dist_array,route)

### PART 2A, TIME TO DESTINATION ###
def test_part2a_A():
    route = 'speed_anna.npz'
    x = 15.5
    n = 2
    ref_value   = 0.9010019433964633
    check_value = roadster.time_to_destination(x, route, n)
    assert np.isclose(ref_value, check_value), 'time_to_destination(...) not close to reference value'

def test_part2a_B():
    route = 'speed_anna.npz'
    x = 35
    n = 100
    ref_value   = 0.4049811174885838
    check_value = roadster.time_to_destination(x, route, n)
    assert np.isclose(ref_value, check_value), 'time_to_destination(...) not close to reference value'

def test_part2a_C():
    route = 'speed_elsa.npz'
    x = 41.3
    n = 1000000
    ref_value   = 0.5574635291451433
    check_value = roadster.time_to_destination(x, route, n)
    assert np.isclose(ref_value, check_value), 'time_to_destination(...) not close to reference value'

# Correct output for last value (whole distance)?    
def test_part2a_D():
    route = 'speed_elsa.npz'
    distance_km, _ = roadster.load_route(route)
    x = distance_km[-1]
    n = 10000
    ref_value   = 0.9614649355160398
    check_value = roadster.time_to_destination(x, route, n)
    assert np.isclose(ref_value, check_value), 'time_to_destination(...) not close to reference value'

### PART 2B, TOTAL CONSUMPTION ###
def test_part2b_A():
    route = 'speed_anna.npz'
    x = 15.4
    n = 2
    ref_value   = 2345.1507931020265
    check_value = roadster.total_consumption(x, route, n)
    assert np.isclose(ref_value, check_value), 'total_consumption(...) not close to reference value'

def test_part2b_B():
    route = 'speed_elsa.npz'
    x = 23.7
    n = 1000000
    ref_value   = 3144.142897705084
    check_value = roadster.total_consumption(x, route, n)
    assert np.isclose(ref_value, check_value), 'total_consumption(...) not close to reference value'
    
# Correct output for last value (whole distance)?    
def test_part2b_C():
    route = 'speed_elsa.npz'
    distance_km, _ = roadster.load_route(route)
    x = distance_km[-1]
    n = 1000000
    ref_value   = 8012.794144526329
    check_value = roadster.total_consumption(x, route, n)
    assert np.isclose(ref_value, check_value), 'total_consumption(...) not close to reference value'

### PART 3A, DISTANCE ###
part3_rtol = 1e-15
part3_atol = 2e-4
def isclose(a,b):
    return np.isclose(a, b, atol = part3_atol, rtol = part3_rtol)
def test_part3a_A():
    route = 'speed_anna.npz'
    T = 0.5
    # ref_value computed with n = 10000000 in trap and tol = 1e-10 in Newton
    ref_value   = 51.07040584543483
    check_value = roadster.distance(T, route)
    assert isclose(ref_value, check_value), 'distance(...) not close to reference value'

def test_part3a_B():
    route = 'speed_elsa.npz'
    T = 0.3
    # ref_value computed with n = 10000000 in trap and tol = 1e-10 in Newton
    ref_value   = 21.712201790750854
    check_value = roadster.distance(T, route)
    assert isclose(ref_value, check_value), 'distance(...) not close to reference value'

### PART 3B, REACH ###
def test_part3b_A():
    route = 'speed_anna.npz'
    C = 10000
    # ref_value computed with n = 10000000 in trap and tol = 1e-10 in Newton
    ref_value   = 52.747912349660716
    check_value = roadster.reach(C, route)
    # Check if value is reasonable
    if check_value < 0:
        raise RuntimeError('Your solution is negative!')
    distance_km, _ = roadster.load_route(route)
    if check_value > distance_km[-1]:
        raise RuntimeError('Your solution is greater than the total distance of the route!');        
    assert isclose(ref_value, check_value), 'reach(...) not close to reference value'

def test_part3b_B():
    route = 'speed_elsa.npz'
    C = 5000
    # ref_value computed with n = 10000000 in trap and tol = 1e-10 in Newton
    ref_value   = 37.90826720711255
    check_value = roadster.reach(C, route)
    # Check if value is reasonable
    if check_value < 0:
        raise RuntimeError('Your solution if negative!')
    distance_km, _ = roadster.load_route(route)
    if check_value > distance_km[-1]:
        raise RuntimeError('Your solution is greater than the total distance of the route!');        
    assert isclose(ref_value, check_value), 'reach(...) not close to reference value'

# Code works in case charge is sufficient for whole route?
def test_part3b_C():
    route = 'speed_elsa.npz'
    C = 10000
    distance_km, _ = roadster.load_route(route)
    ref_value   = distance_km[-1]
    check_value = roadster.reach(C, route)
    assert isclose(ref_value, check_value), 'reach(...) not close to reference value'

# Code works in case charge is sufficient for whole route?
def test_part3b_D():
    route = 'speed_anna.npz'
    C = 20000
    distance_km, _ = roadster.load_route(route)
    ref_value   = distance_km[-1]
    check_value = roadster.reach(C, route)
    assert isclose(ref_value, check_value)

### PART 4A, NYC ROUTE TRAVELER EULER ###
def test_part4a_A():
    t0=6.7
    h = 0.6
    time_h, distance_km, speed_kmph = route_nyc.nyc_route_traveler_euler(t0,h)
    # first value in time_h
    ref_value = t0
    assert np.isclose(ref_value,time_h[0]), 'first value in time_h vector should be t0, since that is the starting time'

def test_part4a_B():
    t0=2
    h = 0.4
    t_h, distance_km, speed_kmph = route_nyc.nyc_route_traveler_euler(t0,h)
    # first value in distance_km
    ref_value = 0
    assert np.isclose(ref_value,distance_km[0]), 'first value in distance_km vector should be 0, since no distance have been traveled yet'

def test_part4a_C():
    t0=4
    h = 0.1
    t_h, distance_km, speed_kmph = route_nyc.nyc_route_traveler_euler(t0,h)
    # last value
    ref_value = 60
    assert np.isclose(ref_value,distance_km[-1]), 'last value in distance_km vector should be 60, since that is the length of the route'

def test_part4a_D():
    t0 = 8
    h = 0.5
    time_h, distance_km, speed_kmph = route_nyc.nyc_route_traveler_euler(t0,h)
    # last value in time_h
    ref_value_time_m1 = 10.003611662684603445
    assert np.isclose(ref_value_time_m1,time_h[-1]), 'last value in time_h vector different from reference value'    
    # next to last value in distance_km
    ref_value_dist_m2 = 59.874350255202649862
    assert np.isclose(ref_value_dist_m2,distance_km[-2]), 'next to last value in distance_km vector different from reference value'
    # check first value in speed_kmph
    ref_value_speed_0 = 8.2800000000000011369
    assert np.isclose(ref_value_speed_0,speed_kmph[0]), 'first value in speed_kmph vector different from reference value'    
    # check last value in speed_kmph
    ref_value_speed_m1 = 34.824801684943381019
    assert np.isclose(ref_value_speed_m1,speed_kmph[-1]), 'last value in speed_kmph vector different from reference value'

def test_part4a_E():
    t0 = 12.34
    h = 0.01
    time_h, distance_km, speed_kmph = route_nyc.nyc_route_traveler_euler(t0,h)
    # last value in time_h
    ref_value_time_m1 = 13.742324071473458247
    assert np.isclose(ref_value_time_m1,time_h[-1]), 'last value in time_h vector different from reference value'    
    # next to last value in distance_km
    ref_value_dist_m2 = 59.84313087421196542
    assert np.isclose(ref_value_dist_m2,distance_km[-2]), 'next to last value in distance_km vector different from reference value'
    # check first value in speed_kmph
    ref_value_speed_0 = 7.3818421193875920494
    assert np.isclose(ref_value_speed_0,speed_kmph[0]), 'first value in speed_kmph vector different from reference value'    
    # check last value in speed_kmph
    ref_value_speed_m1 = 67.501135806462414735
    assert np.isclose(ref_value_speed_m1,speed_kmph[-1]), 'last value in speed_kmph vector different from reference value'
