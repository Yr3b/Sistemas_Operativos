import threading
import time,random

class CajaDeAhorro:
    def __init__(self,saldo=0) -> None:
        self.__saldo = saldo
        self.__lock = threading.Lock()

    def depositar(self,monto):
        try:
            self.__lock.acquire()                                           #bloquea el thread para el usuario
            
            print(f"Saldo antes de depositar: {self.__saldo}\n",end="")
            print(f"Monto a ingresar: {monto}\n",end="")
            time.sleep(random.uniform(1,2))                                 #simulo el tiempo del proceso
            self.__saldo+=monto                                             #Transaccion
            print(f"Saldo despues de depositar: {self.__saldo}\n",end="")

        finally:
            self.__lock.release()                                           #cuando termina lo desbloquea para el proximo user

class Usuario(threading.Thread):
    def __init__(self,nombre,caja_de_ahorro:CajaDeAhorro,monto):
        super().__init__()
        self.__nombre = nombre
        self.__caja_de_ahorro = caja_de_ahorro
        self.__monto = monto

    def __depositarDinero(self):
        print(f"{self.__nombre} intenta depositar {self.__monto}\n",end="")
        self.__caja_de_ahorro.depositar(self.__monto)

    def run(self) -> None:
        self.__depositarDinero()

def main():
    caja01 = CajaDeAhorro()
    usuario1 = Usuario("Delepa",caja01,100)
    usuario2 = Usuario("Joseph",caja01,250)
    usuario3 = Usuario("Otsexo",caja01,500)
    usuario4 = Usuario("Otsexo",caja01,600)
    usuario5 = Usuario("Otsexo",caja01,750)
    users = [usuario1,usuario2,usuario3,usuario4,usuario5]

    for user in users:
        user.start() # iniciar la ejecución del hilo y Llama al método run()

    for user in users:
        user.join() # bloquea el hilo principal hasta que el hilo que invocó join() termine su ejecución.
    
main()

# _ propiedad o método es "protegido"
# __ name mangling, que es un mecanismo para renombrar internamente la propiedad o método y evitar conflictos si se hereda la clase.
# -> None es una anotación de tipo que indica el tipo de retorno de la función o método.

# .start() y .join() gestionan el ciclo de vida de un hilo, pero no controlan el acceso a los recursos compartidos.

# .acquire(): Bloquea el acceso al recurso compartido para que solo un hilo pueda acceder a él a la vez. 
#  Cuando un hilo llama a .acquire(), asegura que ningún otro hilo pueda adquirir ese mismo lock hasta que sea liberado.

# .release():
# Libera el lock para que otros hilos puedan adquirirlo. Una vez que el hilo que tiene el lock ha terminado de usar el recurso compartido, debe llamar a .release() para que otros hilos puedan proceder.

# .start() y .join() gestionan el inicio y la sincronización del ciclo de vida de los hilos, pero no controlan el acceso a los recursos compartidos. 
#  Sin .acquire() y .release(), varios hilos podrían acceder a self.__saldo al mismo tiempo, lo que podría llevar a problemas de consistencia