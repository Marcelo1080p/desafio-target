def pertence_fibonacci(n):
  a, b = 0, 1
  while b <= n:
      if b == n:
        return True
      a, b = b, a + b
  return n == 0

numero = int(input("Informe um número: "))
if pertence_fibonacci(numero):
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")
