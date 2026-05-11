from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre, vida, ataque, defensa):
        self.__nombre = nombre
        self.__vida = vida  # Atributo privado
        self.__ataque = ataque
        self.__defensa = defensa

    # Getters y Setters con encapsulamiento
    @property
    def nombre(self):
        return self.__nombre

    @property
    def vida(self): 
        return self.__vida

    @vida.setter
    def vida(self, valor):
        # Validación: la vida debe estar entre 0 y 100
        if valor < 0:
            self.__vida = 0
        elif valor > 100:
            self.__vida = 100
        else:
            self.__vida = valor

    @property
    def ataque(self): 
        return self.__ataque

    @property
    def defensa(self): 
        return self.__defensa

    # Método abstracto: fuerza a las subclases a implementar el polimorfismo
    @abstractmethod
    def atacar(self, objetivo):
        pass

# 2. Implementación de Subclases (Herencia y Polimorfismo)

class Guerrero(Personaje):
    def atacar(self, objetivo):
        # Habilidad: 20% de incremento de daño
        daño_base = self.ataque * 1.2
        daño_final = max(0, int(daño_base - objetivo.defensa))
        objetivo.vida -= daño_final
        return f"{self.nombre} (Guerrero) golpea con fuerza: {daño_final} de daño"

class Mago(Personaje):
    def atacar(self, objetivo):
        # Habilidad: Ignora la defensa del objetivo
        daño_final = self.ataque
        objetivo.vida -= daño_final
        return f"{self.nombre} (Mago) lanza un hechizo: {daño_final} de daño (ignora defensa)"

class Arquero(Personaje):
    def atacar(self, objetivo):
        # Habilidad: Si ataque > defensa, daño doble
        if self.ataque > objetivo.defensa:
            daño_final = self.ataque * 2
        else:
            daño_final = max(0, self.ataque - objetivo.defensa)
        
        objetivo.vida -= daño_final
        return f"{self.nombre} (Arquero) dispara flecha: {daño_final} de daño"

# 3. Ciclo de Combate

def combate(p1, p2):
    print(f"--- Batalla: {p1.nombre} vs {p2.nombre} ---")
    turno = 1
    
    while p1.vida > 0 and p2.vida > 0:
        print(f"\n[Turno {turno}]")
        
        # Turno del Personaje 1
        print(p1.atacar(p2))
        print(f"Estado: {p1.nombre} ({p1.vida} HP) | {p2.nombre} ({p2.vida} HP)")
        
        if p2.vida <= 0:
            print(f"\n¡{p2.nombre} ha caído! {p1.nombre} es el ganador.")
            break
            
        # Turno del Personaje 2
        print(p2.atacar(p1))
        print(f"Estado: {p1.nombre} ({p1.vida} HP) | {p2.nombre} ({p2.vida} HP)")
        
        if p1.vida <= 0:
            print(f"\n¡{p1.nombre} ha caído! {p2.nombre} es el ganador.")
            break
            
        turno += 1

# --- Configuración del Duelo ---
ragnar = Guerrero("Ragnar", 100, 30, 20)
gandalf = Mago("Gandalf", 80, 40, 10)

combate(ragnar, gandalf)