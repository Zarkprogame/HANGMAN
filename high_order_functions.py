from functools import reduce

def filter_use():
    my_list = [1,2,3,4,5,6,7,8,9,0] 
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    print(odd) #GUARDAMOS LOS NUMEROS IMPARES

def map_use():
    my_list = [1,2,3,4,5]
    squares = list(map(lambda x: x ** 2, my_list))
    print(squares) #ELEVAMOS AL CUADRADO

def reduce_use():
    my_list = [2,2,2,2,2]
    all = reduce(lambda a,b : a*b, my_list)
    print(all) #MULTIPLICAMOS TODO EN LA LISTA
if __name__ == "__main__":
    filter_use()
    map_use()
    reduce_use()