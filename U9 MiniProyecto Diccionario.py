"""
Unidad 9: Mini-Proyecto - Diccionario Inteligente
Ejecutar con: python U9_03_MiniProyecto_Diccionario.py
"""
import sys


class Palabra:
    def __init__(self, texto: str, definicion: str):
        self.texto = texto.lower().strip()
        self.definicion = definicion

    def __lt__(self, otra):
        return self.texto < otra.texto

    def __gt__(self, otra):
        return self.texto > otra.texto

    def __eq__(self, otra):
        return isinstance(otra, Palabra) and self.texto == otra.texto

    def empieza_con(self, prefijo: str) -> bool:
        return self.texto.startswith(prefijo.lower().strip())

    def __repr__(self):
        return f"Palabra('{self.texto}')"

    def __str__(self):
        return f"{self.texto}: {self.definicion}"


class NodoBST:
    def __init__(self, palabra: Palabra):
        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None


class DiccionarioBST:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def insertar(self, palabra: Palabra) -> None:
        if self.raiz is None:
            self.raiz = NodoBST(palabra)
            self.tamano += 1
            return
        self._insertar_rec(self.raiz, palabra)

    def _insertar_rec(self, nodo, palabra):
        if palabra < nodo.palabra:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoBST(palabra)
                self.tamano += 1
            else:
                self._insertar_rec(nodo.izquierdo, palabra)
        elif palabra > nodo.palabra:
            if nodo.derecho is None:
                nodo.derecho = NodoBST(palabra)
                self.tamano += 1
            else:
                self._insertar_rec(nodo.derecho, palabra)

    def buscar(self, texto: str):
        return self._buscar_rec(self.raiz, texto.lower().strip())

    def _buscar_rec(self, nodo, texto):
        if nodo is None:
            return None
        if nodo.palabra.texto == texto:
            return nodo.palabra
        if texto < nodo.palabra.texto:
            return self._buscar_rec(nodo.izquierdo, texto)
        return self._buscar_rec(nodo.derecho, texto)

    def buscar_por_prefijo(self, prefijo: str) -> list:
        resultados = []
        self._prefijo_rec(self.raiz, prefijo.lower().strip(), resultados)
        return resultados

    def _prefijo_rec(self, nodo, prefijo, resultados):
        if nodo is None:
            return
        self._prefijo_rec(nodo.izquierdo, prefijo, resultados)
        if nodo.palabra.empieza_con(prefijo):
            resultados.append(nodo.palabra)
        self._prefijo_rec(nodo.derecho, prefijo, resultados)

    def listar_todas(self) -> list:
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo is None:
            return
        self._inorden(nodo.izquierdo, resultado)
        resultado.append(nodo.palabra)
        self._inorden(nodo.derecho, resultado)

    def altura(self) -> int:
        return self._altura_rec(self.raiz)

    def _altura_rec(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self._altura_rec(nodo.izquierdo), self._altura_rec(nodo.derecho))

    def __len__(self):
        return self.tamano


