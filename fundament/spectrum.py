def generate_spectrum(num):
    spec = []
    element_spec = (0,0,)
    while num >=1:
        num-=1
        spec.append(element_spec)
    return spec;
