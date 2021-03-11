import random, string

def Gerar_Senha(size):
	chars=string.ascii_letters + string.digits + 'ç!@#$%&*()-=+[]{},.;:|?'
	#print(chars)
	rnd = random.SystemRandom() #usa os.urandom;

	password=''.join( rnd.choice(chars) for i in range(size) )
	print('Senha aleatoria gerada: ',password)

#############################
size=int( input('Digite o tamanho da senha: ') )

Gerar_Senha(size)

#############################
for i in range(10):
	Gerar_Senha(size)
#############################