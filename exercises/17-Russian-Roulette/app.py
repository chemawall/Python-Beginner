import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	if spin_chamber() == bullet_position:
		return "You're dead!"
	else:
		return 'Keep playing!'

#atencion que se está igualando la función spin_chamber, no el return de spin chamber


print(fire_gun())