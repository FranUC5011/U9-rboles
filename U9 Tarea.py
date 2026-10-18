"""
Unidad 9: Arboles - Tarea
Ejecutar con: python U9_02_Tarea.py
"""
from collections import deque


class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    # ---------- INSERCION ----------
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)

    # ---------- BUSQUEDA ----------
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == valor:
            return True
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        return self._buscar_recursivo(nodo_actual.derecho, valor)

    # ---------- RECORRIDOS ----------
    def inorden(self):
        r = []
        self._inorden_rec(self.raiz, r)
        return r

    def _inorden_rec(self, nodo, r):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, r)
            r.append(nodo.valor)
            self._inorden_rec(nodo.derecho, r)

    # ---------- VISUALIZACION ----------
    def mostrar_arbol(self):
        self._imprimir_nodo(self.raiz, "", True)

    def _imprimir_nodo(self, nodo, prefijo, es_izquierdo):
        if nodo is not None:
            self._imprimir_nodo(
                nodo.derecho,
                prefijo + ("|   " if es_izquierdo else "    "),
                False,
            )
            print(prefijo + ("\\-- " if es_izquierdo else "/-- ") + str(nodo.valor))
            self._imprimir_nodo(
                nodo.izquierdo,
                prefijo + ("    " if es_izquierdo else "|   "),
                True,
            )

    # ---------- ALTURA ----------
    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return -1
        return 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho))


# ============================================================
# Tarea 1: eliminar(valor)
# ============================================================
def eliminar(self, valor):
    self.raiz = self._eliminar_rec(self.raiz, valor)


def _eliminar_rec(self, nodo, valor):
    if nodo is None:
        return None
    if valor < nodo.valor:
        nodo.izquierdo = self._eliminar_rec(nodo.izquierdo, valor)
    elif valor > nodo.valor:
        nodo.derecho = self._eliminar_rec(nodo.derecho, valor)
    else:
        # Caso 1 y 2
        if nodo.izquierdo is None:
            return nodo.derecho
        if nodo.derecho is None:
            return nodo.izquierdo
        # Caso 3: dos hijos -> sucesor inorden
        sucesor = self._min_nodo(nodo.derecho)
        nodo.valor = sucesor.valor
        nodo.derecho = self._eliminar_rec(nodo.derecho, sucesor.valor)
    return nodo


def _min_nodo(self, nodo):
    actual = nodo
    while actual.izquierdo is not None:
        actual = actual.izquierdo
    return actual


ArbolBinarioBusqueda.eliminar = eliminar
ArbolBinarioBusqueda._eliminar_rec = _eliminar_rec
ArbolBinarioBusqueda._min_nodo = _min_nodo

print("=" * 50)
print("Tarea 1: Eliminar")
print("=" * 50)
bst = ArbolBinarioBusqueda()
for v in [50, 30, 70, 20, 40, 60, 80]:
    bst.insertar(v)
print("Original:", bst.inorden())

bst.eliminar(20)
print("Eliminar 20 (hoja):", bst.inorden())
assert bst.inorden() == [30, 40, 50, 60, 70, 80]

bst.eliminar(30)
print("Eliminar 30 (un hijo):", bst.inorden())
assert bst.inorden() == [40, 50, 60, 70, 80]

bst.eliminar(50)
print("Eliminar 50 (dos hijos):", bst.inorden())
assert bst.inorden() == [40, 60, 70, 80]
assert bst.buscar(50) is False

bst2 = ArbolBinarioBusqueda()
bst2.insertar(1)
bst2.eliminar(1)
assert bst2.raiz is None
print("Unico nodo eliminado -> arbol vacio OK")
print("OK\n")


# ============================================================
# Tarea 2: BFS por niveles
# ============================================================
def bfs(self):
    if self.raiz is None:
        return []
    resultado = []
    cola = deque([self.raiz])
    while cola:
        nodo = cola.popleft()
        resultado.append(nodo.valor)
        if nodo.izquierdo is not None:
            cola.append(nodo.izquierdo)
        if nodo.derecho is not None:
            cola.append(nodo.derecho)
    return resultado


def bfs_por_niveles(self):
    if self.raiz is None:
        return []
    niveles = []
    cola = deque([self.raiz])
    while cola:
        nivel_actual = []
        tam = len(cola)
        for _ in range(tam):
            nodo = cola.popleft()
            nivel_actual.append(nodo.valor)
            if nodo.izquierdo is not None:
                cola.append(nodo.izquierdo)
            if nodo.derecho is not None:
                cola.append(nodo.derecho)
        niveles.append(nivel_actual)
    return niveles


