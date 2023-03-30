print('some example text'.capitalize())

print('some example text'.replace('example', 'modified'))

print(True.bit_length())

print((8).bit_length())

print((5.5).hex())

def function():
    variable = 10
    def subfunction():
        print('variable called from subfunction', variable)
    subfunction()
    print('variable called from function', variable)

function.__call__() # tutaj pokazano demonstracyjnie, że funkcja function posiada metodę call
#                     którą możemy wywołać, co jest równoważne "zwyczajnemu" wywołaniu funkcji

print(function.__name__) # tutaj pobrano nazwę funkcji