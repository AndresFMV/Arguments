# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


# Exercise 1 Greet Template
def greet(name: str, greeting_template: str = 'Hello, <name>!'):
    return greeting_template.replace("<name>", name)


# Exercise 2 Force
def force(mass: float, body: str = 'earth'):
    surface_gravity = {'sun': 274, 'jupiter': 24.9, 'neptune': 11.1,
                       'saturn': 10.4, 'earth': 9.8, 'uranus': 8.9,
                       'venus': 8.9, 'mars': 3.7, 'mercury': 3.7,
                       'moon': 1.6, 'pluto': 0.6
                       }
    return mass * surface_gravity.get(body)


# Exercise 3 Gravity
def pull(m1: float, m2: float, d: float):
    gravitational = 6.674*10**-11
    return gravitational * (m1 * m2) / d**2


print(greet('Doc'))
print(greet('Bob', "What's up, <name>!"))
print(force(8.6810 * 10**25, 'earth'))
print(pull(500, 200, 1))
