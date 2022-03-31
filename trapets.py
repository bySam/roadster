#trapets

def trapets ( func , a , b , n ):
    h = (b - a )/ n
    x = np . linspace (a , b , n +1)
    fx = func ( x )
    T = h *( np .sum( fx ) - ( fx [0]+ fx [ -1])/2)
    return T
