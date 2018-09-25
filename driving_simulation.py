'''
Equations of Motion
-------------------
1) v = u + at           
2) s = ut + 0.5at2      
3) v2 = u2 + 2as

u: initial velocity(speed)
v: final velocity(final speed)
t: time
a: acceleration = rate of change of velocity
s: displacement(distance covered)

For constant speed
------------------
distance = speed * time

'''
from os import system, name

# function clear screen
def clear():
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

# CONSTANT  speed_limit
SPEED_LIMIT = 60

driving_time = int(input('Driving time (s): '))
acceleration = int(input('Acceleration (m/s2): '))
distance = int(input('Distance traveled (m): '))
reached = 0
max_speed = acceleration * driving_time

clear()

for s in range(0, driving_time+1):
    reached += 1
    distance_travelled = 0.5 * acceleration * s**2
    stars = int(distance_travelled / 10)
    print('Duration: {}. Distance: {}'.format(s, '* ' * stars))

print('')

if max_speed >= SPEED_LIMIT:
    print('You drove {}'.format(max_speed))
    print('You\'re driving faster than the allowed speedlimit of {}'.format(SPEED_LIMIT))
else:
    print('Good job! You didn\'t go drove faster than the allowed speedlimit')

if reached < distance:
    print('You did not reached your destination.')
else:
    print('Hurray! you reached your destination')

