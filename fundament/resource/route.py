class numError(Exception):
    pass

from numpy import array
def route_dict(num_city):
    route_dict={}
    route_dict[0]=[1,2,3]
    route_dict[1]=[0,2,7]
    route_dict[2]=[0,1,5]
    route_dict[3]=[0,4,8]
    route_dict[4]=[3,5,6]
    route_dict[5]=[2,4,10,12]
    route_dict[6]=[4,7]
    route_dict[7]=[1,6,9]
    route_dict[8]=[3,11,13]
    route_dict[9]=[7,10,11]
    route_dict[10]=[5,9]
    route_dict[11]=[8,9,12]
    route_dict[12]=[5,11,13]
    route_dict[13]=[8,12]
    #throw an exception when num_city isn't equal to the num of city in route
    if num_city != len(route_dict):
        try:
            raise numError()
        except:
            print("Oops!The num_city you are inputting doesn't adapt to the number of cities in the route")
    return route_dict

def generate_route(route_dict):
    n = len(route_dict)
    route =array([65536]*n**2).reshape(n,n)
    for key,val in route_dict.items():
        route[key,key] = 0
        for i in val:
            route[key,i] = 1
    return route

#print(route_dict())
#print(generate_route(route_dict()))