DATOS_INICIALES = [
    ("abeja", "Insecto himenoptero que produce miel."),
    ("agua", "Liquido transparente esencial para la vida."),
    ("aguja", "Barrita de metal con punta y ojo para coser."),
    ("algoritmo", "Conjunto ordenado de operaciones para resolver un problema."),
    ("amigo", "Persona con la que se tiene afecto y confianza."),
    ("amor", "Sentimiento de afecto intenso hacia alguien."),
    ("anillo", "Aro pequeno que se lleva en los dedos."),
    ("arbol", "Planta lenosa de tronco unico que se ramifica."),
    ("arcoiris", "Fenomeno optico con forma de arco multicolor."),
    ("arena", "Conjunto de granos finos que cubren las playas."),
    ("aurora", "Resplandor que precede al amanecer."),
    ("auto", "Vehiculo de motor con cuatro ruedas para transporte."),
    ("autobus", "Vehiculo de transporte publico de pasajeros."),
    ("autocompletar", "Funcion que completa texto de forma automatica."),
    ("autonomia", "Capacidad de gobernarse por si mismo."),
    ("avion", "Aeronave con alas fijas impulsada por motores."),
    ("azucar", "Sustancia dulce cristalina usada como alimento."),
    ("balon", "Esfera inflada usada en deportes."),
    ("barco", "Embarcacion de gran tamano para navegar."),
    ("biblioteca", "Lugar donde se guardan y consultan libros."),
    ("bicicleta", "Vehiculo de dos ruedas impulsado por pedales."),
    ("bosque", "Extension de terreno cubierta de arboles."),
    ("botella", "Recipiente de cuello estrecho para liquidos."),
    ("cable", "Conductor electrico cubierto de aislamiento."),
    ("cama", "Mueble para dormir o descansar."),
    ("camino", "Via por la que se transita."),
    ("cancion", "Composicion musical para ser cantada."),
    ("casa", "Edificio destinado a vivienda."),
    ("cielo", "Espacio que se ve al mirar hacia arriba."),
    ("ciudad", "Conjunto grande de edificios y habitantes."),
    ("computadora", "Maquina electronica que procesa datos."),
    ("corazon", "Organo muscular que bombea la sangre."),
    ("dado", "Cubo con numeros en sus caras para juegos."),
    ("delfin", "Mamifero marino inteligente."),
    ("diente", "Estructura dura en la boca para masticar."),
    ("dinero", "Medio de pago aceptado en una sociedad."),
    ("dragon", "Criatura mitologica con forma de reptil alado."),
    ("elefante", "Mamifero de gran tamano con trompa y colmillos."),
    ("escuela", "Institucion donde se ensena y aprende."),
    ("estrella", "Cuerpo celeste que emite luz propia."),
    ("familia", "Grupo de personas unidas por parentesco."),
    ("fuego", "Fenomeno que produce luz y calor."),
    ("gato", "Mamifero felino domestico."),
    ("grafo", "Estructura de nodos y aristas."),
    ("hielo", "Agua en estado solido."),
    ("hoja", "Organo verde de las plantas."),
    ("hospital", "Establecimiento para atender enfermos."),
    ("idioma", "Lengua propia de un pueblo o nacion."),
    ("isla", "Porcion de tierra rodeada de agua."),
    ("jardin", "Terreno donde se cultivan plantas."),
    ("jirafa", "Mamifero africano de cuello muy largo."),
    ("juego", "Actividad recreativa con reglas."),
    ("lapiz", "Instrumento para escribir o dibujar."),
    ("libro", "Conjunto de hojas encuadernadas con texto."),
    ("luna", "Satelite natural de la Tierra."),
    ("llave", "Instrumento para abrir o cerrar cerraduras."),
    ("madre", "Mujer que ha dado a luz un hijo."),
    ("mar", "Masa de agua salada que cubre gran parte de la Tierra."),
    ("mesa", "Mueble con superficie plana y patas."),
    ("montana", "Gran elevacion natural del terreno."),
    ("nube", "Masa visible de vapor de agua."),
    ("nino", "Persona de poca edad."),
    ("oceano", "Gran extension de agua salada."),
    ("ojo", "Organo de la vision."),
    ("oso", "Mamifero plantigrado de gran tamano."),
    ("padre", "Hombre que tiene hijos."),
    ("pan", "Alimento hecho de harina y agua."),
    ("pelota", "Esfera usada en juegos y deportes."),
    ("perro", "Mamifero canido domestico."),
    ("pez", "Animal acuatico con aletas y escamas."),
    ("piedra", "Materia mineral solida y dura."),
    ("planta", "Organismo vegetal que crece en la tierra."),
    ("playa", "Zona plana de arena junto al mar."),
    ("programa", "Conjunto de instrucciones para una computadora."),
    ("python", "Lenguaje de programacion de alto nivel."),
    ("raton", "Pequeno mamifero roedor."),
    ("recursividad", "Tecnica donde una funcion se llama a si misma."),
    ("reloj", "Instrumento para medir el tiempo."),
    ("rio", "Corriente natural de agua dulce."),
    ("rosa", "Flor del rosal, generalmente fragante."),
    ("sal", "Compuesto cristalino usado para condimentar."),
    ("semilla", "Parte del fruto que da origen a una planta."),
    ("sol", "Estrella central del sistema solar."),
    ("sombra", "Zona oscura producida al bloquear la luz."),
    ("teclado", "Dispositivo con teclas para escribir."),
    ("tierra", "Planeta en el que vivimos."),
    ("tigre", "Felino salvaje de gran tamano y rayas."),
    ("tren", "Medio de transporte ferroviario."),
    ("uva", "Fruto del que se obtiene el vino."),
    ("vaca", "Mamifero bovino domesticado."),
    ("ventana", "Abertura en la pared para luz y ventilacion."),
    ("viento", "Corriente de aire atmosferico."),
    ("vino", "Bebida alcoholica hecha de uvas fermentadas."),
    ("zapato", "Calzado que cubre el pie."),
    ("zorro", "Mamifero canido salvaje de cola espesa."),
]


