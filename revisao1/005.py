produto = input('nome do produto>> ')
preco = float(input('preco do produto>> '))
quantidade = int(input('quantidade>> '))
print(""" 
    1 - dinheiro
    2 - credito
    3 - duas vezes
    4 - tres vezes
    """)

tipodepagamento = input('tipo de pagamento>> ')

totalcompra = preco * quantidade

if tipodepagamento == 'dinheiro':
    print(totalcompra * 0.1)
if tipodepagamento == 'credito':
    print(totalcompra * 0.05)
if tipodepagamento == 'duas vezes':
    print(totalcompra)
if tipodepagamento == 'tres vezes':
    print(totalcompra * 1.05)