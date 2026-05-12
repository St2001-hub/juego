# juego
Documentación breve del código (Sistema de combate POO)
✅ Descripción general
Este programa simula un combate por turnos entre dos personajes usando Programación Orientada a Objetos (POO). Cada personaje tiene atributos básicos como vida, ataque y defensa, y puede atacar con habilidades diferentes dependiendo de su clase.
🧩 Clase principal: Personaje (Abstracta)
📌 Tipo: Clase abstracta (ABC)
📌 Función: Sirve como plantilla para crear personajes.
Atributos privados:
__nombre: Nombre del personaje
__vida: Vida del personaje (0 a 100)
__ataque: Poder de ataque
__defensa: Defensa del personaje
Encapsulamiento:
Se usa @property y @setter para controlar el acceso a la vida.
La vida nunca puede ser menor que 0 ni mayor que 100.
Método abstracto obligatorio:
atacar(objetivo): Cada subclase debe implementarlo con su propia lógica.
⚔️ Subclases (Herencia + Polimorfismo)
🛡️ Guerrero
Aumenta el daño un 20%.
Daño = ataque * 1.2 - defensa del objetivo.
🔥 Mago
Ignora la defensa del enemigo.
Daño = ataque directo.
🏹 Arquero
Si su ataque es mayor que la defensa del enemigo, hace daño doble.
Si no, hace daño normal restando defensa.
🔁 Función combate(p1, p2)
📌 Simula la batalla entre dos personajes:
Se ejecuta un ciclo while mientras ambos tengan vida mayor a 0.
Cada turno:
Ataca el personaje 1
Se verifica si el enemigo murió
Ataca el personaje 2
Se verifica si el enemigo murió
Al final, se imprime el ganador.
🎮 Ejemplo de ejecución
Se crean dos personajes:
Asta como Guerrero
Yuno como Mago
Luego se ejecuta:
Python
combate(Asta, Yuno)
📌 Resultado: se imprime el combate turno por turno hasta que uno quede con vida en 0.
🧠 Conceptos de POO aplicados
✅ Abstracción
✅ Encapsulamiento
✅ Herencia
✅ Polimorfismo
Si quieres, �⁠te la convierto en documentación tipo Word / informe universitario.
