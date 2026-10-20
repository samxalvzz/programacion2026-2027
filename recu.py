fact = lambda n: 1 if n == 0 else n * fact(n - 1)

potencia = lambda a, b: 1 if b == 0 else a * potencia(a, b -1)

long = lambda s: 0 if s == "" else 1 + long(s[1:])

invertir = lambda s: "" if s == "" else invertir(s[1:]) + s[0]

esta = lambda s, c: False if s == "" else s[0] == c or esta(s[1:], c)

ultimo = lambda s: s if len(s) == 1 else ultimo(s[1:])

digitos = lambda n: 1 if n < 10 else 1 + digitos(n // 10)

suma_digitos = lambda n: n if n < 10 else (n % 10) + suma_digitos(n // 10)