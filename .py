 area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

cobertura_por_litro = 3
litros_necessarios = area / cobertura_por_litro
latas_necessarias = int(litros_necessarios / 18)
if litros_necessarios % 18 != 0:
    latas_necessarias += 1
preco_total = latas_necessarias * 80

print("Você precisa comprar", latas_necessarias, "latas de tinta")
print("O preço total é R$", preco_total)
