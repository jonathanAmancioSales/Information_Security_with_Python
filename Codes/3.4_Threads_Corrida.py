from threading import Thread
import time

def Carro(id,v_t):
	x=0
	while x <=50:
		print('Carro {}: {}\n'.format(id,x))
		x+=v_t
		time.sleep(0.5)


print('#'*20)

t_car1 = Thread(target=Carro, args=['1',2])
t_car2 = Thread(target=Carro, args=['2',3])

t_car1.start()
t_car2.start()

print('#'*20)