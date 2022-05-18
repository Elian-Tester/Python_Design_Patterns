class Observer:
    """
         Observador
    """
    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print(self.name + "Recibir mensaje:" + msg)


class Subject:
    """
         Tema
    """
    def __init__(self):
        self.observers = []

    def add_observers(self, observer):
        self.observers.append(observer)
        return self

    def remove_observer(self, observer):
        self.observers.remove(observer)
        return self

    def notify(self, msg):
        for observer in self.observers:
            observer.update(msg)


xiaoming = Observer("xiaoming")
lihua = Observer("lihua")

rain = Subject()
# Agregar suscripción
rain.add_observers(xiaoming)
rain.add_observers(lihua)

rain.notify("¡Está lloviendo!")

# cancelar suscripción
rain.remove_observer(lihua)

rain.notify("¡Esta tronando!")