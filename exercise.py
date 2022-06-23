from operator import mul

def list_comprehension():
    #Metodo Normal
    squares = []
    for i in range(1,101):
        if i % 3 != 0:
            squares.append(i**2)

    # Lists comprehensions
    squares = [i**2 for i in range(1,101) if i % 3 != 0]

    multiplies = [i for i in range(1,100) if i % 36 == 0]

def dict_comprehension():
    #Metodo Normal
    cubos = {}
    for i in range(1,101):
        if i % 3 != 0:
            cubos[i] = i**3

    #Dict Comprehension
    cubos = {i:i**3 for i in range(1,101) if i % 3 != 0}
    
    square_root = {i:round(i**0.5,2) for i in range(1,101)}
    print(square_root)

if __name__ == "__main__":
    list_comprehension()
    dict_comprehension()