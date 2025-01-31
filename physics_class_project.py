# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius. It should return c_temp
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
# Define a variable f100_in_celsius and set it equal to the value of f_to_c with 100 as an input
f_100_in_celsius = f_to_c(100)
print(f_100_in_celsius)

# Write a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit. It should then return f_temp
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
# Define a variable c0_in_fahrenheit and set it equal to the value of c_to_f with 0 as an input
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Define a function called get_force that takes in maass and acceleration. It should return mass multiplied by acceleration
def get_force(mass, acceleration):
  return mass * acceleration
#Test get_force by calling it with the variables train_mass and train_acceleration. Save the result to a variable called train_force and print it out
train_force = get_force(train_mass, train_acceleration)
#Print a string including the variable for train_force
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Define a function called get_energy that takes in mass and c
def get_energy(mass, c):
# get_energy should return mass multiplied by c squared
  return mass * (c**2)
# Test get_energy by using it on bomb_mass, with the default value of c. Save the result to a variable called bomb_energy
bomb_energy = get_energy(bomb_mass, c=3*10**8)
# Print a string containing the bomb_energy variable
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Define a function called get_work that takes in mass, acceleration and distance
def get_work(mass, acceleration, distance):
  # Use get_force to get the force and then multiply that by distance
  # Return the result
  return get_force(mass, acceleration) * distance
  # Test get_work by using it on train_mass, train_acceleration and train_distance
  # Save the result to a variable called train_work
train_work = get_work(train_mass, train_acceleration, train_distance)
# Print a string containing the train_work and train_distance variables
print("The GE train does " + str(train_work) + " Joules over " + str(train_distance) + " meters.")