ArbolBinarioBusqueda.bfs = bfs
ArbolBinarioBusqueda.bfs_por_niveles = bfs_por_niveles

print("=" * 50)
print("Tarea 2: BFS")
print("=" * 50)
bst = ArbolBinarioBusqueda()
for v in [10, 5, 15, 2, 7, 12, 17]:
    bst.insertar(v)
print("Arbol:")
bst.mostrar_arbol()
print("BFS plano:", bst.bfs())
print("BFS por niveles:", bst.bfs_por_niveles())
assert bst.bfs() == [10, 5, 15, 2, 7, 12, 17]
assert bst.bfs_por_niveles() == [[10], [5, 15], [2, 7, 12, 17]]
print("OK\n")


# ============================================================
# Tarea 3: Suma de elementos
# ============================================================
def suma_elementos(self):
    return self._suma_rec(self.raiz)


def _suma_rec(self, nodo):
    if nodo is None:
        return 0
    return nodo.valor + self._suma_rec(nodo.izquierdo) + self._suma_rec(nodo.derecho)


ArbolBinarioBusqueda.suma_elementos = suma_elementos
ArbolBinarioBusqueda._suma_rec = _suma_rec

print("=" * 50)
print("Tarea 3: Suma de elementos")
print("=" * 50)
bst = ArbolBinarioBusqueda()
for v in [10, 5, 15, 2, 7, 12, 17]:
    bst.insertar(v)
print("Suma calculada:", bst.suma_elementos())
assert bst.suma_elementos() == 68
assert bst.inorden() == [2, 5, 7, 10, 12, 15, 17]
print("Arbol intacto. OK\n")


# ============================================================
# Tarea 4: es_completo()
# ============================================================
def es_completo(self):
    return self._es_completo_rec(self.raiz)


def _es_completo_rec(self, nodo):
    if nodo is None:
        return True
    tiene_izq = nodo.izquierdo is not None
    tiene_der = nodo.derecho is not None
    if tiene_izq != tiene_der:
        return False
    return self._es_completo_rec(nodo.izquierdo) and self._es_completo_rec(nodo.derecho)


ArbolBinarioBusqueda.es_completo = es_completo
ArbolBinarioBusqueda._es_completo_rec = _es_completo_rec

print("=" * 50)
print("Tarea 4: es_completo")
print("=" * 50)

bst_c = ArbolBinarioBusqueda()
for v in [10, 5, 15, 2, 7, 12, 17]:
    bst_c.insertar(v)
print("Completo [10,5,15,2,7,12,17]?", bst_c.es_completo())
assert bst_c.es_completo() is True

bst_i = ArbolBinarioBusqueda()
for v in [10, 5, 15, 2]:
    bst_i.insertar(v)
print("Completo [10,5,15,2]?", bst_i.es_completo())
assert bst_i.es_completo() is False

bst_u = ArbolBinarioBusqueda()
bst_u.insertar(42)
assert bst_u.es_completo() is True
assert ArbolBinarioBusqueda().es_completo() is True
print("OK\n")


# ============================================================
# Tarea 5: balancear_arbol()
# ============================================================
def balancear_arbol(self):
    valores_ordenados = self.inorden()
    nuevo = ArbolBinarioBusqueda()
    nuevo.raiz = nuevo._construir_balanceado(
        valores_ordenados, 0, len(valores_ordenados) - 1
    )
    return nuevo


def _construir_balanceado(self, valores, inicio, fin):
    if inicio > fin:
        return None
    medio = (inicio + fin) // 2
    nodo = NodoArbol(valores[medio])
    nodo.izquierdo = self._construir_balanceado(valores, inicio, medio - 1)
    nodo.derecho = self._construir_balanceado(valores, medio + 1, fin)
    return nodo


ArbolBinarioBusqueda.balancear_arbol = balancear_arbol
ArbolBinarioBusqueda._construir_balanceado = _construir_balanceado

print("=" * 50)
print("Tarea 5: Balancear arbol")
print("=" * 50)
bst_deg = ArbolBinarioBusqueda()
for v in range(1, 16):
    bst_deg.insertar(v)
print("Altura original (degenerado):", bst_deg.altura())
assert bst_deg.altura() == 14

bst_bal = bst_deg.balancear_arbol()
print("Altura balanceada:", bst_bal.altura())
print("Arbol balanceado:")
bst_bal.mostrar_arbol()
assert bst_bal.inorden() == list(range(1, 16))
assert bst_bal.altura() == 3
assert bst_deg.altura() == 14
print("Arbol original intacto. OK\n")

print("=" * 50)
print("Todos los tests pasaron")
print("=" * 50)