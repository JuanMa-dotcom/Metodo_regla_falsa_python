#Valdez López Juan Manuel
#219406415


import math as m 

def regla_falsa(f, a, b, tol=1e-6, max_iter=1000):
    if f(a) * f(b) > 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos (la raiz debe estar en el intervalo).")

    print(f"\n{'Iter':>4} {'a':>12} {'b':>12} {'c':>12} {'f(c)':>12} {'Error':>12}")
    print("-" * 68)

    c_prev = None
    for i in range(1, max_iter + 1):
        fa, fb = f(a), f(b)
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)

        error = abs(c - c_prev) if c_prev is not None else float('inf')
        print(f"{i:>4} {a:>12.6f} {b:>12.6f} {c:>12.6f} {fc:>12.6e} {error:>12.6e}")

        if abs(fc) < tol or (c_prev is not None and error < tol):
            print(f"\nRaiz encontrada: x = {c:.8f} en {i} iteraciones")
            return c

        if fa * fc < 0:
            b = c
        else:
            a = c

        c_prev = c

    print(f"\nMaximo de iteraciones alcanzado. Ultima aproximacion: x = {c:.8f}")
    return c


#Entrada del usuario
print("=" * 50)
print("   METODO DE REGLA FALSA")
print("=" * 50)
print("Ingresa la funcion f(x). Puedes usar:")
print("  x**2, x**3, m.sin(x), m.cos(x), m.exp(x), m.log(x), etc.")
print()

expr = input("f(x) = ")
f = lambda x: eval(expr)

print()
a = float(input("Limite inferior del intervalo (a): "))
b = float(input("Limite superior del intervalo (b): "))
tol = input("Tolerancia (Enter para 1e-6): ")
tol = float(tol) if tol.strip() else 1e-6

print(f"\nFuncion  : f(x) = {expr}")
print(f"Intervalo: [{a}, {b}]")
print(f"Tolerancia: {tol}")

try:
    raiz = regla_falsa(f, a, b, tol)
    print(f"\nVerificacion: f({raiz:.8f}) = {f(raiz):.2e}")
except ValueError as e:
    print(f"\nError: {e}")