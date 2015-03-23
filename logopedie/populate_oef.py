import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logopedie.settings')

import django
django.setup()

from oefening.models import *


def populate():

	child_laurens = add_Child('laurensallart','Laurens','Allart',23)

	imgUrl = os.getcwd()+'/static/images/laurens.jpg'
	imgUrl2 = os.getcwd()+'/static/images/chiro.jpg'
	opg1 = add_Opgave('test1',imgUrl,'antw1','antw2','antw3','antw4',1,'Bijwoord','Medium')
	opg2 = add_Opgave('test2',imgUrl2,'antw1','antw2','antw3','antw4',2,'Bijwoord','Medium')

	reeks= add_Oefeningenreeks('reeks1')
	add_Opgave_to_reeks(reeks,opg1)
	add_Opgave_to_reeks(reeks,opg2)

	add_Resultaat(child_laurens,reeks,2,2)

def add_Child(userName, firstName, lastName, age):
	c = Child.objects.get_or_create(userName=userName, firstName=firstName, lastName=lastName, age=age)[0]
	return c

def add_Opgave(name, picture, optie1, optie2, optie3, optie4, correctAnswer, category, difficulty):
	o = Opgave.objects.get_or_create(name=name)[0]
	o.picture = picture
	o.optie1 = optie1
	o.optie2 = optie2
	o.optie3 = optie3
	o.optie4 = optie4
	o.correctAnswer = correctAnswer
	o.category = category
	o.difficulty = difficulty
	o.save()
	return o

def add_Oefeningenreeks(name):
	r = Oefeningenreeks.objects.get_or_create(name=name)[0]
	return r

def add_Opgave_to_reeks(reeks, opgave):
	reeks.oefeningen.add(opgave)

def add_Resultaat(child, oefeningenreeks, grade, total):
	res = Resultaat.objects.get_or_create(child=child,oefeningenreeks=oefeningenreeks,grade=grade,total=total)[0]
	return res


# Start execution here!
if __name__ == '__main__':
	print "Starting Rango population script..."
	populate()