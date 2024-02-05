import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0 
b = 2 

n = 10000

x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)

under_curve = y_random < f(x_random)
integral_monte_carlo = under_curve.sum() / n * (b - a) * f(b)

integral_quad, error = spi.quad(f, a, b)

def print_results(monte_carlo, quad_res, quad_error, analytical_res):
    print(f"Метод Монте-Карло:\n"
          f"Обчислений інтеграл: {monte_carlo:.6f}\n\n"
          f"Функція 'quad' SciPy:\n"
          f"Обчислений інтеграл: {quad_res:.6f}\n"
          f"Оцінка абсолютної помилки: {quad_error:.2e}\n\n"
          f"Аналітичний розв'язок:\n"
          f"Обчислений інтеграл: {analytical_res:.6f}\n\n"
          f"Різниця між методом Монте-Карло і аналітичним розв'язком: {abs(monte_carlo - analytical_res):.6f}\n"
          f"Різниця між методом Монте-Карло і 'quad': {abs(monte_carlo - quad_res):.6f}")

integral_analytical = (b**3)/3 - (a**3)/3
print_results(integral_monte_carlo, integral_quad, error, integral_analytical)
