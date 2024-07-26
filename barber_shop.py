cabelo_cliente = int(input("Insira o tamanho do cabelo: "))

if cabelo_cliente <= 20:
    print("Valor do corte: R$50,00")
elif cabelo_cliente >= 21 and cabelo_cliente <= 30:
    print("Valor do corte: R$70,00")
elif cabelo_cliente >= 31 and cabelo_cliente < 50:
    print("Valor do corte: R$100,00")
elif cabelo_cliente > 50:
    print("Favor, combinar valor na recepção")
else:
    print("Verifique novamente o valor inserido.")