def cargar_diccionario() -> DiccionarioBST:
    dicc = DiccionarioBST()
    for texto, definicion in DATOS_INICIALES:
        dicc.insertar(Palabra(texto, definicion))
    return dicc


def menu_interactivo(dicc: DiccionarioBST) -> None:
    while True:
        print("\n" + "=" * 40)
        print("  DICCIONARIO INTELIGENTE")
        print("=" * 40)
        print("1. Buscar palabra exacta")
        print("2. Autocompletar (por prefijo)")
        print("3. Ver diccionario completo")
        print("4. Salir")
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            texto = input("Palabra: ").strip()
            p = dicc.buscar(texto)
            print(f"\n{p}" if p else f"\n'{texto}' no encontrada.")
        elif opcion == "2":
            prefijo = input("Prefijo: ").strip()
            rs = dicc.buscar_por_prefijo(prefijo)
            if rs:
                print(f"\n{len(rs)} resultados:")
                for p in rs:
                    print(f"  - {p.texto}")
            else:
                print("\nSin resultados.")
        elif opcion == "3":
            todas = dicc.listar_todas()
            print(f"\nDiccionario completo ({len(todas)}):")
            for p in todas:
                print(f"  {p.texto}: {p.definicion}")
        elif opcion == "4":
            print("\nHasta pronto.")
            break
        else:
            print("Opcion invalida.")


def demo_automatica(dicc: DiccionarioBST) -> None:
    print("=" * 50)
    print("  DEMO AUTOMATICA DEL DICCIONARIO")
    print("=" * 50)
    print(f"\n[INFO] Palabras cargadas: {len(dicc)}")
    print(f"[INFO] Altura del arbol: {dicc.altura()}")

    print("\n[1] Busqueda exacta de 'python':")
    print(f"    {dicc.buscar('python')}")

    print("\n[2] Autocompletar 'au':")
    for p in dicc.buscar_por_prefijo("au"):
        print(f"    - {p.texto}")

    print("\n[3] Autocompletar 'co':")
    for p in dicc.buscar_por_prefijo("co"):
        print(f"    - {p.texto}")

    print("\n[4] Primeras 10 palabras (inorden = alfabetico):")
    for p in dicc.listar_todas()[:10]:
        print(f"    {p.texto}")

    print("\n[5] Verificacion de orden alfabetico:")
    todas = [p.texto for p in dicc.listar_todas()]
    assert todas == sorted(todas)
    print("    OK - todas en orden alfabetico")


if __name__ == "__main__":
    diccionario = cargar_diccionario()

    # Si se pasa argumento "menu", abre la interfaz interactiva
    if len(sys.argv) > 1 and sys.argv[1] == "menu":
        menu_interactivo(diccionario)
    else:
        demo_automatica(diccionario)
        print("\nPara abrir el menu interactivo:")
        print("  python U9_03_MiniProyecto_Diccionario.py menu")