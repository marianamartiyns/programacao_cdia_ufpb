# Cálculo da Raiz Quadrada pelo Método de Newton

print("\n== Cálculo de Raiz Quadrada ==")
n = float(input("Digite um número para calcular sua raiz: "))

b = 2
p = (b + (n/2)) / 2

dif = n - (b *b) # Diferença

while abs(dif) < 0.0001:
    
    p = (b + (n/2)) / 2
    b = p
    
print(f"\nA raiz de {n} é, aproximadamente, {p:.4f}")  

