def function():
    variable = 10
    def subfunction():
        print('variable called from subfunction', variable)
    subfunction()
    print('variable called from function', variable)

function()


def greeting(name='anonymus'):
    return 'Hello ' + name

greeting()

greeting('Marcin')

def pass_example():
    pass