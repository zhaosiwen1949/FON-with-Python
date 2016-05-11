def generate_channel(route,spec_num):
    from .spectrum import generate_spectrum
    city_num = len(route)
    i = 0
    channel = {}
    index = "default"
    while i < city_num:
        j = 0
        while j < city_num:
            if route[i][j] == 1:
                if i <= j:
                    index = str(i)+"-"+str(j)
                else:
                    index = str(j)+"-"+str(i)
                if not index in channel:
                    channel[index] = generate_spectrum(spec_num)
            j += 1
        i += 1
    return channel
