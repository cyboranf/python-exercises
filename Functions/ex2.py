def greeting(name):
    print('Hello ' + name)
    return

result = greeting('Marcin')
print(result) # wynikiem działania funkcji greeting jest None

def greeting(name):
    print('Hello ' + name)
    return None

variable = 10 # pewna zmienna zdefiniowana poza funkcją

def function():
    return variable # funkcja "widzi" tę zmienną i tak możemy jej używać

function()


variable = 10
def function():
    global variable # tutaj wyraźnie zaznaczyliśmy, że chcemy
    # skorzystać z wcześniej zdefiniowanej zmiennej
    variable += 1 # teraz możemy zmodyfikować tę zmienną
    return variable

print(function())