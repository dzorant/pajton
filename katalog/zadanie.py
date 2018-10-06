import random
liczba = random.randint(1,10)
print("Jaka liczbe wylosowano")

for i in range(6):
	print("Podejscie: ", i+1)
	
	odp = input("podaj liczbe : ")
	
	if liczba == int(odp):
		print("Brawo, prawidłowa liczba to : ",odp)
		break
	elif liczba > int(odp):
		print("za mało")	
	elif liczba < int(odp):
		print("za dużo")
	else:
		print("No niestety")
	
	

