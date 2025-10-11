import sympy as sp
from sympy import pi, tanh, cosh, sinh, simplify, together

# Definição dos símbolos
w, a, q, D, b = sp.symbols('w a q D b')
m = sp.symbols('m', integer=True)

# Expressão para alpha_m
alpha = (m * pi * b) / (2 * a)

# Termos do somatório
sign = (-1)**((m - 1)//2)
term1 = 1 / m**5
term2 = alpha * tanh(alpha) / cosh(alpha)

# Fração mais complicada
numerator = alpha - tanh(alpha) * (1 + alpha * tanh(alpha))
denominator = alpha - tanh(alpha) * (alpha * tanh(alpha) - 1)
term3 = numerator / denominator

# Termo completo
summand = sign * term1 * term2 * term3

# Considera b = a
summand_b = summand.subs(b, a)

# Calcula os primeiros termos da série (m ímpares)
terms = []
for mi in [1, 3, 5, 7, 9]:
    term_eval = summand_b.subs(m, mi)
    terms.append(term_eval)

# Soma parcial simbólica e valor numérico
partial_sum = sum(terms)
numerical_value = partial_sum.evalf()

# Calcula w1_max e w
w1_max = 2 * q * a**4 / (pi * D) * numerical_value
w = (5 * q * a**4) / (384 * D) - w1_max

# Resultado final organizado
w_output = together(w)